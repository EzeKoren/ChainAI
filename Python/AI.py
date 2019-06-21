import json
import os
import random
import numpy as np
from keras.models       import Sequential
from keras.layers       import Dense
from keras.optimizers   import Adam
from gamelogic          import findsquare as findsquare
from testfile import main as createfile
from createfile import main as reset

def preparedata(player, data):
    log = os.path.join(os.getcwd(), "aidata.py")
    if player == 2: 
        for i in data:
            i[0["boxes"]] = json.loads(i[0["boxes"]])
            for u in i[0["boxes"]]:
                if u["player"] == 1:
                    u["player"] = 2
                elif u["player"] == 2:
                    u["player"] = 1
    print(data)
    with open(log, "r") as j:
        arrei = list(j.read())
    arrei.append(data)
    with open(log, "w") as o:
        o.write(str(arrei))

def manageobjects():
    obj = createfile()
    declaremode(obj)

def declaremode(pyobj):
    model = Sequential()
    input = Dense(units=200,input_dim=len(pyobj), activation='relu', kernel_initializer='glorot_uniform')(model)
    outx = Dense(5,  activation='linear')(model)
    outy = Dense(9,  activation='linear')(model)
    model = model(inputs=input, outputs=[outx,outy])
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])