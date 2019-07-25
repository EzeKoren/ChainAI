import numpy as np
import json 

class board:
    def __init__(self, board):
        self.player1 = [[0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0]]
        self.player2 = [[0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0]]
        self.dict = open (board, "r")
        for i in dict["boxes"]:
            if i["player"] == 1: 
                self.player1[i["cordx"["cordy"]]] = i["points"]
                self.player2[i["cordx"["cordy"]]] = -1
            elif i["player"] == 2: 
                self.player2[i["cordx"["cordy"]]] = i["points"]
                self.player1[i["cordx"["cordy"]]] = -1
            else:
                self.player2[i["cordx"["cordy"]]] = 0
                self.player1[i["cordx"["cordy"]]] = 0
