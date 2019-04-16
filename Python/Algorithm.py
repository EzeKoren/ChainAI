fitness = 0
jsonfile = "../tablero.json"
def GetFitness():
    with open (jsonfile, "r") as out:
        data = json.load(out)
        