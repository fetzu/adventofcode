# AoC 2022, Day 10: Single Register // Part 1

f = open("10_data.txt","r")
instructions = f.readlines()

X = 1
cycle = 0
queue = []
results = []

# Add up the results at given cycles
def checkcycle(cycle, X, results):
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
        print(f"cycle {cycle}, X = {X} | adding {X * cycle} to result")
        results.append((X * cycle))

for instruction in instructions:
    instruction = instruction.split()

    # If the (FIFO) queue is not empty, cycle the first item
    if len(queue) > 0:
        print(f"cycles: {cycle} | queue")
        cycle += 1
        checkcycle(cycle, X, results)
        X = X + int(queue[0])
        queue.pop(0)

    # Take care of the next instruction in the input data
    if instruction[0] == "noop":
        print(f"cycles: {cycle} | noop")
        cycle += 1    
        checkcycle(cycle, X, results)
    elif instruction[0] == "addx":
        print(f"cycles: {cycle} | addx")
        cycle += 1
        queue.append(instruction[1])
        checkcycle(cycle, X, results)

print(f"cycles: {cycle}")
#print(X)
print(results)
print(sum(results))