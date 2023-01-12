# AoC 2022, Day 14: Not Tetris! // Part 1

# Recusions are fun and should be unlimited. Plus my MacBook has a lot of RAM !
import sys
sys.setrecursionlimit(100000)

# Let's see what's going on with those seg faults...
import faulthandler
faulthandler.enable()

f = open("14_data.txt","r")
lines = f.readlines()
stratae = []

#r = open("14_result.txt", "w")

def renderwall(wall, savefile=False):
    if savefile is True:
        open('14_result.txt', 'w').close()
        r = open("14_result.txt", "w")
    for i in wall:
        for j in i:
            print(j, end="")
            if savefile is True: r.write(j)
        print()
        if savefile is True: r.write("\n")
    print()
    if savefile is True: r.write("\n")

def reorder(left, right):
    if left > right:
        return right, left
    else:
        return left, right

def drawrocks(startx, starty, endx, endy, thewall):
    startx, endx = reorder(startx+1, endx+1)
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
offsety = 500 - miny + 1 # Find out the "offety" to be use to set y to 500 later...
lenx, leny = maxx-minx, maxy-miny
#print(minx, maxx, miny, maxy)

# Generate an empty wall (of sound!) with 1 extra line (our abyss) and 2 extra columns (the fall to abyss)
thewall = [["." for y in range(leny+3)] for x in range(lenx+2)]
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

# Draw the fire at the bottom (of hell!)
for i in range(len(thewall[1])):
    thewall[-1][i] = "§"

# Let's say the sand has to strafe
def sandstrafe(wall, x, y, poststrafe=False):
    #renderwall(wall)
    #if poststrafe is True: 
    #    print(f"DropG: {x}:{y}")
    #    sanddrop(wall, x, y, True)
    if wall[x+1][y-1] == ".":
        wall[x][y] = "."
        wall[x+1][y-1] = "o"
        #print(f"Poststrafe: {x+1}:{y-1} | Origin: 0:{offsety}")
        sanddrop(wall, x+1, y-1)
    elif wall[x+1][y+1] == ".":
        wall[x][y] = "."
        wall[x+1][y+1] = "o"
        #print("Poststrafe")
        sanddrop(wall, x+1, y+1)
    #else:
    #    sanddrop(wall, 0, offsety)


# And now, let us drop that sand !
def sanddrop(wall, x, y, resety=False):
    #renderwall(wall)
    if resety is True: y = offsety

    # Move down (keep falling)
    if wall[x+1][y] == ".":
        if wall[x][y] != wall[0][offsety]: wall[x][y] = "."
        wall[x+1][y] = "o"
        #renderwall(wall)
        sanddrop(wall, x+1, y)
    # Spot down is not free...
    elif wall[x+1][y] == "#" or wall[x+1][y] == "o" or wall[x+1][y] == "§" or wall[x+1][y] == "~":
        # alt: move diagonally
        if wall[x+1][y-1] == "." or wall[x+1][y+1] == ".":
            #print("Can Move Diagonally")
            sandstrafe(wall, x, y)
        # The wall is overflowing, game over ;)
        elif wall[x+1][y] == "o" and x == 0:
            wall[x][y] = "o"
            #print("No more moves possible.\n")
            return
        elif wall[x+1][y] == "§" or wall[x+1][y-1] == "§" or wall[x+1][y+1] == "§" or wall[x+1][y] == "~" or wall[x+1][y-1] == "~" or wall[x+1][y+1] == "~":
            wall[x][y] = "~"
            #sanddrop(wall, 0, y, True)
            return
        # Grain has come to a stop, start new cycle
        else:
            wall[x][y] = "o"
            #print(f"Dropping new grain at origin, because next is {wall[x+1][y]}")
            #renderwall(wall)
            sanddrop(wall, 0, y, True)
    else:
        return

def dropsand(wall, offsety):
    wall[0][offsety] = "+"
    sanddrop(wall, 0, offsety)

dropsand(thewall, offsety)

print("Final wall:")
renderwall(thewall)

print(sum([i.count("o") for i in thewall])-1)