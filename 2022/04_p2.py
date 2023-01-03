# AoC 2022, Day 4: Camp Cleanup // Part 2
f = open("04_data.txt","r")
lines = f.readlines()

count = 0
i = 0
buffer = []

for line in lines:
    pairs = line.split(',')
    
    for pair in pairs:
        item = pair.split('-')
        buffer.append(item)
        i += 1
        if i == 2 and int(buffer[0][0]) <= int(buffer[1][0]) and int(buffer[0][1]) >= int(buffer[1][0]):
            count += 1
        elif i == 2 and int(buffer[0][1]) >= int(buffer[1][0]) and int(buffer[0][1]) <= int(buffer[1][1]):
            count += 1
        elif i == 2 and int(buffer[1][0]) >= int(buffer[0][0]) and int(buffer[1][1]) <= int(buffer[0][1]):
            count += 1
        elif i == 2 and int(buffer[1][1]) >= int(buffer[0][0]) and int(buffer[1][1]) <= int(buffer[0][1]):
            count += 1
        if i == 2:
            buffer = []
            i = 0

print(count)