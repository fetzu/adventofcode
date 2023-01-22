# AoC 2022, Day 15: Beacon Cheeseburger // Part 1

import re

f = open("15_data.txt","r")
lines = f.readlines()

sensorsbeaconpairs = {}
manhattandistances = {}
results = set()

# Line of Interest
RLINE = 2000000

# Go through the data and extract sensor and beacon pairs, put them into our dict, get the Manhattan Distance between sensor and beaucon
for line in lines:
    line = line.split(":")
    sx, sy = re.findall('-?\d+', line[0])
    bx, by = re.findall('-?\d+', line[1])
    sensorsbeaconpairs[(int(sx), int(sy))] = (int(bx), int(by))
    manhattandistances[(int(sx), int(sy))] = (abs(int(sx)-int(bx))+abs(int(sy)-int(by)))

#print(sensors)
#print(manhattandistances)

# Get the min / max x coordinate value of the beacons
maxbx = max(max(sensorsbeaconpairs.values()))
minbx = min(min(sensorsbeaconpairs.values()))

# Loop through all our sensor/beacon pairs and extract all matches for the line of interest
for i in range(minbx*10, maxbx*10):
    for sensor,bdist in manhattandistances.items():
        if (abs(sensor[0]-i)+abs(sensor[1]-RLINE)) <= bdist:
            if(i, RLINE) not in sensorsbeaconpairs.values():
                results.add((i, RLINE))

print(len(results))