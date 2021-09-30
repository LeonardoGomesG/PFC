from setup.config import recursive as config_recursive
from setup.config import signatures as config_signatures
from domain.detection.hashing import compare_hashes_thread
from domain.recursive.scraping import recursive_get_urls_in_domain
from domain.utils import load_data, write_data_thread
from domain.classification.classify import classify_thread
import concurrent.futures
from queue import Queue


base = config_recursive["base"]
domain = config_recursive["domain"]
signatures_path = config_signatures["path"]

if __name__ == '__main__':
    data = load_data()
    urls_queue = Queue()
    write_queue = Queue()
    hits_queue = Queue()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.submit(recursive_get_urls_in_domain, base, urls_queue, domain)
        executor.submit(compare_hashes_thread, urls_queue, hits_queue, write_queue, data)
        executor.submit(write_data_thread, data, write_queue)
        executor.submit(classify_thread, hits_queue)


    # urls = recursive_get_urls_in_domain(base, domain)
    # data = load_data()
    # data = compare_hashes_thread(urls, data)
    # classify(data, signatures_path)
    # write_data(data)
