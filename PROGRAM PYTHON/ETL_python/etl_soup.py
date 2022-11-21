import requests
from bs4 import BeautifulSoup
url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Trouver les titres

titres = soup.find_all("a", class_="gem-c-document-list__item-title")

for title in titres:
    print("*"*10)
    print(title.string)
    print("*"*10)
    print()

descriptions_bs = soup.find_all("p", class_="gem-c-document-list__item-description")
descriptions = [desc.string for desc in descriptions_bs]