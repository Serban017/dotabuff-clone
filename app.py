import requests
from heroes import get_hero_name
 
from flask import Flask, render_template, request, redirect


app = Flask(__name__)

hero_table = get_hero_name()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/player')
def player_search():
    player_id = request.args.get('player_id')
    return redirect(f'/player/{player_id}')

@app.route('/player/<player_id>')
def player(player_id):
    response = requests.get(f"https://api.opendota.com/api/players/{player_id}/recentMatches")
    recent_matches = response.json()
   
    for match in recent_matches:
        if match['player_slot'] <= 4 and match['radiant_win'] == True:
            match['result'] = 'WIN'
        elif match['player_slot'] >= 128 and match['radiant_win'] == False:
            match['result'] = 'WIN'
        else:
            match['result'] = 'LOSS'
    return render_template('player.html', matches=recent_matches, hero_table=hero_table)

if __name__ == '__main__':
    app.run(debug=True)