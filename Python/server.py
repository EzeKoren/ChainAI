from flask import Flask, request
from flask_cors import CORS
from gamelogic import findsquare
import json

app = Flask(__name__)

CORS(app)

@app.route('/input', methods=['POST'])

def manage_request():
    cord = request.form['cord']
    player = request.form['player']
    print("player: {0}, coord: {1}".format(player, cord))
    findsquare(cord, "../Tableros/default.json", player)
    #with open("Tableros/default.json", "r") as json_file:
    #    return json.dumps(json_file)
    return json.dumps("{'text':'hola'}")

app.run()