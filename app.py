from flask import Flask, jsonify, request
import os, string
import sys
import requests


app = Flask(__name__)


#Functions--------------------------------------------------------






#Routes--------------------------------------------------------
@app.route("/") # @ sign wraps the code for the route
def hello_world():
    return "Welcome to the trial website"


@app.route("/word", methods=['GET'])
def word_reverse():
    word = requests.get('https://random-word-api.herokuapp.com/word?number=1')
    word = word.text
    lst = word.split()
    lst.reverse()
    mystr = ''+join(map(str,lst))
    r = word+" is changed to "+mystr
    return jsonify(r)

@app.route('/ping', methods=['GET'])
def ping_pong():
    r = 'pong!'
    return jsonify(r)

@app.route('/string-count', methods=[ 'POST'])
def predict():
    if request.method == 'POST':
        url = request.get_json()
        length = len(url)
    return jsonify(length)
