# AoC 2023, Day 2: WHAT'S IN THE BAG!? // Part 2
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
    gamemaxgreen = 0
    gamemaxred = 0
    gamemaxblue = 0
    #find out the number of rounds in that game
    for round in rounds:
        maxgreen = re.findall(r"(\d+) green", round) or [0]
        if gamemaxgreen < int(maxgreen[0]): gamemaxgreen = int(maxgreen[0])
        maxred = re.findall(r"(\d+) red", round) or [0]
        if gamemaxred < int(maxred[0]): gamemaxred = int(maxred[0])
        maxblue = re.findall(r"(\d+) blue", round)  or [0]
        if gamemaxblue < int(maxblue[0]): gamemaxblue = int(maxblue[0])
    score = score + gamemaxgreen * gamemaxred * gamemaxblue

print(score)