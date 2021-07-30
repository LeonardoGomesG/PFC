import re

from bs4 import BeautifulSoup
import requests

# Apenas para controle de profundidade em testes
depth = 0


def recursive_get_urls_in_domain(base, domain=None):
    print("Finding recursive urls")
    return scrape(base, domain)


# função recursiva
def scrape(ref, domain=None, data=None):
    global depth
    # print("deph = ", depth)
    if data is None:
        data = {}

    r = requests.get(ref)

    # convertendo o texto, para um parser
    s = BeautifulSoup(r.text, "html.parser")

    try:
        base = re.findall("(^\S+)" + domain, ref)[0]
        base = base + domain
    except:
        print("Url out of the domain:", ref)
        return data
    depth += 1
    for i in s.find_all("a"):

        href = i.get('href')

        if href:
            if href.startswith("/"):
                site = base + href
            else:
                site = href

            # escopo da pesquisa limitado a base e profundidade
            if site not in data.keys() and re.search(domain, site) and depth < 50:
                if not href.endswith(".pdf") and not href.endswith(".jpg") and not href.endswith(".rar"):
                    print(site)
                    # recursividade
                    data[site] = None
                    scrape(site, domain, data)

    return data
