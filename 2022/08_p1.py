# AoC 2022, Day 8: On the Grid // Part 1
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
    forest[x][y] = tree
    if x >= forestsize - 1:
        y += 1
        x = 0
    else:
        x += 1

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
            if x == 0 or x == (forestsize - 1) or y == 0 or y == (forestsize -1):
                #print(f"Edge case at {y} {x}!")
                pass
            elif forest[x][y] < forest[x-1][y] or maxheightbuffer[x-1][y] >= forest[x][y]:
                bitmap[x][y] = False

            if x == 0 or x == (forestsize - 1) or y == 0 or y == (forestsize -1):
                pass
            elif maxheightbuffer[x-1][y] >= maxheightbuffer[x][y]: 
                maxheightbuffer[x][y] = maxheightbuffer[x-1][y]

def generatebitmap_rightleft(forest, bitmap):
    for y in reversed(range(len(forest))):
        for x in reversed(range(len(forest))):
            maxheightbuffer[x][y] = forest[x][y]
            if x == 0 or x == (forestsize - 1) or y == 0 or y == (forestsize -1):
                pass
            elif forest[x][y] < forest[x+1][y] or maxheightbuffer[x+1][y] >= forest[x][y]:
                bitmap[x][y] = False

            if x == 0 or x == (forestsize - 1) or y == 0 or y == (forestsize -1):
                pass
            elif maxheightbuffer[x+1][y] >= maxheightbuffer[x][y]: 
                maxheightbuffer[x][y] = maxheightbuffer[x+1][y]

def generatebitmap_updown(forest, bitmap):
    for x in range(len(forest)):
        for y in range(len(forest)):
            maxheightbuffer[x][y] = forest[x][y]
            if x == 0 or x == (forestsize - 1) or y == 0 or y == (forestsize -1):
                pass
            elif forest[x][y] < forest[x][y-1] or maxheightbuffer[x][y-1] >= forest[x][y]:
                bitmap[x][y] = False

            if x == 0 or x == (forestsize - 1) or y == 0 or y == (forestsize -1):
                pass
            elif maxheightbuffer[x][y-1] >= maxheightbuffer[x][y]: 
                maxheightbuffer[x][y] = maxheightbuffer[x][y-1]

def generatebitmap_downup(forest, bitmap):
    for x in reversed(range(len(forest))):
        for y in reversed(range(len(forest))):
            maxheightbuffer[x][y] = forest[x][y]
            #print(f"before: {y} {x} value {maxheightbuffer[x][y]}")
            if x == 0 or x == (forestsize - 1) or y == 0 or y == (forestsize -1):
                pass
            elif forest[x][y] < forest[x][y+1] or maxheightbuffer[x][y+1] >= forest[x][y]:
                bitmap[x][y] = False

            if x == 0 or x == (forestsize - 1) or y == 0 or y == (forestsize -1):
                pass
            elif maxheightbuffer[x][y+1] >= maxheightbuffer[x][y]: 
                maxheightbuffer[x][y] = maxheightbuffer[x][y+1]

def countvisiblefromedges(forest):
    for x in range(len(forest)):
        for y in range(len(forest)):
            anybitmap[x][y] = leftbitmap[x][y] | downbitmap[x][y] | rightbitmap[x][y] | upbitmap[x][y]


generatebitmap_leftright(forest, leftbitmap)
generatebitmap_rightleft(forest, rightbitmap)
generatebitmap_updown(forest, upbitmap)
generatebitmap_downup(forest, downbitmap)

anybitmap = [[True for y in range(forestsize)] for x in range(forestsize)]
countvisiblefromedges(forest)

#print(f"leftright: {leftbitmap}")
#print(f"rightleft: {rightbitmap}")
#print(f"upbitmap: {upbitmap}")
#print(f"downbitmap: {downbitmap}")
#print(f"anybitmap: {anybitmap}")
print(sum([i.count(True) for i in anybitmap]))