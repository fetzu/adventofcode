# AoC 2023, Day 1: ...it's going to be a hard year? // Part 1
f = open("01_data.txt","r")
lines = f.readlines()
linecounter = -1
linevalue = 0
total = 0
buffer = []

numbervalues = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def checknumber(string):
    for number, value in numbervalues.items():
        if number in string:
            return value

for line in lines:
    charcounter = 0
    linecounter += 1
    for char in line:
        if char.isdigit():
            if charcounter == 0: firstchar = char
            lastchar = char
            charcounter += 1
            buffer.clear()
        if char.isalpha:
            #print(char)
            buffer.append(char)
            if len(buffer) > 5: buffer.pop(0)
            tres = checknumber(''.join(buffer))
            if tres is not None:
                if charcounter == 0: firstchar = str(tres)
                lastchar = str(tres)
                del buffer[:1]
                charcounter += 1
    buffer.clear()
    totline = int(firstchar + lastchar)
    #print(totline)
    total = total + totline     

print(total)