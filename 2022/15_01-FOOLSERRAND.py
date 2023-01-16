# AoC 2022, Day 15: Beacon Cheeseburger // Part 1
# NOTE: This will not work with input data (gigantic arrays would be needed), have to look for another solution (set, dict?)

import re

f = open("15_data.txt","r")
lines = f.readlines()

sensors = []
beacons = []
xvals = []
yvals = []


# Go through the data and extract sensor and beacon pairs
for line in lines:
    line = line.split(":")
    sensors.append(re.findall('-?\d+', line[0]))
    beacons.append(re.findall('-?\d+', line[0]))
    for pair in line:
        pair = pair.split(",")
        xvals.append(re.findall('-?\d+', pair[0]))
        yvals.append(re.findall('-?\d+', pair[1]))

# Define the min/max of each type to determine the size of our array
minxvals, maxxvals = min(xvals), max(xvals)
minyvals, maxyvals = min(yvals), max(yvals)
minxvals, maxxvals, minyvals, maxyvals = int(minxvals[0]), int(maxxvals[0]), int(minyvals[0]), int(maxyvals[0])

tunnels = [["." for y in range(minyvals, maxyvals)] for x in range(minxvals, maxxvals)]
print(tunnels)