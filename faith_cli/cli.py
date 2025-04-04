#Get the dependencies
import click
import requests
import json
from pathlib import Path

from cache import load_cache, save_cache
import scraper 

#Define the function to load the verses from the cache file
def load_cache():
    if CACHE_FILE.exists:
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return{}

#Function to get verses from the cache file
def get_cached_verses(topic):
    cache = load_cache()
    return cache.get(topic, None)
    
@click.command()


#Options: API.bible, 
@click.argument("emotion")

def display(emotion):
    #Load the verses from the json file
    verses = load_verses
    
    pass


        
if __name__ == "__main__":
    display()