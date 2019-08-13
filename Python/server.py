from flask import Flask, request, render_template
from flask_cors import CORS
from GameManager import game
import json
import os

app = Flask(__name__)

player1data = []
player2data = []

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
    player = int(request.form['player'])
    if current.makeMove(player, cord) == "failed":
        return "failed"
    else:
        fcode = json.dumps(current.boardobj)
        appenddata(player, cord)
        return fcode

def appenddata(player, cord):
    current.getCurrentInfo(player)
    if player == 1:
        player1data.append([current.state, int(cord.replace('c', ''))])
        if current.done == True:
            with open("trainingData", "r") as v:
                data = v.read
            data.append([player1data])
            with open("trainingData", "w") as v:
                v.write(data)
    else:
        player2data.append([current.state, int(cord.replace('c', ''))])
        if current.done == True:
            with open("trainingData", "r") as v:
                data = v.read
            data.append([player2data])
            with open("trainingData", "w") as v:
                v.write(data)   
# @app.route('/appenddata', methods=['POST'])

# def manage_request3():
#     player = request.form['player']
#     print(player)
#     data = request.form['data']
#     preparedata(player, data)
#     return "done"

app.run(host='0.0.0.0') 
