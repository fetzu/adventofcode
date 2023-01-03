# AoC 2022, Day 3: Rucksack // Part 1
f = open("03_data.txt","r")
lines = f.readlines()

score = 0
bailout = False

def ASCOORE(char):
    global score
    if char.islower():
        score += (ord(char) - 96)
    elif char.isupper():
        score += (ord(char) - 38)
    return score

for line in lines:
    length = int(len(line) / 2)
    left = line[:length]
    right = line[length:]

    for item in left:
        for otheritem in right:
            if item == otheritem and bailout is False:
                #print(f"Hit for {item}")
                ASCOORE(item)
                bailout = True
    bailout = False



print(score)