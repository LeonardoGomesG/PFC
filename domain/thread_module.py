import concurrent.futures
from domain.utils import write_data
import logging
from queue import Queue
import random
import threading
import time

# def producer(queue, event):
#     """Pretend we're getting a number from the network."""
#     while not event.is_set():
#         message = random.randint(1, 101)
#         logging.info("Producer got message: %s", message)
#         queue.put(message)

#     logging.info("Producer received event. Exiting")

# def consumer(queue, event):
#     """Pretend we're saving a number in the database."""
#     while not event.is_set() or not queue.empty():
#         message = queue.get()
#         logging.info(
#             "Consumer storing message: %s (size=%d)", message, queue.qsize()
#         )
# 
    # logging.info("Consumer received event. Exiting")

def scraping_producer(urls_queue, event):
    """Pretend we're getting a number from the network."""
    while not event.is_set():
        # scraping() -> urls_queue.put({urls: url.get()})
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        urls_queue.put(message)

    logging.info("Producer received event. Exiting")


def hash_consumer(urls_queue, hits_queue, write_queue, event):
    """Pretend we're saving a number in the database."""
    while not event.is_set() or not urls_queue.empty():
        urls = urls_queue.get()
        #hash(urls)
        # -> hits_queue.put(hits)
        # -> write_queue.put(data)

        logging.info(
            "Consumer storing message: %s (size=%d)", urls, urls_queue.qsize()
        )

    logging.info("Consumer received event. Exiting")


def classify_consumer(hits_queue, event):
    """Pretend we're saving a number in the database."""
    while not event.is_set() or not hits_queue.empty():
        hit = hits_queue.get()
        
        #classify(hit)

        logging.info(
            "Consumer storing message: %s (size=%d)", hit, hits_queue.qsize()
        )

    logging.info("Consumer received event. Exiting")

def write_consumer(write_queue, event):
    """Pretend we're saving a number in the database."""
    data = {}
    while not event.is_set() or not write_queue.empty():
        new_data = write_queue.get()
        data.update(new_data)

        if len(data.keys()) > 100:
            write_data(data)
            data.clear()
        
        #hash(urls)
        # -> hits_queue.put(hits)
        # -> write_queue.put(data)

        logging.info(
            "Consumer storing message: %s (size=%d)", new_data, write_queue.qsize()
        )

    # if data:
    write_data(data)
    data.clear()

    logging.info("Consumer received event. Exiting")


# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")

#     pipeline = queue.Queue(maxsize=10)
#     event = threading.Event()
#     with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#         executor.submit(producer, pipeline, event)
#         executor.submit(consumer, pipeline, event)

#         time.sleep(0.1)
#         logging.info("Main: about to set event")
#         event.set()

if __name__ == "__main__":
    data_queue = Queue()
    url_queue = Queue()
    