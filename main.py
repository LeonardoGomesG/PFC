from domain.logs import configure_logs, log_end
from setup.config import recursive as config_recursive, rerun_recursion, max_threads
from domain.detection.hashing import compare_hashes_thread
from domain.recursive.scraping import recursive_get_urls_in_domain
from domain.utils import fill_urls_queue_thread, load_data, write_data_thread
from domain.classification.classify import classify_thread
import concurrent.futures
from queue import Queue

bases = config_recursive["base"]
bases_domains = config_recursive["domain"]
if __name__ == '__main__':
    configure_logs()
    data = load_data()
    urls_queue = Queue()
    write_queue = Queue()
    hits_queue = Queue()
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.submit(compare_hashes_thread, urls_queue, hits_queue, data, len(bases))
        executor.submit(classify_thread, hits_queue, write_queue)
        executor.submit(write_data_thread, write_queue)
        if rerun_recursion:
            for (base, base_domain) in zip(bases, bases_domains):
                executor.submit(recursive_get_urls_in_domain, base, urls_queue, base_domain)

        else:
            executor.submit(fill_urls_queue_thread, data, urls_queue)

    
    log_end()

