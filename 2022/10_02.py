# AoC 2022, Day 1: Private Screen(ing) // Part 2

f = open("10_data.txt","r")
instructions = f.readlines()

X = 1
cycle = 0
queue = []
results = []

#CRT = ["o" * 40]*6
CRT = []

def renderCRT():
    for i in range(len(CRT)):
        if i > 2 and i % 40 == 0: print()
        print(CRT[i], end = '')

def drawCRT(X, cycle):
    char = cycle % 40
    #print(f"drawCRT, cycle #{cycle}, X is {X} and char is {char}")

    if X == char - 2 or X == char or X == char - 1:
        CRT.append("#")
    else:
        CRT.append(".")

# Add up the results at given cycles
def checkcycle(cycle, X, results):
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
        #print(f"cycle {cycle}, X = {X} | adding {X * cycle} to result")
        results.append((X * cycle))
    #print(f"cycles: {cycle}")
    drawCRT(X, cycle)

for instruction in instructions:
    instruction = instruction.split()

    # If the (FIFO) queue is not empty, cycle the first item
    if len(queue) > 0:
        #print(f"cycles: {cycle} | queue")
        cycle += 1
        checkcycle(cycle, X, results)
        X = X + int(queue[0])
        queue.pop(0)

    # Take care of the next instruction in the input data
    if instruction[0] == "noop":
        #print(f"cycles: {cycle} | noop")
        cycle += 1    
        checkcycle(cycle, X, results)
    elif instruction[0] == "addx":
        #print(f"cycles: {cycle} | addx")
        cycle += 1
        queue.append(instruction[1])
        checkcycle(cycle, X, results)

print(f"total cycles: {cycle}")
#print(X)
#print(results)
#print(sum(results))
#print(CRT)
#print(len(CRT))
renderCRT()