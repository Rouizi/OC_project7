from flask import render_template, request, flash
from app import app
import json
from app.classes import GoogleMap, HistoryFromWiki, adress_found, adress_not_foud, relate, no_relate
import random

@app.route('/')
@app.route('/index')
def index():
    activate = True
    script = True
    key = app.config['GOOGLE_MAP_KEY']
    return render_template('index.html', key=key, activate=activate, script=script)

@app.route('/a_propos_de_moi')
def a_propos_de_moi():
    activate = False
    script = False
    key = app.config['GOOGLE_MAP_KEY']
    return render_template('a_propos_de_moi.html', key=key, activate=activate, script=script)
    
@app.route('/adress_lat_lng', methods=['POST'])
def adress_lat_lng():
    content =  request.form['content']
    google_map = GoogleMap(content)
    # results_google contain either formatted_address, lat, lng or None
    results_google = google_map.get_adress_lat_lng()
    nb = random.randrange(0, 5)
    if results_google is not None:
        # results[1] = latitude, results[2] = longitude
        history_from_wiki = HistoryFromWiki(results_google[1], results_google[2])
        adress = adress_found[nb] + results_google[0]
        results_wiki = history_from_wiki.get_history_url()
        if results_wiki is not None:
            history = relate[nb] + results_wiki[0]
            return json.dumps({'status': 'SUCCESS',
                               'adress': adress,
                               'lat': results_google[1],
                               'lng': results_google[2],
                               'history': history,
                               'url': results_wiki[1]})
        else:
            return json.dumps({'status': 'OK',
                               'adress': adress,
                               'lat': results_google[1],
                               'lng': results_google[2],
                               'history': no_relate[nb]})
    else:
        return json.dumps({'status': 'ZERO_RESULTS', 'adress': adress_not_foud[nb]})

