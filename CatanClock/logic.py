from flask import render_template, Blueprint, request, redirect, session, url_for
import json

bp = Blueprint('logic', __name__)


@bp.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        session['game_settings'] = {
            'players': int(request.form['player_count']),
            'time': int(request.form['time_per_player']),
            'increment': int(request.form.get('increment', 0)),
            'colors': json.loads(request.form['color_order'])
        }
        return redirect(url_for('logic.game'))

    if 'game_settings' not in session:
        session['game_settings'] = {
            'players': 4,
            'time': 1200,
            'increment': 0,
            'colors': ['rot', 'weiß', 'blau', 'gelb']
        }

    return render_template('settings.html',
                           players=session['game_settings']['players'],
                           time=session['game_settings']['time'],
                           increment=session['game_settings'].get('increment', 0),
                           colors=session['game_settings']['colors'])


@bp.route('/game', methods=['GET', 'POST'])
def game():
    return render_template('game.html',
                           players=session['game_settings']['players'],
                           time=session['game_settings']['time'],
                           increment=session['game_settings'].get('increment', 0),
                           colors=session['game_settings']['colors'])
