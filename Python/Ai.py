from AILogic import board
import random
import json
from testfile import main as cf
import createfile
import numpy as np
# nut
def aimanager():
    tablero = json.loads(cf())["file"]
    envp1 = board(1, tablero)
    envp2 = board(2, tablero)
    turn = 1
    
def preparedata(player, data):
    current_board = np.zeros([2,10,6]).astype(str)
    data = json.loads(data)
    for i in data:
        for a in i[0["boxes"]]:
            if a["player"] == player:
                current_board[0][a["cordy"]][a["cordx"]] = a["points"]
            else: current_board[1][a["cordy"]][a["cordx"]] = a["points"]
            
            

        
def model_data_preparation():
    training_data = []
    accepted_scores = []
    for game_index in range(intial_games):
        score = 0
        game_memory = []
        previous_observation = []
        for step_index in range(goal_steps):
            action = random.randrange(0, 2)
            observation, reward, done, info = env.step(action)
            
            if len(previous_observation) > 0:
                game_memory.append([previous_observation, action])
                
            previous_observation = observation
            score += reward
            if done:
                break
            
        if score >= score_requirement:
            accepted_scores.append(score)
            for data in game_memory:
                if data[1] == 1:
                    output = [0, 1]
                elif data[1] == 0:
                    output = [1, 0]
                training_data.append([data[0], output])
        
        env.reset()

    print(accepted_scores)
    
    return training_data
