from flask import render_template, request, flash
from app import app
import json

@app.route('/')
@app.route('/index')
def index():
    flash('salut tout le monde')
    return render_template('index.html')
    
@app.route('/latlng', methods=['POST'])
def latlng():
    content =  request.form['content']
    return json.dumps({'status':'OK','content':content})

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

@app.route('/signUpUser1', methods=['POST'])
def signUpUser1():
    user =  request.form['username']
    password = request.form['password']
    return json.dumps({'status':'OK','user':user,'pass':password})