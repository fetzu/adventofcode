# AoC 2023, Day 4: A whole lotto-numbers // Part 2

f = open("04_data.txt","r")
cards = f.readlines()
score = 0

stack = cards

for card in stack:
    card_number = int(card.split(':')[0].split()[1])
    numbers = card.split(": ")[1].split(" | ")
    winningnumbers = set(int(num) for num in numbers[0].split())
    mynumbers = set(int(num) for num in numbers[1].split())
    matches = len(winningnumbers.intersection(mynumbers))
    for i in range(1, matches + 1): stack.append(cards[card_number + (i - 1)])

print(len(stack))