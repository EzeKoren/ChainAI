from gamelogic import findsquare
from testfile import main as create
import json
import os

maxx = 5
maxy = 9

class game:
    def newGame (self):
        s = json.loads(create(self.boardnum))
        self.boardpath = s["file"]
        self.boardobj = json.loads(s["obj"])
        self.boardnum = s["num"]
        self.turn = 1        
    
    def loadData (self, board):
        self.boardnum = board
        self.boardpath = os.path.join(os.getcwd(), "Tableros", str(board) + ".json")
        self.boardobj = json.loads(open(self.boardpath, "r").read().replace('\n', ''))
        
    def makeMove (self, player, cordx, cordy):
        if self.turn == player:
            move = str(cordy) + str(cordx)
            self.boardobj = json.loads(findsquare(move, self.boardpath, player))["obj"]
            if player == 1: player = 2
            elif player == 2: player = 1
            
            return ("success")
        else: 
            return ("error")
    
    def getCurrentInfo (self, player): 
        self.state = [[0,0,0,0,0,0],
                      [0,0,0,0,0,0],
                      [0,0,0,0,0,0],
                      [0,0,0,0,0,0],
                      [0,0,0,0,0,0],
                      [0,0,0,0,0,0],
                      [0,0,0,0,0,0],
                      [0,0,0,0,0,0],
                      [0,0,0,0,0,0],
                      [0,0,0,0,0,0]]
        self.actions = []
        for square in self.boardobj["boxes"]:
            cordx = square["cordx"]
            cordy = square["cordy"]
            if square["player"] == player:
                self.state[cordx][cordy] = square["points"]
                self.actions.append([cordy, cordx])
            elif square["player"] != 0:
                self.state[cordx][cordy] = 0 - square["points"]
            else:
                self.actions.append([cordy, cordx])              
