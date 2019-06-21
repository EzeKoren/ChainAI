from flask import Flask, request, render_template
from flask_cors import CORS
from gamelogic import findsquare
from testfile import main as createfile
from AI import preparedata
import json
import os

app = Flask(__name__)

CORS(app)

@app.route('/create', methods=['POST'])

def manage_request1():
    jsonfile = createfile()
    return str(jsonfile)

@app.route('/input', methods=['POST'])

def manage_request2():
    cord = request.form['cord']
    tablero = os.path.join(os.getcwd(), "Tableros", request.form['file'] + ".json")
    player = request.form['player']
    fcode = findsquare(cord, tablero, player)
    return fcode

@app.route('/appenddata', methods=['POST'])

def manage_request3():
    player = request.form['player']
    print(player)
    data = request.form['data']
    print(data)
    preparedata(player, data)
    return("done")

app.run('0.0.0.0', port=80)