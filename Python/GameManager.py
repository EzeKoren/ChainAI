from gamelogic import findsquare
from testfile import main as create
import json
import os

class game:
    def newGame (self):
        self.done = False
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
        self.failed = False
        if str(self.turn) == str(player):
            s = json.loads(findsquare(cord, self.boardpath, player))["obj"]
            print (s)
            if s == 'failed': 
                self.failed = True
            else: 
                self.boardobj = s
                if self.turn == 1: self.turn = 2
                elif self.turn == 2: self.turn = 1
        else: 
            self.failed = True
    
    def getCurrentInfo (self, player): 
        foundp1 = False
        foundp2 = False
        self.actions = []
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
        self.score = 0
        for square in self.boardobj["boxes"]:
            cordx = square["cordx"]
            cordy = square["cordy"]
            if square["player"] == player:
                self.state[cordy][cordx] = square["points"]
                foundp1 = True
                self.score += 1
                self.actions.extend([square["cord"]])
            elif square["player"] != 0:
                self.state[cordy][cordx] = 0 - square["points"]
                foundp2 = True
                self.score -= 1            
            else:
                self.actions.extend([square["cord"]])              
                print("Pitu estuvo aqui")              
        if foundp1 == True and foundp2 == False:
            self.done = True
            self.score = 10000
        elif foundp2 == True and foundp1 == False:
            self.done = True
            self.score = -10000