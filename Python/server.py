from flask import Flask, request
from flask_cors import CORS
from gamelogic import findsquare
from testfile import main as createfile
import json
import os

app = Flask(__name__)

CORS(app)

@app.route('/create', methods=['POST'])

def manage_request1():
    jsonfile = createfile()
    print (jsonfile)
    return jsonfile

@app.route('/input', methods=['POST'])

def manage_request2():
    cord = request.form['cord']
    print (cord)
    tablero = os.path.join(os.getcwd(), "Tableros", request.form['file'] + ".json")
    print (tablero)
    player = request.form['player']
    print (player)
    fcode = findsquare(cord, tablero, player)
    if fcode == "success":
        with open(tablero, "r") as json_file:
            data = json.load(json_file)
            return json.dumps(data)
    elif fcode == "failed": return "failed"

app.run()