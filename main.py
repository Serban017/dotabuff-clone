import requests
from heroes import get_hero_name
from match import get_match_details
from pprint import pprint

option = input("1. Look up a player's match history\n2. Analyze a match directly\n")

if option == "1": 

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

elif option == "2":

    hero_table = get_hero_name()

    match_id = input("Enter a match ID: ")
    match_details = get_match_details(match_id)


    print("--- RADIANT ---")
    for player in match_details['players']: 

        if player['player_slot'] <= 4: 
            print(f"Hero {hero_table[player['hero_id']]} - KDA: {player['kills']}/{player['deaths']}/{player['assists']}")

    print("--- DIRE ---")   
    for player in match_details['players']: 

        if player['player_slot'] >= 128: 
            print(f"Hero {hero_table[player['hero_id']]} - KDA: {player['kills']}/{player['deaths']}/{player['assists']}")
else:

    print("That's not an option bro")
