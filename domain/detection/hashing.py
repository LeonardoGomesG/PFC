from queue import Queue
import threading
import time
import hashlib
import requests
from domain.utils import _sentinel


# def compare_hashes(data):
#     print("\nDetection: Calculating Hashes")
#     time.sleep(1)
#     diff = 0
#     for url_path in data.keys():
#         try:
#             response = requests.get(url_path).text.encode('utf-8')
#             # create a hash
#             new_hash = hashlib.md5(response).hexdigest()

#             # check if new hash is same as the previous hash
#             if new_hash == data[url_path]:
#                 continue

#             # if something changed in the hashes
#             else:
#                 # notify
#                 #call classify()
#                 print("Detection: Hash difference for: ", url_path, ": ", data[url_path])
#                 print("Detection: new_hash: ", new_hash, "\n")
#                 data[url_path] = new_hash
#                 diff += 1
#                 continue

#         # To handle exceptions
#         except Exception as e:
#             print("Detection: error")

#     print("Detection: ", diff, "differences found")
#     return data


def compare_hashes_thread(urls_queue: Queue, hits_queue: Queue, write_queue: Queue, data: dict):
    print("Detection: Calculating Hashes")
    # print(recursive_event.is_set())
    # print(urls_queue.empty())
    diff = 0
    while True:
    # while not recursive_event.is_set() or not urls_queue.empty():
        # time.sleep(1)
        # diff = 0
        url = urls_queue.get()
        if url is _sentinel:
            urls_queue.put(_sentinel)
            hits_queue.put(_sentinel)
            write_queue.put(_sentinel)
            break
            
        # print("Detection: url_queue_size: ", urls_queue.qsize(), "\n")

    # for url_path in urls.keys(): 
    #create a thread for each
        # try:
        url_path = list(url.keys())[0]
        response = url[url_path].text.encode('utf-8')
        # response = requests.get(url_path).text.encode('utf-8')
        # create a hash
        print("Detection: hashing", url_path)
        
        new_hash = hashlib.md5(response).hexdigest()

        try:
            previous_hash = data[url_path]
        except:
            previous_hash = None

        # check if new hash is same as the previous hash
        if url_path in data.keys() and new_hash == previous_hash:
            continue

        # if something changed in the hashes or new page
        else:
            # notify
            #call classify()
            hits_queue.put({url_path: new_hash})
            write_queue.put({url_path: new_hash})
            print("Detection: Hash difference for: ", url_path, ": ", previous_hash)
            print("Detection: new_hash: ", new_hash)
            # data[url_path] = new_hash
            diff += 1

        # To handle exceptions
        # except Exception as e:
        #     print("Detection: ERROR", e)

    #join threads and return data or save to file a batch
    print("Detection: ", diff, "differences found")
    print("Detection: Finished hashing")

    # hashing_event.is_set()

    # return data

