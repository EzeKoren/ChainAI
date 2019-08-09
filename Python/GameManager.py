from gamelogic import findsquare
from testfile import main as create
import json
import os

maxx = 5
maxy = 9

class game:
    def newGame (self):
        s = json.loads(create())
        self.boardpath = s["file"]
        self.boardobj = json.loads(s["obj"])
        self.boardnum = s["num"]
        self.turn = 1        
    
    def loadData (self, board):
        self.boardnum = board
        self.boardpath = os.path.join(os.getcwd(), "Tableros", str(board) + ".json")
        self.boardobj = json.loads(open(self.boardpath, "r").read().replace('\n', ''))
        
    def makeMove (self, player, cord):
        if str(self.turn) == player:
            self.boardobj = json.loads(findsquare(cord, self.boardpath, player))["obj"]
            if self.turn == 1: self.turn = 2
            elif self.turn == 2: self.turn = 1
            return (json.dumps(self.boardobj))
        else: 
            return ("failed")
    
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
