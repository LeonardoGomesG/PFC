# File used for configuration
recursive = {
    # "base": "https://webscraper.io/test-sites/e-commerce/static",
    # "base": "http://www.sicca.ima.mg.gov.br/index.html",
    "base": "https://www.bbc.com/news/technology-43812539",
    "domain": ".com",
    "max_depth": 20
}

data = {
    "load_previous_data": True,
    'path': './domain/data.json'
}

signatures = {
    'path': './domain/classification/signatures.txt'
}
