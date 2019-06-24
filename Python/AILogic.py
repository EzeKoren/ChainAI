import numpy as np
import json
import os
import time
from testfile import main as cf
from createfile import main as rst
from gamelogic import findsquare as po
class board():
    def __init__(self, player, idnum):
        if idnum == None:
            self.boardnum = os.path.join(os.getcwd(), "Tableros", str(json.loads(cf())["file"]) + ".json")
        else: 
            self.boardnum = os.path.join(os.getcwd(), "Tableros", str(idnum) + ".json")     
        self.init_board = np.zeros([2,10,6]).astype(str)
        self.init_board[self.init_board == "0.0"] = 0
        self.player = player
        self.current_board = self.init_board
        self.turncount = 0
        self.done = False
    
    def step(self, cord):
        time.sleep(0.05)
        cord = str(cord)
        self.action = cord
        obj = po(cord, self.boardnum, self.player)
        if obj != "failed":
            obj = json.loads(obj)
            obj = obj["obj"]
            self.turncount += 1
            self.thisscore = 0
            self.otherscore = 0
            for a in obj["boxes"]:
                if a["player"] == self.player:
                    self.current_board[0][a["cordy"]][a["cordx"]] = a["points"]
                else: self.current_board[1][a["cordy"]][a["cordx"]] = a["points"]                    
            # for a in obj["boxes"]:
            #     if a["player"] == 1:
            #         self.current_board[a["cordy"]][a["cordx"]][0] = 1
            #         self.thisscore += 1
            #         if a["points"] > 1:
            #             self.current_board[a["cordy"]][a["cordx"]][1] = 1
            #             self.thisscore += 1
            #             if a["points"] > 2:
            #                 self.current_board[a["cordy"]][a["cordx"]][2] = 1
            #                 self.thisscore += 1
            #     elif a["player"] == 2: 
            #         self.current_board[a["cordy"]][a["cordx"]][3] = 1
            #         self.thisscore += 1
            #         if a["points"] > 1:
            #             self.current_board[a["cordy"]][a["cordx"]][4] = 1
            #             self.thisscore += 1
            #             if a["points"] > 2:
            #                 self.current_board[a["cordy"]][a["cordx"]][5] = 1
            #                 self.thisscore += 1
            # if self.player == 1:
            #     self.player = 2
            #     self.current_board[:,:,6] = 0
            # elif self.player == 2: 
            #     self.player = 1
            #     self.current_board[:,:,6] = 1
            print(self.current_board)
            self.observation = self.current_board
            # self.check_winner()
            return self.observation, self.done, self.action
        else: return "Invalid move" 

    # def check_winner(self):
    #     if self.turncount > 2:
    #         if self.thisscore > 0 and self.otherscore > 0:
    #             self.done = False
    #         else: self.done = True
        
    def actions(self):
        acts = []
        for cordy in range(10):
            for cordx in range(6):
                if self.current_board[cordy][cordx] >= 0:
                    acts.append(int(str(cordx) + str(cordy)))
        return acts
    def reset(self):
        rst(self.boardnum)

