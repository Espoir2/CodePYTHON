import requests
from pprint import pprint
url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
# Voir le code html source
pprint(page.content)