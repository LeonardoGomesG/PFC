from queue import Queue
import re
# import threading
from typing import Dict
from domain.utils import _sentinel

# from bs4 import BeautifulSoup
import lxml.html
import requests

# Apenas para controle de profundidade em testes
from setup.config import recursive as config_recursive
# from typing import string

max_depth = config_recursive["max_depth"]
depth = 0


def recursive_get_urls_in_domain(base: str, url_queue: Queue, domain: str=None):
    print("Recursive: Finding recursive urls")
    if max_depth:
        print("Recursive: Limiting max_depth:", max_depth)

    urls = scrape_threads(base, url_queue, domain)
    # recursive_event.set()
    # print("recursive_event set")
    # print(recursive_event.is_set())
    url_queue.put(_sentinel)
    print("Recursive: Finished recursion")
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
        

# recursive scraping
def scrape_threads(ref: str, url_queue: Queue, domain: str=None, urls_data: Dict=None):
    global depth
    if urls_data is None:
        urls_data = {}

    if ref not in urls_data.keys() and re.search(domain, ref) and not reached_max_depth(depth):
        r = requests.get(ref)

        # converting to a parser
        s = lxml.html.fromstring(r.text)
        depth += 1
        if not ref.endswith(".pdf") and not ref.endswith(".jpg") and not ref.endswith(".rar") and not re.search("@", ref):
            urls_data[ref] = r
            url_queue.put({ref: r})
            print("\nRecursive:", ref)

            for i in s.xpath('//a[@href]'):

                href = i.get('href')

                try:
                    protocol = re.findall('(\w+)://', ref)[0]
                    hostname = re.findall('://([\w\-.]+)', ref)[0]
                    base = protocol + "://" + hostname
                except:
                    print("Recursive: Out of the domain")
                    continue

                if href:
                    if href.startswith("/"):
                        site = base + href
                    else:
                        site = href

                scrape_threads(site, url_queue, domain, urls_data)

    return urls_data

