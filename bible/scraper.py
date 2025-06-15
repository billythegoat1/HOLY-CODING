import requests
from bs4 import BeautifulSoup
import json

topic = "joy"
url = f"https://www.openbible.info/topics/{topic}"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

verse_divs = soup.find_all('div', class_='verse')

scraped_verses = []

#find.('a') is equivalent to div.a

for div in verse_divs:

    reference = div.a.text
    verse = div.p.text.strip()
    
    scraped_verses.append({"ref":reference,"verse":verse})
    
    
print(scraped_verses)




