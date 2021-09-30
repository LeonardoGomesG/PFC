from queue import Queue
import hashlib
from domain.utils import _sentinel

def compare_hashes_thread(urls_queue: Queue, hits_queue: Queue, write_queue: Queue, data: dict):
    print("Detection: Calculating Hashes")
    diff = 0
    while True:
        url = urls_queue.get()
        if url is _sentinel:
            urls_queue.put(_sentinel)
            hits_queue.put(_sentinel)
            write_queue.put(_sentinel)
            break
            
        url_path = list(url.keys())[0]
        response = url[url_path].text.encode('utf-8')
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
            diff += 1

    print("Detection: ", diff, "differences found")
    print("Detection: Finished hashing")


