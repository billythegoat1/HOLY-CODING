import requests
from bs4 import BeautifulSoup

topic = "joy"

url = f"https://www.openbible.info/topics/{topic}"
try:
    #setting a timeout of 10 seconds
    response = requests.get(url, timeout=10)
    #Raises an error for responses like 404,500
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error fetching the data: {e}")
    exit()
    
soup = BeautifulSoup(response.text, 'html.parser')

verses = soup.find_all('div', class_='verse')
#Creating a table to hold the verses
Scraped_verses = []
try:
        
        for verse in verses:
            reference = verse.a.get_text(strip=True) if verse else "No reference was found."
            text = verse.p.get_text(" ", strip=True) if verse else "No verse was found."
            
            Scraped_verses.append({"reference": reference, "text": text})
            
            print(f"{reference}\n{text}\n{'___'*50}")
       
except Exception as e:
        print(f"Error: {e}")
    
print(f"Successfully scrapped {len(Scraped_verses)} verses \n \n ")
