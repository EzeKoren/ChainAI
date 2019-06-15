import json
import sys

maxx = 5
maxy = 9

example = {
    "cord" : "00",
    "id" : "c00",
    "cordx" : 0,
    "cordy" : 0,
    "points" : 0,
    "max" : 0,
    "limx" : 1,
    "limy" : 1,
    "player" : 0 
}


def main(jsonfile):
    reset(example, maxx, maxy, jsonfile)
    termine(jsonfile)

def reset(example, maxx, maxy, jsonfile):
    with open (jsonfile, "w") as out:
        out.truncate
        out.write("{\n\"boxes\":[\n")
    curx = 0
    cury = 0
    while cury <= maxy:
        while curx <= maxx: 
            example["max"] = 0  # Resetting max value
            example["cordx"] = curx
            example["cordy"] = cury
            example["cord"] = str(cury) + str(curx)
            example["id"] = "c" + example["cord"]
            example["player"] = 0
            if example["cordx"] == 0:
                example["limx"] = 1
                example["max"] += 1
            elif example["cordx"] == maxx:
                example["limx"] = -1
                example["max"] += 1
            else:
                example["limx"] = 2
                example["max"] += 2

            if example["cordy"] == 0:
                example["limy"] = 1
                example["max"] += 1
            elif example["cordy"] == maxy:
                example["limy"] = -1
                example["max"] += 1
            else:
                example["limy"] = 2
                example["max"] += 2
            example["tilexp"] = example["max"]
            toprint = json.dumps(example, indent=4)
            print(toprint)
            with open (jsonfile, "a") as out:
                json.dump(example, out, indent=4)
                if curx == maxx and cury == maxy:
                    return
                else:
                    out.write(",\n")    
            curx += 1
        cury += 1
        curx = 0

def termine(jsonfile):
    with open(jsonfile, "a") as out:
        out.write("\n]\n}")
    with open(jsonfile, "r") as out:
        datastore = json.load(out)
    with open(jsonfile, "w") as out:
        out.write(json.dumps(datastore, indent=4))
    print("termine")