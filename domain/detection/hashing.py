from queue import Queue
import hashlib
from domain.constants import sentinel


def compare_hashes_thread(urls_queue: Queue, hits_queue: Queue, data: dict):
    print("DETECTION: Calculating Hashes")
    diff = 0
    while True:
        url = urls_queue.get()
        if url is sentinel:
            urls_queue.put(sentinel)
            hits_queue.put(sentinel)
            break
            
        url_path = url[0]
        raw_response = url[1]
        response = raw_response.text.encode('utf-8')
        # create a hash
        print(f"DETECTION: hashing {url_path}")

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
            hits_queue.put((url_path, raw_response, new_hash))
            print(f"DETECTION: Hash difference for {url_path}: {previous_hash}")
            print(f"DETECTION: new_hash: {new_hash}")
            diff += 1

    print(f"DETECTION: {diff} differences found")
    print("DETECTION: Finished hashing")


