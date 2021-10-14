# File used for configuration


# For each base, there must be a domain
recursive = {
    # "base": "https://webscraper.io/test-sites/e-commerce/static",
    "base": ["http://www.sicca.ima.mg.gov.br/index.html", 'https://cnmqualifica.cnm.org.br/conexoes-municipalistas/', "http://www.comp.ime.eb.br/graduacao_teste/"],
    # "base": "https://www.bbc.com/news/technology-43812539",
    # 'base': 'https://cnmqualifica.cnm.org.br/conexoes-municipalistas/',
    # "domain": "webscraper.io/test-sites/e-commerce",,
    'domain': ["gov.br", "cnmqualifica.cnm.org.br", "ime.eb.br/graduacao_teste"],
    "max_depth": None
}

max_threads = 10

rerun_recursion = True

load_previous_data = True,

tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

signatures = {
    'path': './domain/classification/signatures.txt',
    'tesseract': r'C:\Program Files\Tesseract-OCR\tesseract.exe'
}

notification = {
    'from_email': 'asdmalizia@gmail.com',
    'password': 'kuhidkqxnauykqxq', #alessandra
    # 'password': 'zrtohmwiiycrwzbp',  #leonardo

    # 'to_email': 'narcelio@outlook.com'
    # 'to_email': 'alessandramalizia@hotmail.com'
    'to_email': 'leonardo.gomes.g95@gmail.com'
}
