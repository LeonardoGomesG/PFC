import json
import logging
from queue import Queue
from typing import Dict

import requests
from setup.config import load_previous_data
from domain.constants import sentinel, data_path
from requests.exceptions import Timeout


def load_data():
    logger = logging.getLogger('LOG')
    if load_previous_data:
        with open(data_path) as file:
            data = json.load(file)
        file.close()
        logger.info("AUXILIAR: Previous data loaded")
        return data
    else:
        logger.info("AUXILIAR: Previous data not loaded")


def write_data(data):
    with open(data_path, "w") as file:
        json.dump(data, file, indent=2, sort_keys=True)
    file.close()

def write_append_data(append_data):
    with open(data_path, "r+") as file:
        data = json.load(file)
        data.update(append_data)
        file.seek(0)
        json.dump(data, file, indent=2, sort_keys=True)
    file.close()

def write_data_thread(data: Dict, write_queue: Queue):
    logger = logging.getLogger('LOG')
    data = {}
    while True:
        new_data = write_queue.get()
        if new_data is sentinel:
            write_queue.put(sentinel)
            break

        data.update(new_data)

        if len(data.keys()) > 100:
            logger.info("AUXILIAR: Writing Data to data.json\n")
            write_append_data(data)
            data.clear()
        
    logger.info("AUXILIAR: Writing remaining Data to data.json")
    write_append_data(data)
    logger.info("AUXILIAR: All data saved successfully\n")
    data.clear()

def fill_urls_queue_thread(data: Dict, urls_queue: Queue):
    logger = logging.getLogger('LOG')
    logger.info("AUXILIAR: rerun_recursive set to false")
    logger.info("AUXILIAR: begin loading previous data and requests into queue...\n")

    for url in data:
        logger.info(f"AUXILIAR: getting request for: {url}")
        try:
            request = requests.get(url, timeout=10)
        except Timeout:
            logger.info(f"AUXILIAR: timeout for {url}")
            continue

        urls_queue.put((url, request))

    urls_queue.put(sentinel)

    logger.info("AUXILIAR: Previous data loaded onto queue\n")






