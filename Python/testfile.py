import os
import json
from createfile import main as populatefile

def main():
        num = 1
        found = False
        while found == False:
                folder = os.getcwd()
                if os.path.isdir(os.path.join(folder, "Tableros")) == False:
                        os.mkdir(os.path.join(folder, "Tableros"))
                tablero = os.path.join(folder, "Tableros", str(num) + ".json")
                if os.path.isfile(tablero) == False:
                        print(tablero)
                        found = True
                        open(tablero, "w+")
                        populatefile(tablero)
                        obj = open(tablero, "r").read().replace('\n', '')
                else: num += 1
        print ("created " + tablero)
        toreturn = {}
        toreturn["file"] = num
        toreturn["obj"] = obj
        return json.dumps(toreturn)

