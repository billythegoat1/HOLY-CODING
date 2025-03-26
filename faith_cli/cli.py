import click
import requests
import json
from pathlib import Path


def load_verses():
    verses_Path = Path(__file__).parent / "verses.json"
    with open(verses_Path, "r") as f:
        return json.load(f)
    
@click.command()
#I opt to use APIs to get verses and hence the cli app will have to have access to internet.
#Learn how to use API in python.

#Options: API.bible, 
@click.argument("emotion")

def display(emotion):
    #Load the verses from the json file
    verses = load_verses
    
    pass


        
if __name__ == "__main__":
    display()