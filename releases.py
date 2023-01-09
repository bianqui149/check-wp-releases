# Importar módulos
import requests
from bs4 import BeautifulSoup

url = "https://wordpress.org/news/category/releases/"

response = requests.get(url)

html = BeautifulSoup(response.text, 'html.parser')

quotes_html = html.find_all('div', class_="wp-block-wporg-release-version")

core_version = ''

if not quotes_html:
     core_version = 'No release yet'
else:
    core_version = quotes_html[0].get_text()

print(core_version)

