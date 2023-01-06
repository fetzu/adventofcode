# AoC 2022, Day 8: On the Grid // Part 2

# Recusions are fun and should be unlimited. Plus my MacBook has a lot of RAM !
import sys
sys.setrecursionlimit(1000)

f = open("08_data.txt","r")
trees = f.read()

# Let us build a nice array the size of our input, assuming the forest is a square
forestsize = int(len(trees) ** 0.5)
forest = [[0 for y in range(forestsize)] for x in range(forestsize)]
#print(forestsize)
#print(forest)
#print(trees)

# Let's clean input data by getting rid of those pesky linereturns...
seert = []
for tree in trees:
    if tree != "\n": seert.append(tree)

# Let's fill our forest with trees...!
x = 0
y = 0
for tree in seert:
    #print(f"Tree is {tree} at position x:{x} y:{y}")
    forest[y][x] = tree
    if x >= forestsize - 1:
        y += 1
        x = 0
    else:
        x += 1
forestedge = len(forest) - 1

leftbitmap = [[True for y in range(forestsize)] for x in range(forestsize)]
rightbitmap = [[True for y in range(forestsize)] for x in range(forestsize)]
upbitmap = [[True for y in range(forestsize)] for x in range(forestsize)]
downbitmap = [[True for y in range(forestsize)] for x in range(forestsize)]
maxheightbuffer = [["0" for y in range(forestsize)] for x in range(forestsize)]

def generatebitmap_leftright(forest, bitmap):
    for y in range(len(forest)):
        for x in range(len(forest)):
            #print(f"Loop at position y:{y} x:{x}")
            maxheightbuffer[x][y] = forest[x][y]
            if x == 0 or x == forestedge or y == 0 or y == (forestsize -1):
                #print(f"Edge case at {y} {x}!")
                pass
            elif forest[x][y] < forest[x-1][y] or maxheightbuffer[x-1][y] >= forest[x][y]:
                bitmap[x][y] = False

            if x == 0 or x == forestedge or y == 0 or y == (forestsize -1):
                pass
            elif maxheightbuffer[x-1][y] >= maxheightbuffer[x][y]: 
                maxheightbuffer[x][y] = maxheightbuffer[x-1][y]

def generatebitmap_rightleft(forest, bitmap):
    for y in reversed(range(len(forest))):
        for x in reversed(range(len(forest))):
            maxheightbuffer[x][y] = forest[x][y]
            if x == 0 or x == forestedge or y == 0 or y == (forestsize -1):
                pass
            elif forest[x][y] < forest[x+1][y] or maxheightbuffer[x+1][y] >= forest[x][y]:
                bitmap[x][y] = False

            if x == 0 or x == forestedge or y == 0 or y == (forestsize -1):
                pass
            elif maxheightbuffer[x+1][y] >= maxheightbuffer[x][y]: 
                maxheightbuffer[x][y] = maxheightbuffer[x+1][y]

def generatebitmap_updown(forest, bitmap):
    for x in range(len(forest)):
        for y in range(len(forest)):
            maxheightbuffer[x][y] = forest[x][y]
            if x == 0 or x == forestedge or y == 0 or y == (forestsize -1):
                pass
            elif forest[x][y] < forest[x][y-1] or maxheightbuffer[x][y-1] >= forest[x][y]:
                bitmap[x][y] = False

            if x == 0 or x == forestedge or y == 0 or y == (forestsize -1):
                pass
            elif maxheightbuffer[x][y-1] >= maxheightbuffer[x][y]: 
                maxheightbuffer[x][y] = maxheightbuffer[x][y-1]

def generatebitmap_downup(forest, bitmap):
    for x in reversed(range(len(forest))):
        for y in reversed(range(len(forest))):
            maxheightbuffer[x][y] = forest[x][y]
            #print(f"before: {y} {x} value {maxheightbuffer[x][y]}")
            if x == 0 or x == forestedge or y == 0 or y == (forestsize -1):
                pass
            elif forest[x][y] < forest[x][y+1] or maxheightbuffer[x][y+1] >= forest[x][y]:
                bitmap[x][y] = False
            
            if x == 0 or x == forestedge or y == 0 or y == (forestsize -1):
                pass
            elif maxheightbuffer[x][y+1] >= maxheightbuffer[x][y]: 
                maxheightbuffer[x][y] = maxheightbuffer[x][y+1]

def countvisiblefromedges(forest):
    for x in range(len(forest)):
        for y in range(len(forest)):
            anybitmap[x][y] = leftbitmap[x][y] | downbitmap[x][y] | rightbitmap[x][y] | upbitmap[x][y]

## Part Deux ##
scenicscores = [["0" for y in range(forestsize)] for x in range(forestsize)]

# Recursive because I hate myself. vx and vy are vectors, theight is the height of the tree to test)
def lookup(x, y, vx, vy, count, theight):
    #print(f"Looking at {x}:{y} with vectors {vx}:{vy} | length:{len(forest)} | height:{theight} | count:{count}")
    if x == 0:
        if count == 0: count = 1
        return count
    elif theight > forest[x + vx][y + vy]:
        count += 1
        #print(f"Recusion @ {x}:{y} (value {theight}) with count @ {count} | vx: {vx} vy: {vy}")
        #print(f"Next step: lookright with {x+vx}, {y+vy}, {vx}, {vy}, {count}")
        return lookup(x + vx, y + vy, vx, vy, count, theight)
    else:
        if count == 0: count = 1
        else: count += 1
        return count

def lookleft(x, y, vx, vy, count, theight):
    #print(f"Looking at {x}:{y} with vectors {vx}:{vy} | length:{len(forest)} | height:{theight} | count:{count}")
    if y == 0:
        if count == 0: count = 1
        return count
    elif theight > forest[x + vx][y + vy]:
        count += 1
        #print(f"Recusion @ {x}:{y} (value {theight}) with count @ {count} | vx: {vx} vy: {vy}")
        #print(f"Next step: lookleft with {x+vx}, {y+vy}, {vx}, {vy}, {count}")
        return lookleft(x + vx, y + vy, vx, vy, count, theight)
    else:
        if count == 0: count = 1
        else: count += 1
        return count

def lookdown(x, y, vx, vy, count, theight):
    #print(f"Looking at {x}:{y} with vectors {vx}:{vy} | length:{len(forest) - 1} | height:{theight} | count:{count}")
    if x == forestedge:
        if count == 0: count = 1
        return count
    elif theight > forest[x + vx][y + vy]:
        count += 1
        #print(f"Recusion @ {x}:{y} (value {theight}) with count @ {count} | vx: {vx} vy: {vy}")
        #print(f"Next step: lookdown with {x+vx}, {y+vy}, {vx}, {vy}, {count}")
        return lookdown(x + vx, y + vy, vx, vy, count, theight)
    else:
        if count == 0: count = 1
        else: count += 1
        return count

def lookright(x, y, vx, vy, count, theight):
    #print(f"Looking at {x}:{y} with vectors {vx}:{vy} | length:{len(forest) - 1} | height:{theight} | count:{count}")
    if y == forestedge:
        #print(f"(end of y) Done with {x}:{y} with total of {count}")
        if count == 0: count = 1
        return count
    elif theight > forest[x + vx][y + vy]:
        count += 1
        #print(f"Recusion @ {x}:{y} (value {theight}) with count @ {count} | vx: {vx} vy: {vy}")
        #print(f"Next step: lookright with {x+vx}, {y+vy}, {vx}, {vy}, {count}")
        return lookright(x + vx, y + vy, vx, vy, count, theight)
    else:
        if count == 0: count = 1
        else: count += 1
        #print(f"(else) Done with {x}:{y} with total of {count}")
        return count

def scenicscore():
    for x in range(len(forest)):
        for y in range(len(forest)):
            #count = 0
            #print(f"Looking for {x}:{y} (value {forest[x][y]})")
            theight = forest[x][y]
            scenicscores[x][y] = lookup(x, y, -1, 0, 0, theight) * lookleft(x, y, 0, -1, 0, theight) * lookdown(x, y, 1, 0, 0, theight) * lookright(x, y, 0, 1, 0, theight)
            #scenicscores[x][y] = lookup(x, y, -1, 0, 0, theight)
            #scenicscores[x][y] = lookleft(x, y, 0, -1, 0, theight)
            #scenicscores[x][y] = lookdown(x, y, 1, 0, 0, theight)
            #scenicscores[x][y] = lookright(x, y, 0, 1, 0, theight)

            #print(f"Done looking for {x}:{y} (value {forest[x][y]}) with count @ {scenicscores[x][y]}")


generatebitmap_leftright(forest, leftbitmap)
generatebitmap_rightleft(forest, rightbitmap)
generatebitmap_updown(forest, upbitmap)
generatebitmap_downup(forest, downbitmap)

anybitmap = [[True for y in range(forestsize)] for x in range(forestsize)]
countvisiblefromedges(forest)

scenicscore()

#print(f"leftright: {leftbitmap}")
#print(f"rightleft: {rightbitmap}")
#print(f"updown: {upbitmap}")
#print(f"downup: {downbitmap}")
#print(f"anybitmap: {anybitmap}")

#print(sum([i.count(True) for i in anybitmap]))
#print(forest)
#print(scenicscores)
print(max(map(max, scenicscores)))