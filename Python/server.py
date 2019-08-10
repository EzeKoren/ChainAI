from flask import Flask, request, render_template
from flask_cors import CORS
from GameManager import game
import json
import os

app = Flask(__name__)



CORS(app)
current = game()
@app.route('/create', methods=['POST'])

def manage_request1():
    current.newGame()
    jsonfile = json.dumps(current.boardobj)
    return str(jsonfile)

@app.route('/input', methods=['POST'])

def manage_request2():
    cord = request.form['cord']
    player = request.form['player']
    current.makeMove(player, cord)
    fcode = json.dumps(current.boardobj)
    return fcode

# @app.route('/appenddata', methods=['POST'])

# def manage_request3():
#     player = request.form['player']
#     print(player)
#     data = request.form['data']
#     preparedata(player, data)
#     return "done"

app.run(host='0.0.0.0') 
