# from flask import Flask, request
# from flask_cors import CORS
# from gamelogic import findsquare as nut

# app = Flask(__name__)
# CORS(app)

# @app.route('../', methods=['POST'])
# def manage_request():
#     cord = request.form['cord']
#     player = request.form['player']
#     nut(cord, "Tableros/default.json", player)
#     return 0

# app.run()

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'