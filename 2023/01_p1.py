# AoC 2023, Day 1: Here we go again... // Part 1
f = open("01_data.txt","r")
lines = f.readlines()
linecounter = -1
linevalue = 0
total = 0

for line in lines:
    charcounter = 0
    linecounter += 1
    for char in line:
        if char.isdigit():
            if charcounter == 0: firstchar = char
            lastchar = char
            charcounter += 1
    totline = int(firstchar + lastchar)
    total = total + totline     

print(total)