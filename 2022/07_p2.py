# AoC 2022, Day 7: Bored Again Shell // Part 2
from collections import defaultdict

f = open("07_data.txt","r")
lines = f.readlines()

# Find maxdepth and initialise filesystem array
#maxdepth = 1
#for line in lines:
#    if line.count("$"):
#        if line.count("cd"):
#            dir = line.split()[2]
#            if dir == "..":
#                maxdepth -= 1
#            else:
#                maxdepth += 1
#filesystem = []*maxdepth

filesystem = []
filesizes = defaultdict(int)
currentdepth = 0

DISKSIZE = 70000000

for line in lines:
    if line.count("$"):
        if line.count("cd"):
            dir = line.split()[2]
            if dir == "..":
                filesystem.pop()
            else:
                currentdepth += 1
                path = f"{filesystem[-1]}/{dir}" if filesystem else dir
                filesystem.append(path)
        elif line.count("ls"):
            pass
    elif line.count("dir"):
            pass
    
    else:
        size, file = line.split()
        for path in filesystem:
            filesizes[path] += int(size)

availablespace = DISKSIZE - filesizes["/"]
neededspace = 30000000 - availablespace

for result in sorted(filesizes.values()):
    if result > neededspace:
        print(result)
        break