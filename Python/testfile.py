import os
import json 

num = 1
found = False
while found == False:
        folder = os.path.abspath("../Tableros/")
        print (folder)
        bul = os.path.isdir(folder)
        print(folder, 'is there', bul)
        # tablero = os.path.join(folder, str(num) + ".json")
        # if os.path.isfile(tablero) == False:
        #         print(tablero)
        #         found = True
        #         print(folder, 'is there', os.path.isfolder(folder))
        # else: num += 1
        # print ("created " + tablero)
