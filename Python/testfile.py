import os
import json
from createfile import main as populatefile

def main():
        num = 1
        found = False
        while found == False:
                if os.path.isdir(os.path.join(os.getcwd(), "Tableros")) == False:
                        os.mkdir(os.path.join(os.getcwd(), "Tableros"))
                tablero = os.path.join(os.getcwd(), "Tableros", str(num) + ".json")
                if os.path.isfile(tablero) == False:
                        found = True
                        open(tablero, "w+")
                        populatefile(tablero)
                        obj = open(tablero, "r").read().replace('\n', '')
                else: num += 1
        toreturn = {}
        toreturn["file"] = tablero
        toreturn["num"] = num
        toreturn["obj"] = obj
        return json.dumps(toreturn)

