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
    if current.done == True:
        return "won"
    else:
        current.makeMove(player, cord)
        if current.failed == True:
            return "failed"
        else:
            fcode = json.dumps(current.boardobj)
            appenddata(player, cord)
            return fcode

def appenddata(player, cord):
    current.getCurrentInfo(player)
    if player == 1:
        player1data.extend([current.state, cord])
        if current.done == True:
            with open(os.path.join(os.getcwd(), "data"), "r") as v:
                data = v.read()
                data = data.split("][")
            data.extend([player1data])
            with open(os.path.join(os.getcwd(), "data"), "w") as v:
                v.write(str(data))
    else:
        player2data.extend([current.state, cord])
        if current.done == True:
            with open(os.path.join(os.getcwd(), "data"), "r") as v:
                data = v.read()
                data = data.split("][")
            data.append([player2data])
            with open(os.path.join(os.getcwd(), "data"), "w") as v:
                v.write(str(data))   

app.run(host='0.0.0.0', port='4839') 
