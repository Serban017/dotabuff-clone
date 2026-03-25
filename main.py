import requests
from pprint import pprint


response = requests.get("https://api.opendota.com/api/players/87278757/recentMatches")

match_data = response.json() 

for match in match_data: 
    
    if match["player_slot"] <= 4 and match["radiant_win"] == True:
        print(f"Match {match['match_id']} - WIN - Hero ID: {match['hero_id']} - KDA: {match['kills']}/{match['deaths']}/{match['assists']}")
    else:
        print(f"Match {match['match_id']} - LOSS - Hero ID: {match['hero_id']} - KDA: {match['kills']}/{match['deaths']}/{match['assists']}")