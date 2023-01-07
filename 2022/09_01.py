# AoC 2022, Day 9: Rope-in // Part 1

f = open("09_data.txt","r")
instructions = f.readlines()

# Prepare instructions as an array of moves (0 is direction, 1 is length) 
moves = []
steps = []
for lines in instructions:
    move = lines.split()
    moves.append(move)

# Figure out the size of the 2D Array we are going to be working on
x = 0
y = 0
xmax = 0
ymax = 0
xmin = 0
ymin = 0
for i in range(len(moves)):
    
    if moves[i][0] == "R": x += int(moves[i][1])
    if moves[i][0] == "L": x -= int(moves[i][1])
    if moves[i][0] == "U": y += int(moves[i][1])
    if moves[i][0] == "D": y -= int(moves[i][1])

    if x > xmax: xmax = x
    if x < xmin: xmin = x
    if y > ymax: ymax = y
    if y < ymin: ymin = y
xrange = xmax - xmin
yrange = ymax - ymin

# Create our 2D Bridge array
#bridge = [[False for y in range(yrange)] for x in range(xrange)]
bridge = [[False for y in range(2000)] for x in range(2000)]

# Setting the start position for head and tail
#bridge[-xmin][-ymin] = "head"
#head = [-xmin, -ymin]
#tail = [-xmin, -ymin]
head = [1000, 1000]
tail = [1000, 1000]

# Let's get the head moving
for i in range(len(moves)):

    steps = [moves[i][0], moves[i][1]]
    
    for step in range(int(steps[1])):
        if steps[0] == "R": 
            head[0] = int(head[0]) + 1
        if steps[0] == "L": 
            head[0] = int(head[0]) - 1
        if steps[0] == "D": 
            head[1] = int(head[1]) + 1
        if steps[0] == "U": 
            head[1] = int(head[1]) - 1

        # And now let's get the tail to follow...
        dirx = head[0] - tail[0]
        diry = head[1] - tail[1]
        #print(f"step: {steps}, head: {head}, tail {tail}, move is {dirx}:{diry}")
    
        if dirx <= -2 and diry <= -1: 
            tail[0] = tail[0] - 1
            tail[1] = tail[1] - 1
        elif dirx <= -2 and diry >= 1: 
            tail[0] = tail[0] - 1
            tail[1] = tail[1] + 1
        elif dirx <= -2: 
            tail[0] = tail[0] - 1

        elif dirx >= 2 and diry >= 1: 
            tail[0] = tail[0] + 1
            tail[1] = tail[1] + 1
        elif dirx >= 2 and diry <= -1: 
            tail[0] = tail[0] + 1
            tail[1] = tail[1] - 1
        elif dirx >= 2: 
            tail[0] = tail[0] + 1

        if diry <= -2 and dirx <= -1: 
            tail[1] = tail[1] - 1
            tail[0] = tail[0] - 1
        elif diry <= -2 and dirx >= 1: 
            tail[1] = tail[1] - 1
            tail[0] = tail[0] + 1
        elif diry <= -2:
            tail[1] = tail[1] - 1

        elif diry >= 2 and dirx <= -1: 
            tail[1] = tail[1] + 1
            tail[0] = tail[0] - 1
        elif diry >= 2 and dirx >= 1: 
            tail[1] = tail[1] + 1
            tail[0] = tail[0] + 1
        elif diry >= 2:
            tail[1] = tail[1] + 1


        bridge[tail[0]][tail[1]] = True

#print(head)
#print(tail)
#print(bridge)
print(sum([i.count(True) for i in bridge]))