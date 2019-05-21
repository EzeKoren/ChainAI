import json
import os
import random
import numpy as np
from keras.models     import Sequential
from keras.layers     import Dense
from keras.optimizers import Adam

tablename = 1

def placecrap(px, py, pl, file):
    os.system("gamelogic.py " + px + " " + py + " " + pl + " " + file)

def build_model(input_size, output_size):
    model = Sequential()
    model.add(Dense(128, input_dim=input_size, activation='relu'))
    model.add(Dense(52, activation='relu'))
    model.add(Dense(output_size, activation='linear'))
    model.compile(loss='mse', optimizer=Adam())
    return model

def train_model(training_data):
    X = np.array([i[0] for i in training_data]).reshape(-1, len(training_data[0][0]))
    y = np.array([i[1] for i in training_data]).reshape(-1, len(training_data[0][1]))
    model = build_model(input_size=len(X[0]), output_size=len(y[0]))
    model.fit(X, y, epochs=10)
    return model



def main():
    

# def stats():
#     with open (jsonfile, "r") as dou:
#         board = json.load(dou)
#         fitness = 0
#         for square in board["boxes"]:
#             if square["player"] == "ai":
#                 v = square[""]

if __name__ == "__main__":
    main()
