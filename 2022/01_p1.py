# AoC 2022, Day 1: Calories // Part 1
f = open("01_data.txt","r")
hoarder = 0
zwischen = 0

lines = f.readlines()

for line in lines:
    if line == '\n':
        #print("Empty line")
        if zwischen > hoarder:
            #print(f"Hit at {zwischen}")
            hoarder = zwischen
            zwischen = 0
        else:
            #print(f"Miss at {zwischen}")
            zwischen = 0
    else:
        zwischen = zwischen + int(line)

print(hoarder)