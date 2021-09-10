import re

from bs4 import BeautifulSoup
import requests

# Apenas para controle de profundidade em testes
from setup.config import recursive as config_recursive

max_depth = config_recursive["max_depth"]
depth = 0


def recursive_get_urls_in_domain(base, domain=None):
    print("Finding recursive urls")
    if max_depth:
        print("Limiting max_depth:", max_depth)
    return scrape(base, domain)


def reached_max_depth(current_depth):
    if max_depth:
        return current_depth > max_depth
    else:
        return False

# recursive scraping
def scrape(ref, domain=None, data=None):
    global depth
    # print("deph = ", depth)
    if data is None:
        data = {}

    r = requests.get(ref)

    # converting to a parser
    s = BeautifulSoup(r.text, "html.parser")

    depth += 1
    for i in s.find_all("a"):

        href = i.get('href')

        try:
            protocol = re.findall('(\w+)://', ref)[0]
            hostname = re.findall('://([\w\-.]+)', ref)[0]
            base = protocol + "://" + hostname
        except:
            print("Out of the domain")
            continue

        if href:
            if href.startswith("/"):
                site = base + href
            else:
                site = href

            # search limited by domain and depth
            if site not in data.keys() and re.search(domain, site) and not reached_max_depth(depth):
                if not site.endswith(".pdf") and not site.endswith(".jpg") and not site.endswith(".rar") and not re.search("@", site):
                    print(site)
                    data[site] = None
                    # print("\n", data.keys())
                    scrape(site, domain, data)

    return data
