# File used for configuration

# For each base, there must be a domain
recursive = {
    "base": [
        "http://www.sicca.ima.mg.gov.br/index.html", 
        "https://cnmqualifica.cnm.org.br/conexoes-municipalistas/", 
        "https://webscraper.io/test-sites/e-commerce/static"
    ],
    "domain": [None, "org.br", "webscraper.io/test-sites/e-commerce"],
    "max_depth": None
}

max_threads = 10

rerun_recursion = True

load_previous_data = True,

notification = {
    'from_email': 'asdmalizia@gmail.com',
    'password': 'kuhidkqxnauykqxq',
    'to_email': 'leonardo.gomes.g95@gmail.com'
}
