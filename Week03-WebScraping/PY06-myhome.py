import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.myhome.ie/residential/mayo/property-for-sale?page=2")

soup = BeautifulSoup(page.content, 'html.parser')
print (soup.prettify())
