from domain.utils import _sentinel
from setup.config import signatures as config_signatures
from setup.config import notification as config_notification
import pytesseract
import requests
from PIL import Image
from queue import Queue
import re
import lxml.html
from io import BytesIO
from domain.notification.notifiy import send_email 
import logging
from queue import Queue
import re
import lxml.html
from domain.constants import sentinel, signatures_path


pytesseract.pytesseract.tesseract_cmd = config_signatures['tesseract']


def get_signatures_regex(path):
    ''' Return regex of all signatures in specified file, without special characters'''

    with open(path, 'r') as file:
        signatures  = file.readlines()
            

    regex = ''
    for signature in signatures:
        signature = re.sub("[^a-zA-Z0-9 ]", '', signature)
        regex += f'{signature}|'

    return regex[:-1]

def detect_signature(content, signatures_regex):
    return re.search(signatures_regex, content, re.IGNORECASE) is not None

def detect_image(content, base, regex):
    ''' Return true for pages in which body is only an image and image contains signatur'''

    html = lxml.html.fromstring(content)
    images = html.xpath('//body[count(./img)=1]/img')
    if len(images)==1:

        src = images[0].get('src')
        if src.startswith("/"):
            url = base + src
        else:
            url = src

        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        content = pytesseract.image_to_string(img)
        content = re.sub("[^a-zA-Z0-9 ]", '', content)
        
        return detect_signature(content, regex)
    return False

def classify_thread(hits_queue: Queue, write_queue: Queue):
    logger = logging.getLogger('LOG')
    logger.info("CLASSIFICATION: Classifying hash differences")
    logger.info("CLASSIFICATION: Getting regex signatures\n")
    signatures_regex = get_signatures_regex(signatures_path)
    defaced_urls = []
    while True:
        hit = hits_queue.get()
        if hit is sentinel:
            hits_queue.put(sentinel)
            write_queue.put(sentinel)
            break

        url = hit[0]
        raw_response = hit[1]
        hash = hit[2]
        response = raw_response.text
        try:
            url = list(hit.keys())[0]
            raw_response = hit[url]
            response = raw_response.text

            protocol = re.findall('(\w+)://', url)[0]
            hostname = re.findall('://([\w\-.]+)', url)[0]
            base = protocol + "://" + hostname

            if detect_signature(response, signatures_regex) or detect_image(response, base, signatures_regex):
                logger.info(f"CLASSIFICATION: Defacement Detected for {url}!\n")

                defaced_urls.append(url)
                send_email(config_notification["to_email"], 'PFC Notification', f'Defacement Detected for {url}!')
            else:
                write_queue.put({url: hash})
                logger.info(f"CLASSIFICATION: No defacement detected for {url}\n")  

        except Exception as e:
            logger.info(f"CLASSIFICATION: ERROR: {e}")


    logger.info('CLASSIFICATION: Classification finished')   
    logger.info(f"CLASSIFICATION: Defaced Urls: \n{defaced_urls}") 
    return 

