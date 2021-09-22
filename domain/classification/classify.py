import re
import requests


def detect_signatures(data, path):
    
    with open(path, 'r') as file:
        signatures  = file.readlines()

    for url in data.keys():
        try:
            response = requests.get(url).text

            # remove special characters            
            regex = ''
            for signature in signatures:
                signature = re.sub("[^a-zA-Z0-9 ]", '', signature)
                regex += f'{signature}|'

            # test if content has one of the signatures in list
            if re.match(regex[:-1], response, re.IGNORECASE) is not None:
                # send alert
                print('Defacement Detected!')
            
        except Exception as e:
            print(f"Error: {e}")

    return