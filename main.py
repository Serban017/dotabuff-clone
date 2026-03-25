import requests
from heroes import get_hero_name
from pprint import pprint


player_id = input("Enter player ID: ")

response = requests.get(f"https://api.opendota.com/api/players/{player_id}/recentMatches")

match_data = response.json() 

hero_table = get_hero_name()

for match in match_data: 
    
    if match["player_slot"] <= 4 and match["radiant_win"] == True:
        print(f"Match {match['match_id']} - WIN - Hero: {hero_table[match['hero_id']]} - KDA: {match['kills']}/{match['deaths']}/{match['assists']}")
    elif match["player_slot"] >= 128 and match["radiant_win"] == False:
        print(f"Match {match['match_id']} - WIN - Hero: {hero_table[match['hero_id']]} - KDA: {match['kills']}/{match['deaths']}/{match['assists']}")
    else:
        print(f"Match {match['match_id']} - LOSE - Hero: {hero_table[match['hero_id']]} - KDA: {match['kills']}/{match['deaths']}/{match['assists']}")