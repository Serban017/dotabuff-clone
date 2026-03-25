import requests
import os 
import json
from pprint import pprint


def get_match_details(match_id):
    
    if os.path.exists(f"match_details{match_id}.json"):
        with open (f"match_details{match_id}.json", "r") as f:
            match_data = json.load(f)
    else:
        response = requests.get(f"https://api.opendota.com/api/matches/{match_id}")
        match_data = response.json()
        with open(f"match_details{match_id}.json", "w") as f:
            json.dump(match_data, f)

    return match_data

