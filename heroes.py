import requests
import os
import json
from pprint import pprint

def get_hero_name():
    
    if os.path.exists("heroes_data.json"):
        with open("heroes_data.json", "r") as f:
            heroes_data = json.load(f)
    else:
        response = requests.get("https://api.opendota.com/api/heroes")
        heroes_data = response.json()
        with open("heroes_data.json", "w") as f:
            json.dump(heroes_data, f)


    hero_table = {}

    for hero in heroes_data:
        hero_table[hero['id']] = hero['localized_name']
        
    return hero_table
