import logging
from queue import Queue
import hashlib
from domain.constants import sentinel


def compare_hashes_thread(urls_queue: Queue, hits_queue: Queue, data: dict, recursive_threads_count: int):
    logger = logging.getLogger('LOG')
    logger.info("DETECTION: Calculating Hashes\n")
    diff = 0
    sentinel_count = 0
    while True:
        url = urls_queue.get()
        if url is sentinel: 
            sentinel_count +=1
            # print("SENTINEL_COUNT: ", sentinel_count)
            if sentinel_count == recursive_threads_count:
                urls_queue.put(sentinel)
                hits_queue.put(sentinel)
                break
            
            continue

        url_path = url[0]
        raw_response = url[1]
        response = raw_response.text.encode('utf-8')
        # create a hash
        logger.info(f"DETECTION: hashing {url_path}")

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
            logger.info(f"DETECTION: Hash difference for {url_path}: {previous_hash}")
            logger.info(f"DETECTION: new_hash: {new_hash}")
            diff += 1
        

    logger.info(f"DETECTION: {diff} differences found")
    logger.info("DETECTION: Finished hashing\n")


