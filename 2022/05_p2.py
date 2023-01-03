# AoC 2022, Day 5: Not Rust // Part 2
f = open("05_data.txt","r")
lines = f.readlines()

# Hardcoding this because I am dumb...
port = [["Q", "F", "M", "R", "L", "W", "C", "V"], ["D", "Q", "L"], ["P", "S", "R", "G", "W", "C", "N", "B"], ["L", "C", "D", "H", "B", "Q", "G"], ["V", "G", "L", "F", "Z", "S"], ["D", "G", "N", "P"], ["D", "Z", "P", "V", "F", "C", "W"], ["C", "P", "D", "M", "S"], ["Z", "N", "W", "T", "V", "M", "P", "C"]]

# discard all the lines without instructions
for line in lines:
    if not line.find("move"):
        move = line.split()
        #print(move[3])
        n = int(move[1])
        s = int(move[3]) - 1
        d = int(move[5]) - 1
        #print(f"Moving {n} containers from {s+1} to {d+1}")
        port[d].extend(port[s][-n:])
        port[s] = port[s][:-n]

print(port)
[print(p[-1], end="") for p in port]