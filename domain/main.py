from domain.hashing import compare_hashes
from domain.scraping import recursive_get_urls_in_domain
from domain.utils import load_data, write_data
from setup.config import recursive as config_recursive


base = config_recursive["base"]
domain = config_recursive["domain"]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    urls = recursive_get_urls_in_domain(base, domain)
    data = load_data(urls)
    data = compare_hashes(data)
    write_data(data)
