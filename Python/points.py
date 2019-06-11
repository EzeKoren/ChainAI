import json

def count(observation, player):
    found1 = False
    found2 = False
    for square in observation["boxes"]:
        if square["player"] == player:
             found1 = True
             reward += 1
             if square["cordx"] or square["cordy"] == 0 or square["cordx"] == 5 or square["cordy"] == 9:
                reward += 1
                if square["cordx"] and square["cordy"] == 0 or square["cordx"] == 5 and square["cordy"] == 9:
                        reward += 1
        elif square["player"] != 0:
             found2 = True
             reward -= 1
             if square["cordx"] or square["cordy"] == 0 or square["cordx"] == 5 or square["cordy"] == 9:
                reward -= 1
                if square["cordx"] and square["cordy"] == 0 or square["cordx"] == 5 and square["cordy"] == 9:
                        reward -= 1
    if found1 == False: return "lost" 
    elif found2 == False: return "won" 
    else: return reward