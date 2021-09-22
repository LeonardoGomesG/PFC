from setup.config import recursive as config_recursive
from setup.config import signatures as config_signatures
from setup.config import data as config_data

from domain.detection.hashing import compare_hashes
from domain.recursive.scraping import recursive_get_urls_in_domain
from domain.utils import load_data, write_data
from domain.classification.classify import detect_signatures

base = config_recursive["base"]
domain = config_recursive["domain"]
signatures_path = config_signatures["path"]
data_path = config_data['path']
load_previous_data = config_data["load_previous_data"]

if __name__ == '__main__':
    urls = recursive_get_urls_in_domain(base, domain)
    data = load_data(urls, load_previous_data, data_path)
    data = compare_hashes(data)
    detect_signatures(data, signatures_path)
    write_data(data, data_path)
