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
    log = os.path.join(os.getcwd(), "ai.data")
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
# tablero = createfile()
# goal_steps = 10
# intial_games = 10000

# def model_data_preparation_1():
#     player = 1
#     training_data = []
#     accepted_scores = []
#     for game_index in range(intial_games):
#         score = 0
#         game_memory = []
#         previous_observation = []
#         for step_index in range(goal_steps):
#             actionx = random.randrange(0, 6)
#             actiony = random.randrange(0, 10)
#             action = str(actionx) + str (actiony)
#             findsquare(action, tablero, player)
#             with open(tablero, "r") as jayson: 
#                 observation = json.load(jayson) 
#             if len(previous_observation) > 0:
#                 game_memory.append([previous_observation, action])
#             reward = 0
#             done = True
#             found1 = False
#             found2 = False
#             for square in observation["boxes"]:
#                 if square["player"] == player:
#                      found1 = True
#                      reward += 1
#                      if square["cordx"] or square["cordy"] == 0 or square["cordx"] == 5 or square["cordy"] == 9:
#                         reward += 1
#                         if square["cordx"] and square["cordy"] == 0 or square["cordx"] == 5 and square["cordy"] == 9:
#                                 reward += 1


#                 elif square["player"] != 0:
#                      found2 = True
#                      reward -= 1
#                      if square["cordx"] or square["cordy"] == 0 or square["cordx"] == 5 or square["cordy"] == 9:
#                         reward -= 1
#                         if square["cordx"] and square["cordy"] == 0 or square["cordx"] == 5 and square["cordy"] == 9:
#                                 reward -= 1
#             if found1 and found2 == True: done = False
#             previous_observation = observation
#             score += reward
#             if done:
#                 break
          
#         if score > 0:
#             accepted_scores.append(score)
#             for data in game_memory:
#                 if data[1] == 1:
#                     output = [0, 1]
#                 elif data[1] == 0:
#                     output = [1, 0]
#                 training_data.append([data[0], output])
#         reset(tablero)

#     print(accepted_scores)
  
#     return training_data

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
