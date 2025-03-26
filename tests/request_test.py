import requests
from bs4 import BeautifulSoup

url = "https://www.openbible.info/topics/fear"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

verses = soup.find_all('div', class_='verse')

for verse in verses:
    verse_ref = verse.a
    verse_text = verse.p
    print(verse_ref.text)
    print(verse_text.text)
