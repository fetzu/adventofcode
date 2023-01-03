# AoC 2022, Day 3: Rucksack // Part 2
f = open("03_data.txt","r")
lines = f.readlines()

score = 0
count = 0

def ASCOORE(char):
    global score
    if char.islower():
        score += (ord(char) - 96)
    elif char.isupper():
        score += (ord(char) - 38)
    return score

while len(lines) != 0: 
    buffer = lines[:3]
    
    for item in buffer[0]:
        if item in buffer[1]:
            if item in buffer[2]:
                ASCOORE(item)
                count += 1
                #print(f"Hit #{count} for {item} with score of {score}")
                break

    for n in range(3):
        lines.pop(0)

print(score)