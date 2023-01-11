# AoC 2022, Day 14: Not Tetris! // Part 1
from ast import literal_eval

f = open("14_data.txt","r")
lines = f.readlines()
stratae = []

def renderwall(wall):
    for i in wall:
        for j in i:
            print(j, end="")
        print()
    print()

def reorder(left, right):
    if left > right:
        return right, left
    else:
        return left, right

def drawrocks(startx, starty, endx, endy, thewall):
    startx, endx = reorder(startx, endx)
    starty, endy = reorder(starty, endy)
    lenx, leny = endx-startx, endy-starty
    #print(f"{startx} {endx} lenx: {lenx} | {starty} {endx} leny: {leny}")
    if lenx == 0 and leny == 0:
        thewall[starty][startx] = "#"
    elif lenx == 0:
        for y in range(starty, endy + 1):
            #print("lenx == 0 |", y, startx)
            thewall[y][startx] = "#"
    elif leny == 0:
        for x in range(startx, endx + 1):
            #print("leny == 0 |", x, starty)
            thewall[starty][x] = "#"
    else:
        for y in range(starty, endy + 1):
            for x in range(startx, endx):
                thewall[y][x] = "#"

# Figure out the size of the cave wall by finding the larger x and y value in the set
x = []
y = []
for line in lines:
    line = line.removesuffix("\n")
    line = line.split(" -> ")
    stratae.append(line)
    for pair in line:
        pair = pair.split(",")
        y.append(int(pair[0]))
        x.append(int(pair[1]))
minx, maxx = min(x), max(x)
miny, maxy = min(y), max(y)
if minx > 0: minx = 0 # Fix the size of array to have starting points with coordinated (500, 0) inside
offsety = 500 - miny # Find out the "offety" to be use to set y to 500 later...
lenx, leny = maxx-minx, maxy-miny
#print(minx, maxx, miny, maxy)

# Generate an empty wall (of sound!)
thewall = [["." for y in range(leny+1)] for x in range(lenx+1)]
#renderwall(thewall)

# Draw the rocks on the wall !
for y in range(len(stratae)):
    for x in range(len(stratae[y]) - 1):
        start = stratae[y][x].split(",")
        end = stratae[y][x+1].split(",")
        #print(start, end)
        lstartx, lstarty = int(start[0]) - miny, int(start[1]) - minx
        lendx, lendy = int(end[0]) - miny, int(end[1]) - minx
        #print(f"passing: {lstartx}, {lstarty}, {lendx}, {lendy} @ {y}:{x}")
        #print("\n")
        drawrocks(lstartx, lstarty, lendx, lendy, thewall)

# And now, let us drop that sand !
def sanddrop(wall, x, y):
    # Move down
    if wall[x+1][y] == ".":
        wall[x][y] = "."
        wall[x+1][y] = "o"
        renderwall(wall)
        sanddrop(wall, x+1, y)
    elif wall[x+1][y] == "#" or wall[x+1][y] == "o":
        if wall[x+1][y] == "o" and x == 0:
            wall[x][y] = "o"
            return
        else:
            renderwall(wall)
            sanddrop(wall, 0, y)
    else:
        return

def dropsand(wall, offsety):
    wall[0][offsety] = "+"
    sanddrop(wall, 0, offsety)

dropsand(thewall, offsety)
renderwall(thewall)