# Importing libraries
import time
import hashlib
from urllib.request import urlopen, Request

# setting the URL you want to monitor
# url = Request('https://leetcode.com/',
#               headers={'User-Agent': 'Mozilla/5.0'})
import requests


def get_hashes(urls):
    return

#
# def compare_hashes(url):
#     # to perform a GET request and load the
#     # content of the website and store it in a var
#     response = urlopen(url).read()
#
#     # to create the initial hash
#     currentHash = hashlib.sha256(response).hexdigest()
#     print("running")
#     time.sleep(1)
#     while True:
#         try:
#             # perform the get request and store it in a var
#             response = urlopen(url).read()
#
#             # create a hash
#             currentHash = hashlib.sha256(response).hexdigest()
#             print(currentHash, '\n')
#             # wait for 30 seconds
#             time.sleep(5)
#
#             # perform the get request
#             response = urlopen(url).read()
#
#             # create a new hash
#             newHash = hashlib.sha256(response).hexdigest()
#
#             # check if new hash is same as the previous hash
#             if newHash == currentHash:
#                 continue
#
#             # if something changed in the hashes
#             else:
#                 # notify
#                 print("something changed")
#
#                 # again read the website
#                 response = urlopen(url).read()
#
#                 # create a hash
#                 currentHash = hashlib.sha256(response).hexdigest()
#                 print(currentHash, '\n')
#
#                 # wait for 30 seconds
#                 time.sleep(5)
#                 continue
#
#         # To handle exceptions
#         except Exception as e:
#             print("error")


def compare_hashes_path(data):
    # to perform a GET request and load the
    # content of the website and store it in a var
    # response = requests.get(url_path).text.encode('utf-8')

    # to create the initial hash
    # currentHash = hashlib.sha256(response).hexdigest()
    print("Finding Hashes")
    time.sleep(1)
    # while True:
    for url_path in data.keys():
        try:
            # perform the get request and store it in a var
            response = requests.get(url_path).text.encode('utf-8')

            # create a hash
            newHash = hashlib.sha256(response).hexdigest()
            # print(url_path, ":", newHash, '\n')
            # wait for 30 seconds
            # time.sleep(5)

            # check if new hash is same as the previous hash
            if newHash == data[url_path]:
                continue

            # if something changed in the hashes
            else:
                # notify
                print("Hash difference for: ", url_path, ": ", data[url_path])
                print("NewHash: ", newHash, "\n")
                data[url_path] = newHash

                # wait for 30 seconds
                # time.sleep(5)
                continue

        # To handle exceptions
        except Exception as e:
            print("error")

    return data