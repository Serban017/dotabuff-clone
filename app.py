import requests
from heroes import get_hero_name
 
from flask import Flask

app = Flask(__name__)

hero_table = get_hero_name()

@app.route('/')
def home():
    return "Welcome to Dotabuff Clone!"

@app.route('/player/<player_id>')
def player(player_id):
    response = requests.get(f"https://api.opendota.com/api/players/{player_id}/recentMatches")
    recent_matches = response.json()
    first_match = recent_matches[0]
    return f"Match {first_match['match_id']} - WIN - Hero: {hero_table[first_match['hero_id']]} - KDA: {first_match['kills']}/{first_match['deaths']}/{first_match['assists']}"

if __name__ == '__main__':
    app.run(debug=True)