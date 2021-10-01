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

def classify_thread(hits_queue: Queue):
    print("CLASSIFICATION: Classifying hash differences")
    print("CLASSIFICATION: Getting regex signatures")
    signatures_regex = get_signatures_regex(config_signatures["path"])
    diff = 0
    defaced_urls = []
    while True:
        hit = hits_queue.get()
        if hit is _sentinel:
            hits_queue.put(_sentinel)
            break

        try:
            url = list(hit.keys())[0]
            raw_response = hit[url]
            response = raw_response.text

            protocol = re.findall('(\w+)://', url)[0]
            hostname = re.findall('://([\w\-.]+)', url)[0]
            base = protocol + "://" + hostname

            if detect_signature(response, signatures_regex) or detect_image(response, base, signatures_regex):
                print(f"CLASSIFICATION: Defacement Detected for {url}!")
                diff += 1 
                defaced_urls.append(url)
                send_email(config_notification["to_email"], 'PFC Notification', f'Defacement Detected for {url}!')
            else:
                print("CLASSIFICATION: No defacement detected for", url)  

        except Exception as e:
            print(f"CLASSIFICATION: ERROR: {e}")

    print('CLASSIFICATION: Classification finished')   
    print(f"CLASSIFICATION: Defaced Urls: \n{defaced_urls}") 
    return 

