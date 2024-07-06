# AoC 2023, Day 2: WHAT'S IN THE BAG!? // Part 1
import re

f = open("02_data.txt","r")
games = f.readlines()
gamecounter = 0
score = 0

for game in games:
    gamecounter += 1
    rounds = game.split(";")
    numrounds = len(rounds)
    okrounds = 0
    #find out the number of rounds in that game
    for round in rounds:
        maxgreen = re.findall(r"(\d+) green", round)  or [0]
        maxred = re.findall(r"(\d+) red", round) or [0]
        maxblue = re.findall(r"(\d+) blue", round)  or [0]
        if int(maxgreen[0]) <= 13 and int(maxred[0]) <= 12 and int(maxblue[0]) <= 14:
            okrounds += 1
    if okrounds == numrounds: score += gamecounter

print(score)