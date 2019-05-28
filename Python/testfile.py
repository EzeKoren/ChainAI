import os
import json 

num = 1
found = False
while found == False:
        folder = os.getcwd()
        print(folder)
        tablero = os.path.join(folder, "Tableros", str(num) + ".json")
        print(folder)
        print(tablero)
        if os.path.isfile(tablero) == False:
                print(tablero)
                found = True
                print(folder, 'is there', os.path.isdir(folder))
                open(tablero, "w+")
        else: num += 1
        print ("created " + tablero)
