from flask import Flask, request
from flask_cors import CORS
from gamelogic import findsquare as nut

app = Flask(__name__)
CORS(app)

@app.route('/chainai', methods=['POST'])
def manage_request():
    cord = request.form['cord']
    player = request.form['player']
    nut(cord, "Tableros/default.json", player)
    return 0

app.run()

