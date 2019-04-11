import json
import sys

jsonfile = "./tablero.json"
boxtocheck = str(sys.argv[1]) + str(sys.argv[2])

def main():
    print("boxtocheck " + boxtocheck)
    with open(jsonfile, "r") as jayson:
        data = json.load(jayson)
        print(data)
        for v in data["boxes"]:
            print(v["cord"])
            if v["cord"] == boxtocheck:
                xd
            

if __name__ == "__main__":
    main()