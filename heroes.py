import requests
from pprint import pprint


def get_hero_name():
    
    response = requests.get("https://api.opendota.com/api/heroes")

    heroes_data = response.json()

    hero_table = {}

    for hero in heroes_data:
        hero_table[hero['id']] = hero['localized_name']
        
        
    return hero_table

get_hero_name()