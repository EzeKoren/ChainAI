########################################
#------AI/FRONTEND MUST MAKE SURE------#
#----THE SQUARE ISN'T TAKEN ALREADY----#
########################################

import json
import sys

jsonfile = "../tablero.json"
params = str(sys.argv[1]) + str(sys.argv[2])
player = str(sys.argv[3])
  
def findsquare(boxtocheck):
    ## DUMPS JSON OBJECTS TO A PYTHON EDITABLE DICTIONARY
    with open(jsonfile, "r") as jayson: 
        data = json.load(jayson) 
        ## LOOPS UNTILL IT FINDS THE DESIRED POSITION 
        for square in data["boxes"]:
            if square["cord"] == boxtocheck:
                ## MARKS POSITION AS TAKEN BY PLAYER
                square["player"] = player
                ## ADDS A POINT TO THE SQUARE
                square["points"] += 1
                ## CHECKS IF POINTS LIMIT IS REACHED
                if square["points"] == square["max"]:
                    ## RESET THE SQUARE'S POINTS
                    square["points"] = 0
                    ## DUMPS THE MODIFIED DICTIONARY TO THE JSON FILE
                    with open(jsonfile, "w") as ndeah:
                        json.dump(data, ndeah, indent=4)
                    ## TRIGGERS EXPANSION
                    print ("expanding")
                    if square["cordx"] == 2:
                        findsquare(str(square["cordx"] + 1) + str(square["cordy"]))
                        findsquare(str(square["cordx"] - 1) + str(square["cordy"]))
                    else: 
                        findsquare(str(square["cordx"] + square["limx"]) + str(square["cordy"]))
                    if square["cordy"] == 2:
                        findsquare(str(square["cordx"]) + str(square["cordy"] + 1))
                        findsquare(str(square["cordx"]) + str(square["cordy"] - 1))
                    else: 
                        findsquare(str(square["cordx"]) + str(square["cordy"] + square["limy"]))
                else:
                    ## DUMPS THE MODIFIED DICTIONARY TO THE JSON FILE
                    with open (jsonfile, "w") as ndeah:
                        json.dump(data, ndeah, indent=4)



if __name__ == "__main__":
    findsquare(params)