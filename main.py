from hashing import compare_hashes_path
from recursive import scrape
from utils import load_data, write_data

base = "http://www.ime.eb.mil.br"
domain = "ime.eb.mil.br"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    data = load_data()
    data = scrape(base, data, domain)
    data = compare_hashes(data)
    write_data(data)
