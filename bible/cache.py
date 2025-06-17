import json

def load_cache(file):
    verses = json.load(verses)
    return verses

def save_cache(verses):
    with open('verses.json','w') as f:
        json.dump(verses, f, indent=3)