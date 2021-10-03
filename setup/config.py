# File used for configuration
recursive = {
    "base": "https://webscraper.io/test-sites/e-commerce/static",
    # "base": "http://www.sicca.ima.mg.gov.br/index.html",
    # "base": "https://www.bbc.com/news/technology-43812539",
    # 'base': 'https://cnmqualifica.cnm.org.br/conexoes-municipalistas/',
    # "domain": "webscraper.io/test-sites/e-commerce",,
    'domain': 'webscraper.io',
    "max_depth": 100
}

rerun_recursion = True

load_previous_data = True,

tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

signatures = {
    'path': './domain/classification/signatures.txt',
    'tesseract': r'C:\Program Files\Tesseract-OCR\tesseract.exe'
}

notification = {
    'from_email': 'asdmalizia@gmail.com',
    'password': 'kuhidkqxnauykqxq',
    # 'to_email': 'narcelio@outlook.com'
    'to_email': 'alessandramalizia@hotmail.com'
}
