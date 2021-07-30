# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from urllib.request import urlopen, Request

import re

import requests
import difflib

from hashing import compare_hashes_path
from recursive import scrape
from utils import load_data, write_data

# url = Request("http://www.ime.eb.mil.br",
#               headers={'User-Agent': 'Mozilla/5.0'})
#
# url_path = 'https://leetcode.com/'

base = "http://www.ime.eb.mil.br"
domain = "ime.eb.mil.br"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    data = load_data()
    data = scrape(base, data, domain)
    data = compare_hashes_path(data)
    write_data(data)
    # print(data.keys())

    # test = "http://www.ime.eb.mil.br/banana/maca"
    # print(re.findall("(^\S+)."+domain, test)[0])
    # urls = scrape(base)
    # response = urlopen(url).read()
    # request = requests.get(url_path).text
    # print(re.search("eb.mil.br", base))
    # compare_hashes_path(base)
    # compare_hashes(url)
    # print(response)
    # print(request)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
