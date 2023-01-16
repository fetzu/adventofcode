# AoC 2022, Day 15: Beacon Cheeseburger // Part 1

import re

f = open("15_data.txt","r")
lines = f.readlines()

sensors = {}
	


# Go through the data and extract sensor and beacon pairs, put them into our dict
for line in lines:
    line = line.split(":")
    sx, sy = re.findall('-?\d+', line[0])
    bx, by = re.findall('-?\d+', line[1])
    sensors[(int(sx), int(sy))] = (int(bx), int(by))

print(sensors)