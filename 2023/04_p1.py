# AoC 2023, Day 4: A whole lotto-numbers // Part 1

f = open("04_data.txt","r")
cards = f.readlines()
score = 0

for card in cards:
    numbers = card.split(": ")[1].split(" | ")
    winningnumbers = set(int(num) for num in numbers[0].split())
    mynumbers = set(int(num) for num in numbers[1].split())
    matches = len(winningnumbers.intersection(mynumbers))
    if matches >=2: score = score + (2 ** (matches - 1))
    elif matches == 1: score = score + 1

print(score)