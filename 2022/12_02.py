# AoC 2022, Day 12: On the Grid Again... // Part 2
from collections import deque

f = open("12_data.txt","r")
points = f.read()

#stepcounter = 0
startcoord = []
#endcoord = ()
frontier = []
results = []

# Function to convert the char values to int. ACTUALLY I did not need this... :/
#def giveint(char):
#    if char.isupper():
#        return ord(char) + 100
#    else:
#        return ord(char)

# Let us build a nice array the size of our input, assuming it is a square.. it is not...
ysize = int(len(points) ** 0.5) - 2
xsize = -1
for char in points: 
    if char == "\n": 
        break 
    else: xsize += 1
grid = [[[False for i in range(5)] for x in range(xsize+1)] for y in range(ysize+1)]


# Let's clean input data by getting rid of those pesky linereturns...
heightmap = []
for point in points:
    if point != "\n": heightmap.append(point)

# Let's fill our grid with heights...!
x = 0
y = 0
for height in heightmap:
    #print(f"Height is {height} at position x:{x} y:{y}")
    if height == "S": 
        startcoord.append((y, x))
        grid[y][x][0] = 97
    elif height == "E": 
        endcoord = (y, x)
        grid[y][x][0] = 122
    elif height == "a":
        startcoord.append((y, x))
        grid[y][x][0] = ord(height)
    else: grid[y][x][0] = ord(height)
    if x == xsize:
        y += 1
        x = 0
    else:
        x += 1

#maxheightbuffer = [["0" for y in range(gridsize)] for x in range(gridsize)]

def checkmoves(grid):
    for y in range(ysize+1):
        for x in range(xsize+1):
            #print(f"Loop at position y:{y} x:{x}")
            # Corner cases
            if x == 0 and y == 0:
                if grid[y][x][0] >= grid[y][x+1][0] - 1:
                    grid[y][x][2] = True
                if grid[y][x][0] >= grid[y+1][x][0] - 1:
                    grid[y][x][3] = True
                pass
            elif x == 0 and y == ysize:
                if grid[y][x][0] >= grid[y][x+1][0] - 1:
                    grid[y][x][2] = True
                if grid[y][x][0] >= grid[y-1][x][0] - 1:
                    grid[y][x][1] = True
                pass
            elif x == xsize and y == 0:
                if grid[y][x][0] >= grid[y+1][x][0] - 1:
                    grid[y][x][3] = True
                if grid[y][x][0] >= grid[y][x-1][0] - 1:
                    grid[y][x][4] = True
                pass
            elif x == xsize and y == ysize:
                if grid[y][x][0] >= grid[y-1][x][0] - 1:
                    grid[y][x][1] = True
                if grid[y][x][0] >= grid[y][x-1][0] - 1:
                    grid[y][x][4] = True
                pass

            # Edge cases
            elif x == 0:
                if grid[y][x][0] >= grid[y-1][x][0] - 1:
                    grid[y][x][1] = True
                if grid[y][x][0] >= grid[y][x+1][0] - 1:
                    grid[y][x][2] = True
                if grid[y][x][0] >= grid[y+1][x][0] - 1:
                    grid[y][x][3] = True
                pass
            elif y == 0:
                if grid[y][x][0] >= grid[y][x+1][0] - 1:
                    grid[y][x][2] = True
                if grid[y][x][0] >= grid[y+1][x][0] - 1:
                    grid[y][x][3] = True
                if grid[y][x][0] >= grid[y][x-1][0] - 1:
                    grid[y][x][4] = True
                pass
            elif x == xsize:
                if grid[y][x][0] >= grid[y-1][x][0] - 1:
                    grid[y][x][1] = True
                if grid[y][x][0] >= grid[y][x-1][0] - 1:
                    grid[y][x][4] = True
                if grid[y][x][0] >= grid[y+1][x][0] - 1:
                    grid[y][x][3] = True
                pass
            elif y == ysize:
                if grid[y][x][0] >= grid[y-1][x][0] - 1:
                    grid[y][x][1] = True
                if grid[y][x][0] >= grid[y][x+1][0] - 1:
                    grid[y][x][2] = True
                if grid[y][x][0] >= grid[y][x-1][0] - 1:
                    grid[y][x][4] = True
                pass


            else:
                if grid[y][x][0] >= grid[y-1][x][0] - 1:
                    #print("Able to move up")
                    grid[y][x][1] = True
                if grid[y][x][0] >= grid[y][x+1][0] - 1:
                    #print("Able to move right")
                    grid[y][x][2] = True
                if grid[y][x][0] >= grid[y+1][x][0] - 1:
                    #print("Able to move down")
                    grid[y][x][3] = True
                if grid[y][x][0] >= grid[y][x-1][0] - 1:
                    #print("Able to move left")
                    grid[y][x][4] = True

def buildqueue(grid):
    for y in range(ysize+1):
        for x in range(xsize+1):
            for dir in range(1, 5):
                if grid[y][x][dir] is True:
                    if (([[y], [x]])) in frontier:
                        None
                    else: frontier.append([[y], [x]])

# Bono Breadth First Search, Multiple Starts edition !
def bbfs(start, end):
    queue = deque()
    visited = set()
    queue.append([start])
    while queue:
        buffer = queue.popleft()
        y, x = buffer[-1]
        if (y, x) == end:
            #print("DONE !")
            #print(buffer)
            results.append(len(buffer) - 1)
            pass
        elif (y, x) not in visited:
            #print(f"y: {y}, x: {x}")
            if grid[y][x][1] is True:
                buffertwo = buffer[:]
                buffertwo.append((y-1, x))
                queue.append(buffertwo)
                #queue.append([[y-1], [x]])
            if grid[y][x][2] is True:
                buffertwo = buffer[:]
                buffertwo.append((y, x+1))
                queue.append(buffertwo)
                #queue.append([[y], [x+1]])
            if grid[y][x][3] is True:
                buffertwo = buffer[:]
                buffertwo.append((y+1, x))
                queue.append(buffertwo)
                #queue.append([[y+1], [x]])
            if grid[y][x][4] is True:
                buffertwo = buffer[:]
                buffertwo.append((y, x-1))
                queue.append(buffertwo)
                #queue.append([[y], [x-1]])
            visited.add((y, x))
        else:
            #print("Already visited!")
            pass
    #print("Queue is empty!")
            

# Trying to be a smartass but I am a dumdum...
#def findshortestpath(ypos, xpos, dir, stepcounter=0):
#    if grid[ypos][xpos][dir] is True:
#        print("right")
#        stepcounter += 1
#        return findshortestpath(ypos-1, xpos, 1, stepcounter)
#    if grid[ypos][xpos][dir+1] is True:
#        stepcounter += 1
#        return findshortestpath(ypos, xpos+1, 1, stepcounter)
#    if grid[ypos][xpos][dir+2] is True:
#        stepcounter += 1
#        return findshortestpath(ypos+1, xpos+1, 1, stepcounter)
#    if grid[ypos][xpos][dir+3] is True:
#        stepcounter += 1
#        return findshortestpath(ypos, xpos-1, 1, stepcounter)
#    else:
#        scoreboard.append(stepcounter)
#        stepcounter = 0
#        pass

# Call the functions to check moves and then find shortest path
checkmoves(grid)
#buildqueue(grid)
#print(len(frontier))
#print(frontier)
for (start) in startcoord:
    bbfs((start), endcoord)
#findshortestpath(0, 0, 1)
#print(grid)
print(min(results))