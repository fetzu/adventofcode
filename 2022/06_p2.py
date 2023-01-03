# AoC 2022, Day 6: Secret Comms // Part 2
f = open("06_data.txt","r")
lines = f.read()
chars = list(lines)
queue = len(chars) - 14

buffer = []

# Buffer the first 3 characters
for n in range(14):
    buffer.append(chars[n])

# Check for uniqueness of chars in buffer, break and print number of iterations if needed
for i in range(queue):
    buffer.append(chars[i])
    if len(buffer) > len(set(buffer)):
        buffer.pop(0)
    else:
        print(f"Result is {i} with {buffer}")
        break

#print(buffer)