import re

from bs4 import BeautifulSoup
import requests

# Apenas para controle de profundidade em testes
depth = 0


# função recursiva
def scrape(ref, data=None, domain=None):
    global depth
    print("deph = ", depth)
    if data is None:
        data = []

    r = requests.get(ref)

    # convertendo o texto, para um parser
    s = BeautifulSoup(r.text, "html.parser")

    try:
        base = re.findall("(^\S+)" + domain, ref)[0]
        base = base + domain
    except:
        print("Url out of the domain:", ref)
        return data

    for i in s.find_all("a"):

        href = i.get('href')

        if href:
            if href.startswith("/"):
                site = base + href
            else:
                site = href

            # escopo da pesquisa limitado a base e profundidade
            if re.search(domain, site) and depth < 50:
                if not href.endswith(".pdf") and not href.endswith(".jpg") and not href.endswith(".rar"):
                    print(site)
                    depth += 1
                    if site not in data.keys():
                        data[site] = None

                    scrape(site, data, domain)

    return data
