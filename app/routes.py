from flask import render_template, request, flash
from app import app
import json
from app.classes import GoogleMap, HistoryFromWiki, adress_found, adress_no, relate
import random

@app.route('/')
@app.route('/index')
def index():
    flash("Besoin d'une adresse ? GrandPy Bot est là pour vous ! "
          "On dit même qu'il a toujours une petite histoire à raconter ...")
    return render_template('index.html')
    
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
        results_wiki = history_from_wiki.get_history_url()
        history = relate[nb] + results_wiki[0]
        adress = adress_found[nb] + results_google[0]
        # I set ensure_ascii to False to be able to display special characters
        return json.dumps({'status': 'OK',
                           'adress': adress,
                           'lat': results_google[1],
                           'lng': results_google[2],
                           'history': history,
                           'url': results_wiki[1]}, ensure_ascii=False)
    else:
        return json.dumps({'status': 'ZERO_RESULTS', 'adress': adress_no[nb]})


@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

@app.route('/signUpUser1', methods=['POST'])
def signUpUser1():
    user =  request.form['username']
    password = request.form['password']
    return json.dumps({'status':'OK','user':user,'pass':password})