from queue import Queue
import re
from typing import Dict
from domain.constants import sentinel

import lxml.html
import requests
from requests.exceptions import Timeout

from setup.config import recursive as config_recursive

import logging
# Controling depth for testing
max_depth = config_recursive["max_depth"]
depth = 0


def recursive_get_urls_in_domain(base: str, url_queue: Queue, domain: str=None):
    logger = logging.getLogger('LOG')
    if max_depth:
        logger.info(f"RECURSIVE: Limiting max_depth: {max_depth}")

    logger.info(f"RECURSIVE: Finding recursive urls from {base}\n")
    if not is_inside_domain(base, domain):
        url_queue.put(sentinel)
        logger.error(f"CONFIG_ERROR: base url out of the domain!")


    urls = scrape_threads(base, url_queue, domain)
    url_queue.put(sentinel)
    logger.info(f"RECURSIVE: Finished recursion from {base}\n")
    return urls


def reached_max_depth(current_depth):
    if max_depth:
        return current_depth >= max_depth
    else:
        return False

def valid_url(ref):
    return not ref.endswith(".pdf") \
        and not ref.endswith(".jpg") \
        and not ref.endswith(".rar") \
        and not re.search("@", ref)

def is_inside_domain(ref, domain):
    if domain:
        return re.search(domain, ref)
    else:
        return True
        

# recursive scraping
def scrape_threads(ref: str, url_queue: Queue, domain: str=None, urls_data: Dict=None):
    logger = logging.getLogger('LOG')
    global depth
    if urls_data is None:
        urls_data = {}

    if ref not in urls_data.keys() and is_inside_domain(ref, domain) and not reached_max_depth(depth):
        try:
            request = requests.get(ref, timeout=10)
        except Timeout:
            logger.info(f"RECURSIVE: timeout for {ref}")
            request = None
            return

        # converting to a parser
        s = lxml.html.fromstring(request.text)
        depth += 1

        logger.info(f"RECURSIVE: {ref}")
        urls_data[ref] = request
        url_queue.put((ref, request))
        
        # search for a.href tag, expansion possibility for other tags
        for i in s.xpath('//a[@href]'):
            href = i.get('href')

            try:
                protocol = re.findall('(\w+)://', ref)[0]
                hostname = re.findall('://([\w\-.]+)', ref)[0]
                base = protocol + "://" + hostname
            except:
                logger.info("RECURSIVE: Out of the domain")
                continue

            if href:
                if href.startswith("/"):
                    site = base + href
                else:
                    site = href

            if valid_url(site):
                scrape_threads(site, url_queue, domain, urls_data)

    return

