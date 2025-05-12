import json
from pathlib import Path


#creating a hidden (.) cache folder and file in the user's home directory
CACHE_DIR = Path.home() / ".faith_cli"
CACHE_FILE = CACHE_DIR / "cache.json"

#check if the directory exists and if not create it
CACHE_DIR.mkdir(exist_ok=True)

def load_cache():
    if CACHE_FILE.exists():
        
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    #if it doesn't return an empty dictionary
    return {}

def save_cache(cache_data):
    #write the cached data to the file
        with open(CACHE_FILE, "w") as f:
            json.dump(cache_data, f)
            
if __name__ == "__main__":
    
    #load the data
    cache = load_cache()
    #write to the loaded data
    cache["joy"] = {"reference": "Psalm 23:1", "text": "The lord is my shepherd, i shall not want"}
    #write to the file
    save_cache(cache);
    
    print("cache saved!")