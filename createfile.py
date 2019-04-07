import json
maxx = 6
maxy = 10

jsonfile = './sample.json'

example = {
    "cordx" : 0,
    "cordy" : 0,
    "limx" : 1,
    "limy" : 1,
    "player" : 0 
}


def main():
    reset(example, maxx, maxy)


def reset(example, maxx, maxy):
    curx = 0
    cury = 0
    while cury <= maxy:
        while curx <= maxx:
            example["cordx"] = curx
            example["cordy"] = cury
            example["player"] = 0
            if example["cordx"] == 0:
                example["limx"] = 1
            else: 
                if example["cordx"] == maxx:
                    example["limx"] = -1
                else:
                    example["limx"] = 2
            if example["cordy"] == 0:
                example["limy"] = 1
            else: 
                if example["cordy"] == maxy:
                    example["limy"] = -1
                else:
                    example["limy"] = 2
            toprint = json.dumps(example, indent=4)
            print(toprint)
# TODO: Send to sample.json 
            curx += 1
        cury += 1
        curx = 0



if __name__ == "__main__":
    main()