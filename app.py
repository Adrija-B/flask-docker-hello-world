from flask import Flask, jsonify, request, render_template, Response
import os, string
import requests
from flask import json
from werkzeug.exceptions import HTTPException
import logging # <-- added

app = Flask(__name__)

if __name__ == '__main__':
   app.run(debug = True)

#Functions--------------------------------------------------------

# Modification of https://flask.palletsprojects.com/en/2.1.x/errorhandling/#generic-exception-handlers
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    logging.exception(e) # <-- added
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

def reverse_words_order_and_swap_cases(sentence):
    words = sentence[::-1]
    return ''.join([word.upper() for word in words])


#Routes--------------------------------------------------------
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/ping', methods=['GET'])
def ping_pong():
    """Returns jsonify(string) as a simple output"""
    return jsonify('pong!')

@app.route('/word', methods=['GET'])
def word_reverse():
    """Gets a word and returns a JSON containing the original word and the transformed word"""
    word = requests.get('https://random-word-api.herokuapp.com/word?number=1')
    word = word.text.strip("[]\"")
    reversed_word = reverse_words_order_and_swap_cases(word)
    jsonStr = json.dumps({
            "Original Word Style": word,
            "New Word Style": reversed_word
            }, indent=2, sort_keys=False)
    return jsonStr

@app.route('/string-count', methods=[ 'POST'])
def string_length():
   """uses request.get to get the String and returns the length"""
   url = request.get_json()
   length = len(url)
   return jsonify(length)
