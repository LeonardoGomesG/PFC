from domain.logs import configure_logs, log_end
from setup.config import recursive as config_recursive, rerun_recursion
from domain.detection.hashing import compare_hashes_thread
from domain.recursive.scraping import recursive_get_urls_in_domain
from domain.utils import fill_urls_queue_thread, load_data, write_data_thread
from domain.classification.classify import classify_thread
import concurrent.futures
from queue import Queue

base = config_recursive["base"]
base_domain = config_recursive["domain"]
if __name__ == '__main__':
    configure_logs()
    data = load_data()
    urls_queue = Queue()
    write_queue = Queue()
    hits_queue = Queue()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        if rerun_recursion:
            executor.submit(recursive_get_urls_in_domain, base, urls_queue, base_domain)
        else:
            executor.submit(fill_urls_queue_thread, data, urls_queue)

        executor.submit(compare_hashes_thread, urls_queue, hits_queue, data)
        executor.submit(classify_thread, hits_queue, write_queue)
        executor.submit(write_data_thread, write_queue)
    
    log_end()

