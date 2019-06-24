import numpy as np
import json
import os
from testfile import main as cf
from gamelogic import findsquare as po
class board():
    def __init__(self):
        self.boardnum = os.path.join(os.getcwd(), "Tableros", str(json.loads(cf())["file"]) + ".json")
        self.init_board = np.zeros([10,6,7]).astype(str)
        self.init_board[self.init_board == "0.0"] = "0"
        self.player = 1
        self.current_board = self.init_board
        self.turncount = 0
        self.current_board[:,:,6] = 1
    
    def drop_piece(self, cord):
        cord = str(cord)
        obj = json.loads(str(po(cord, self.boardnum, self.player)))["obj"]
        if obj != "failed":
            self.turncount += 1
            self.thisscore = 0
            self.otherscore = 0
            for a in obj["boxes"]:
                if a["player"] == 1:
                    self.current_board[a["cordy"]][a["cordx"]][0] = 1
                    self.thisscore += 1
                    if a["points"] > 1:
                        self.current_board[a["cordy"]][a["cordx"]][1] = 1
                        self.thisscore += 1
                        if a["points"] > 2:
                            self.current_board[a["cordy"]][a["cordx"]][2] = 1
                            self.thisscore += 1
                elif a["player"] == 2: 
                    self.current_board[a["cordy"]][a["cordx"]][3] = 1
                    self.thisscore += 1
                    if a["points"] > 1:
                        self.current_board[a["cordy"]][a["cordx"]][4] = 1
                        self.thisscore += 1
                        if a["points"] > 2:
                            self.current_board[a["cordy"]][a["cordx"]][5] = 1
                            self.thisscore += 1
            if self.player == 1:
                self.player = 2
                self.current_board[:,:,6] = 0
            elif self.player == 2: 
                self.player = 1
                self.current_board[:,:,6] = 1
        else: return("Invalid move") 

    def check_winner(self):
        if self.turncount >= 2:
            if self.thisscore > 0 and self.otherscore > 0:
                return(False)
            else: return(True)
        
    def actions(self):
        acts = []
        for cordy in range(10):
            for cordx in range(6):
                if self.current_board[cordy][cordx] >= 0:
                    acts.append(int(str(cordx) + str(cordy)))
        return(acts)

