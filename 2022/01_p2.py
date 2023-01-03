# AoC 2022, Day 1: Calories // Part 2
f = open("01_data.txt","r")
hoarders = [0] * 3
zwischen = 0

lines = f.readlines()

for line in lines:
    if line == '\n':
        #print("Empty line")
        for hoarder in hoarders:
            if hoarder < zwischen:
                #print(f"Hit at {zwischen}")
                hoarders[-1] = zwischen
                hoarders.sort(reverse=True)
                zwischen = 0
        else:
            #print(f"Miss at {zwischen}")
            zwischen = 0
    else:
        zwischen = zwischen + int(line)

print(sum(hoarders))
