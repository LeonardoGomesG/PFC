import re
import requests
import lxml.html


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
    return re.match(signatures_regex, content, re.IGNORECASE) is not None

def detect_image(content):
    ''' Return true for pages in which body is only an image'''

    html = lxml.html.fromstring(content)
    filter = html.xpath('//body[count(./img)=1]')
    return len(filter) == 1

def classify(data, path):

    regex = get_signatures_regex(path)
    for url in data.keys():
        try:
            response = requests.get(url).text

            if detect_signature(response, regex) or detect_image(response):
                # send alert
                print('Defacement Detected!')
            
        except Exception as e:
            print(f"Error: {e}")

    return

