# AoC 2022, Day 11: Monkey Business // Part 2
import math
import operator

f = open("11_data.txt","r")
lines = f.readlines()
lastline = lines[-1]

ROUNDS = 10000
businessacumen = []
monkeypack = []
monkeybusiness = 0

operators = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.xor,
}

# You know what, this is an oppotunity to learn classes...
class Monkey:
    def __init__(self, number, operator, amount, test, iftrue, iffalse):
        self.number = number
        self.items = []
        self.operator = operator
        self.opamount = amount
        self.test = test
        self.iftrue = int(iftrue)
        self.iffalse = int(iffalse)
        self.inspectioncount = 0
    
    def additem(self, item):
        self.items.append(int(item))

    def inscpectitems(self):
        for i in range(len(self.items)):
            if self.opamount == "old": opamountcorr = int(self.items[i])
            else: opamountcorr = int(self.opamount)
            #print(f"{self.number}: {self.items[i]} {type(self.items[i])}, {opamountcorr}")
            self.items[i] = math.floor((operators[self.operator](self.items[i], opamountcorr)) % lcm)
            self.inspectioncount = self.inspectioncount + 1

    def testitems(self):
        for _ in range(len(self.items)):
            if not self.items:
                pass
            else:
                if (self.items[0] % int(self.test)) == 0:
                    monkeypack[self.iftrue].additem(self.items[0])
                else:
                    monkeypack[self.iffalse].additem(self.items[0])
                self.items.pop(0)
        

# Work through the input to create our pack !
for line in lines:
    # Brute force finding the number of monkeys in dataset
    if line.startswith("Monkey"):
        tmp1 = line.removeprefix("Monkey")
        tmp2 = tmp1.replace(":", "")
        monkeynumber = int(tmp2)
        monkeypack.append(f"m{monkeynumber}")

    # VERY elegant and efficient way of going through the items...
    if line.startswith("  Starting items:"):
        tmp1 = line.removeprefix("  Starting items:")
        tmp2 = tmp1.removesuffix("\n")
        startingitems = tmp2.split(",")
        for i in range(len(startingitems)):
            startingitems[i] = startingitems[i].removeprefix(" ")
    
    if line.startswith("  Operation:"):
        tmp1 = line.removeprefix("  Operation: new = old ")
        tmp2 = tmp1.split()
        optype = tmp2[0]
        opamount = tmp2[1] # Watchout: amount can be "old" (aka "times itself")

    if line.startswith("  Test:"):
        tmp1 = line.removeprefix("  Test: divisible by ")
        tmp2 = tmp1.removesuffix("\n")
        test = tmp2

    if line.startswith("    If true:"):
        tmp1 = line.removeprefix("    If true: throw to monkey ")
        tmp2 = tmp1.removesuffix("\n")
        iftrue = tmp2

    if line.startswith("    If false:"):
        tmp1 = line.removeprefix("    If false: throw to monkey ")
        tmp2 = tmp1.removesuffix("\n")
        iffalse = tmp2   

    # Create the monkey !
    if line == '\n' or line is lastline:
        monkeypack[monkeynumber] = Monkey(monkeynumber, optype, opamount, test, iftrue, iffalse)
        for item in startingitems:
            monkeypack[monkeynumber].additem(item)

def printmonkeys():
    for i in range(len(monkeypack)):
        mon = monkeypack[i]
        print(vars(mon))

# Part 2: Find the least common multiple for set 
def findlcm():
    lcmset = []
    for i in range(len(monkeypack)):
        lcmset.append(int(monkeypack[i].test))
    lcm = math.lcm(*lcmset) #[math.lcm() for i in range(len(lcmset))]
    print(f"Least common multiple for the set {lcmset} is: {lcm}")
    return lcm

# And now, let us take care of monkeybusiness !
def dingdingding():
    for i in range(len(monkeypack)):
        monkeypack[i].inscpectitems()
        monkeypack[i].testitems()

def closingbell():
    for i in range(len(monkeypack)):
        businessacumen.append(monkeypack[i].inspectioncount)
    businessacumen.sort()
    monkeybusiness = businessacumen[-1] * businessacumen[-2]
    return monkeybusiness

lcm = findlcm()
for _ in range(ROUNDS): dingdingding()
monkeybusiness = closingbell()


printmonkeys()
print(f"businessacumen: {businessacumen}")
print(f"result = {monkeybusiness}")