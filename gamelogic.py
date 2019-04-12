import json
import sys

jsonfile = "./tablero.json"
params = str(sys.argv[1]) + str(sys.argv[2])
player = str(sys.argv[3])

def findsquare(boxtocheck):
    print("boxtocheck " + boxtocheck)
    with open(jsonfile, "r") as jayson:
        data = json.load(jayson)
        for square in data["boxes"]:
            if square["cord"] == boxtocheck:
                print(square["cord"])
                square["player"] = player
                square["points"] += 1
                if square["points"] == square["max"]:
                    square["points"] = 0
                    with open(jsonfile, "w") as ndeah:
                        json.dump(data, ndeah, indent=4)
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
                    with open (jsonfile, "w") as ndeah:
                        json.dump(data, ndeah, indent=4)



if __name__ == "__main__":
    findsquare(params)