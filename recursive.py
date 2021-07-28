from bs4 import BeautifulSoup
import requests

base = "http://www.ime.eb.mil.br"


# função recursiva
def scrape(ref, urls=None):
    # fazendo o request para a url
    if urls is None:
        urls = []

    r = requests.get(ref)

    # convertendo o texto, para um parser
    s = BeautifulSoup(r.text, "html.parser")

    for i in s.find_all("a"):

        href = i.get('href')
        site = ref

        if href:
            if href.startswith("/"):
                site = base + href
            elif href.startswith("http"):
                site = href

            # escopo da pesquisa limitado a base
            if site not in urls and site.startswith(base):
                urls.append(site)
                print(site)
                # recursividade
                if not href.endswith(".pdf") and not href.endswith(".jpg") and not href.endswith(".rar"):
                    scrape(site, urls)

    return urls

