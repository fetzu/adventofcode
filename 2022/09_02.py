# AoC 2022, Day 9: Rope-in // Part 2

f = open("09_data.txt","r")
instructions = f.readlines()

# Prepare instructions as an array of moves (0 is direction, 1 is length) 
moves = []
steps = []
for lines in instructions:
    move = lines.split()
    moves.append(move)

# Figure out the size of the 2D Array we are going to be working on
#x = 0
#y = 0
#xmax = 0
#ymax = 0
#xmin = 0
#ymin = 0
#for i in range(len(moves)):
#    
#    if moves[i][0] == "R": x += int(moves[i][1])
#    if moves[i][0] == "L": x -= int(moves[i][1])
#    if moves[i][0] == "U": y += int(moves[i][1])
#    if moves[i][0] == "D": y -= int(moves[i][1])
#
#    if x > xmax: xmax = x
#    if x < xmin: xmin = x
#    if y > ymax: ymax = y
#    if y < ymin: ymin = y
#xrange = xmax - xmin
#yrange = ymax - ymin

# Create our 2D Bridge array
#bridge = [[False for y in range(yrange)] for x in range(xrange)]
bridge = [[False for y in range(2000)] for x in range(2000)]

# Setting the start position for head and tail
#bridge[-xmin][-ymin] = "head"
#head = [-xmin, -ymin]
#tail = [-xmin, -ymin]
head = [1000, 1000]
tail = [1000, 1000]
# The rope has 10 knots now...
rope = [head, [1000, 1000], [1000, 1000], [1000, 1000], [1000, 1000], [1000, 1000], [1000, 1000], [1000, 1000], [1000, 1000], tail]

# The rope being longer, we now need a system to move the remaining pieces along
def ropein(rope, step):
    for i in range(1, len(rope)):
        dirx = rope[i-1][0] - rope[i][0]
        diry = rope[i-1][1] - rope[i][1]
        #print(f"step #{step} knot #{i} | i-1: {rope[i-1]}, i:{rope[i]}, move is {dirx}:{diry}")
    
        # Cases where the knot should not move: same x/y and four adjacent corners
        if abs(dirx) <= 1 and abs(diry) <= 1:
            #print("No move!")
            pass

        # Let us move that knot
        if dirx <= -2 and diry <= -1: 
            rope[i][0] = rope[i][0] - 1
            rope[i][1] = rope[i][1] - 1
        elif dirx <= -2 and diry >= 1: 
            rope[i][0] = rope[i][0] - 1
            rope[i][1] = rope[i][1] + 1
        elif dirx <= -2: 
            rope[i][0] = rope[i][0] - 1

        elif dirx >= 2 and diry >= 1: 
            rope[i][0] = rope[i][0] + 1
            rope[i][1] = rope[i][1] + 1
        elif dirx >= 2 and diry <= -1: 
            rope[i][0] = rope[i][0] + 1
            rope[i][1] = rope[i][1] - 1
        elif dirx >= 2: 
            rope[i][0] = rope[i][0] + 1

        elif diry <= -2 and dirx <= -1: 
            rope[i][1] = rope[i][1] - 1
            rope[i][0] = rope[i][0] - 1
        elif diry <= -2 and dirx >= 1: 
            rope[i][1] = rope[i][1] - 1
            rope[i][0] = rope[i][0] + 1
        elif diry <= -2:
            rope[i][1] = rope[i][1] - 1

        elif diry >= 2 and dirx <= -1: 
            rope[i][1] = rope[i][1] + 1
            rope[i][0] = rope[i][0] - 1
        elif diry >= 2 and dirx >= 1: 
            rope[i][1] = rope[i][1] + 1
            rope[i][0] = rope[i][0] + 1
        elif diry >= 2:
            rope[i][1] = rope[i][1] + 1

    #return rope


# Let's get the head moving (just for the head !)
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

        #print(f"Calling ropein() @ step #{i} / {step}")
        ropein(rope, i)

        bridge[tail[0]][tail[1]] = True

#print(rope)
#print(bridge)
print(sum([i.count(True) for i in bridge]))