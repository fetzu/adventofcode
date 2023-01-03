# AoC 2022, Day 2: Rock, Paper, Scissors // Part 2
f = open("02_data.txt","r")
rounds = f.readlines()

score = 0

for round in rounds:
    hand = str.split(round)

    if hand[0] == "A":
        if hand[1] == "X":
            score += 3
            score += 0
        elif hand[1] == "Y":
            score += 1
            score += 3
        elif hand[1] == "Z":
            score += 2
            score += 6  

    elif hand[0] == "B":
        if hand[1] == "X":
            score += 1
            score += 0
        elif hand[1] == "Y":
            score += 2
            score += 3
        elif hand[1] == "Z":
            score += 3
            score += 6   
    
    elif hand[0] == "C":
        if hand[1] == "X":
            score += 2
            score += 0
        elif hand[1] == "Y":
            score += 3
            score += 3
        elif hand[1] == "Z":
            score += 1
            score += 6 


print(score)
