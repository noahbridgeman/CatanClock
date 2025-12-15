from flask import render_template, Blueprint, request, redirect, session
import json

bp = Blueprint('logic', __name__)

@bp.route('/settings', methods=['GET', 'POST'])
def settings():
    session['game_settings'] = {
        'players': 3,
        'time': 10,
        'colors': ['rot', 'weiß', 'blau', 'gelb']
    }


    return render_template('settings.html',
                           players=session['game_settings']['players'],
                           time=session['game_settings']['time'],
                           colors=session['game_settings']['colors'])


@bp.route('/start_game', methods=['POST'])
def start_game():
    player_count = int(request.form['player_count'])
    time_per_player = int(request.form['time_per_player'])
    color_order = json.loads(request.form['color_order'])

    # Speichern in Session oder DB
    session['game_settings'] = {
        'players': player_count,
        'time': time_per_player,
        'colors': color_order
    }

    return redirect('/game')

@bp.route('/game', methods=['GET', 'POST'])
def game():
    return render_template('game.html',
                           players=session['game_settings']['players'],
                           time=session['game_settings']['time'],
                           colors=session['game_settings']['colors'])