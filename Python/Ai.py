import GameManager 
import random
import numpy as np
from keras.models     import Sequential
from keras.layers     import Dense
from keras.optimizers import Adam

game = gameManager()

class init():
    def startgame():
        game.newGame()
    def loop():
        turn = game.turn
        if game.done == True:
            init().startgame()
        
class player1():
    def getinfo():
        game.getCurrentInfo(1)
        state = game.state
        score = game.score
        possibleActions = game.actions
    
