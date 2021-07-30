from hashing import compare_hashes
from scraping import recursive_get_urls_in_domain
from utils import load_data, write_data

# Create a .config file
base = "http://www.ime.eb.mil.br"
domain = "ime.eb.mil.br"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    urls = recursive_get_urls_in_domain(base, domain)
    data = load_data()
    data = {**urls, **data}
    data = compare_hashes(data)
    write_data(data)
