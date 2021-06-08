#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify, request
from flask import redirect, url_for
import flask_login
from random import *
import requests
import os
from backend.schema.User import User, users
from backend.library.auth import login_manager

load_dotenv()

app = Flask(__name__, static_folder="../dist/static", template_folder="../dist")
app.secret_key = os.getenv('APP_SESSION_SECRET_KEY', "THIS_IS_A_TEMP_KEY")
login_manager.init_app(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''

    email = request.form['email']
    if request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return redirect(url_for('protected'))

    return 'Bad login'


@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
@flask_login.login_required
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")

@app.route('/api/random')
@flask_login.login_required
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)