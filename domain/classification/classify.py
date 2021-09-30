from queue import Queue
import re
import lxml.html
from lxml import etree
import requests
from domain.utils import _sentinel
from setup.config import signatures as config_signatures

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
    # print(content)
    return re.search(signatures_regex, content, re.IGNORECASE) is not None

def detect_image(content):
    ''' Return true for pages in which body is only an image'''

    html = lxml.html.fromstring(content)
    filter = html.xpath('//body[count(./img)=1]')
    return len(filter) == 1

# def classify(data, signatures_path):
#     regex = get_signatures_regex(signatures_path)
#     for url in data.keys():
#         try:
#             response = requests.get(url).text

#             if detect_signature(response, regex) or detect_image(response):
#                 # send alert
#                 print('Defacement Detected!')
            
#         except Exception as e:
#             print(f"Error: {e}")

#     return

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
            # response = raw_response.text

            response = requests.get(url).text

            # print("------------------------------")
            # print(response)
            # print("-------------------------------------------")

            if detect_signature(response, signatures_regex) or detect_image(response):
                # send alert
                print(f"CLASSIFICATION: Defacement Detected for {url}!")
                diff += 1 
                defaced_urls.append(url)
            else:
                print("CLASSIFICATION: No defacement detected for", url)  

        except Exception as e:
            print(f"CLASSIFICATION: ERROR: {e}")

    print('CLASSIFICATION: Classification finished')   
    print(f"CLASSIFICATION: Defaced Urls: \n{defaced_urls}") 
    return 


        # for url in data.keys():
        #     try:
        #         response = requests.get(url).text

        #         if detect_signature(response, signatures_regex) or detect_image(response):
        #             # send alert
        #             print('Defacement Detected!')
                
        #     except Exception as e:
        #         print(f"Error: {e}")

        # return

