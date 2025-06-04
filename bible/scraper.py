import requests
from bs4 import BeautifulSoup

topic = "adam"
url = f"https://www.openbible.info/topics/{topic}"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

print(soup)