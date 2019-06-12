########################################
#------AI/FRONTEND MUST MAKE SURE------#
#----THE SQUARE ISN'T TAKEN ALREADY----#
########################################

import json
import sys
import os
import time

# jsonfile = "../Tableros/" + str(sys.argv[4]) + ".json"
# params = str(sys.argv[1]) + str(sys.argv[2])
# player = str(sys.argv[3])
  
def findsquare(boxtocheck, jsonfile, player, prevanim, animnum):
    anim = {}
    animnum += 1
    ## DUMPS JSON OBJECTS TO A PYTHON EDITABLE DICTIONARY
    with open(jsonfile, "r") as jayson: 
        data = json.load(jayson) 
        ## LOOPS UNTILL IT FINDS THE DESIRED POSITION 
        for square in data["boxes"]:
            if square["cord"] == boxtocheck:
                animnum += 1
                anim["cord"] = "\#" + boxtocheck
                ## MARKS POSITION AS TAKEN BY PLAYER
                ## time.sleep(.5)
                square["player"] = player
                anim["player"] = player
                ## ADDS A POINT TO THE SQUARE
                square["points"] += 1
                anim["points"] = square["points"]
                ## CHECKS IF POINTS LIMIT IS REACHED
                if square["points"] == square["max"]:
                    ## RESET THE SQUARE'S POINTS
                    square["points"] = 0
                    square["player"] = 0
                    anim["points"] = 0
                    anim["player"] = 0
                    prevanim[animnum] = anim
                    ## DUMPS THE MODIFIED DICTIONARY TO THE JSON FILE
                    with open(jsonfile, "w") as ndeah:
                        json.dump(data, ndeah, indent=4)
                    ## TRIGGERS EXPANSION
                    print ("expanding")
                    if square["cordx"] == 2:
                        findsquare(str(square["cordx"] + 1) + str(square["cordy"]), jsonfile, player)
                        findsquare(str(square["cordx"] - 1) + str(square["cordy"]), jsonfile, player)
                    else: 
                        findsquare(str(square["cordx"] + square["limx"]) + str(square["cordy"]), jsonfile, player)
                    if square["cordy"] == 2:
                        findsquare(str(square["cordx"]) + str(square["cordy"] + 1), jsonfile, player)
                        findsquare(str(square["cordx"]) + str(square["cordy"] - 1), jsonfile, player)
                    else: 
                        findsquare(str(square["cordx"]) + str(square["cordy"] + square["limy"]), jsonfile, player)
                else:
                    ## DUMPS THE MODIFIED DICTIONARY TO THE JSON FILE
                    with open (jsonfile, "w") as ndeah:
                        json.dump(data, ndeah, indent=4)
                    prevanim[animnum] = anim

