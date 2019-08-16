########################################
#------AI/FRONTEND MUST MAKE SURE------#
#----THE SQUARE ISN'T TAKEN ALREADY----#
########################################

from multiprocessing import Process
import json
import sys
import os

# jsonfile = "../Tableros/" + str(sys.argv[4]) + ".json"
# params = str(sys.argv[1]) + str(sys.argv[2])
# player = str(sys.argv[3])
  
def findsquare(boxtocheck, jsonfile, player):
    recursions = 0
    ## DUMPS JSON OBJECTS TO A PYTHON EDITABLE DICTIONARY
    toreturn = {}
    with open(jsonfile, "r") as jayson: 
        data = json.load(jayson) 
        ## LOOPS UNTILL IT FINDS THE DESIRED POSITION 
        for square in data["boxes"]:
            if square["cord"] == boxtocheck or square["id"] == boxtocheck:
                print (player)
                print (square["player"])
                ## CHCECKS IF TAKEN
                if square["player"] == player or square["player"] == 0:
                    ## MARKS POSITION AS TAKEN BY PLAYER
                    square["player"] = player
                    ## ADDS A POINT TO THE SQUARE
                    square["points"] += 1
                    ## CHECKS IF POINTS LIMIT IS REACHED
                    print(str("player " + str(square["player"]) + " cord " + str(square["cord"]) + " points " + str(square["points"])))
                    print(str("limx " + str(square["limx"]) + " limy " + str(square["limy"]) + " max " + str(square["max"])))
                    if square["points"] == square["max"]:
                        ## RESET THE SQUARE'S POINTS
                        square["points"] = 0
                        square["player"] = 0
                        ## DUMPS THE MODIFIED DICTIONARY TO THE JSON FILE
                        with open(jsonfile, "w") as ndeah:
                            json.dump(data, ndeah, indent=4)
                        ## TRIGGERS EXPANSION
                        recursions += 1
                        print ("expanding")
                        print (str(square["cordy"]) + ", " + str(square["cordy"] + 1) + ", " + str(square["cordy"] - 1))
                        print (str(square["cordx"]) + ", " + str(square["cordx"] + 1) + ", " + str(square["cordx"] - 1))
                        if square["limy"] == 2:
                            data = second(str(square["cordy"] + 1) + str(square["cordx"]), data, player)          
                            data = second(str(square["cordy"] - 1) + str(square["cordx"]), data, player)
                        else: 
                            data = second(str(square["cordy"] + square["limy"]) + str(square["cordx"]), data, player)
                        if square["limx"] == 2:
                            data = second(str(square["cordy"]) + str(square["cordx"] + 1), data, player)
                            data = second(str(square["cordy"]) + str(square["cordx"] - 1), data, player)
                        else: 
                            data = second(str(square["cordy"]) + str(square["cordx"] + square["limx"]), data, player)
                    print("done")
                    ## DUMPS THE MODIFIED DICTIONARY TO THE JSON FILE
                    with open (jsonfile, "w") as ndeah:
                        json.dump(data, ndeah, indent=4)
                        toreturn["obj"] = data
                        toreturn["cord"] = square["cord"]
                        return str(json.dumps(toreturn))
                else: 
                    toreturn["obj"] = "failed"
                    return str(json.dumps(toreturn))

def second(boxtocheck, data, player):
    for square in data["boxes"]:
        if square["cord"] == boxtocheck or square["id"] == boxtocheck:
            ## MARKS POSITION AS TAKEN BY PLAYER
            square["player"] = player
            ## ADDS A POINT TO THE SQUARE
            square["points"] += 1
            ## CHECKS IF POINTS LIMIT IS REACHED
            print("player " + str(square["player"]) + " cord " + str(square["cord"]) + " points " + str(square["points"]))
            print("limx " + str(square["limx"]) + " limy " + str(square["limy"]) + " max " + str(square["max"]))
            if square["points"] == square["max"]:
                ## RESET THE SQUARE'S POINTS
                square["points"] = 0
                square["player"] = 0
                ## TRIGGERS EXPANSION
                recursions +=1
                if recursions < 200:
                    print ("expanding")
                    print (str(square["cordy"]) + ", " + str(square["cordy"] + 1) + ", " + str(square["cordy"] - 1))
                    print (str(square["cordx"]) + ", " + str(square["cordx"] + 1) + ", " + str(square["cordx"] - 1))
                    if square["limy"] == 2:
                        data = second(str(square["cordy"] + 1) + str(square["cordx"]), data, player)          
                        data = second(str(square["cordy"] - 1) + str(square["cordx"]), data, player)
                    else: 
                        data = second(str(square["cordy"] + square["limy"]) + str(square["cordx"]), data, player)
                    if square["limx"] == 2:
                        data = second(str(square["cordy"]) + str(square["cordx"] + 1), data, player)
                        data = second(str(square["cordy"]) + str(square["cordx"] - 1), data, player)
                    else: 
                        data = second(str(square["cordy"]) + str(square["cordx"] + square["limx"]), data, player)
                else: 
                    print("recursive stopped")
            return data