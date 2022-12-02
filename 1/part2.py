import os

file = open(os.path.realpath(os.path.dirname(__file__)) + "\input.txt")

elves = []

foodAmount = 0
elfIndex = 0
fileLines = file.read().splitlines()

# tuple of index and value of most weighed down elf
solution = (0,0)

for idx, x in enumerate(fileLines):
    if(x == ""):
        elfIndex = elfIndex + 1
        elves.append((elfIndex, foodAmount))
        foodAmount = 0
        continue
    
    foodAmount += int(x)
    
    #handle last line
    if(idx+1 == len(fileLines)):
        elfIndex = elfIndex + 1
        elves.append((elfIndex, foodAmount))

def sortFunc(tup):
    return tup[1]

elves.sort(reverse=True, key=sortFunc)

print(elves[0])
print(elves[1])
print(elves[2])

print(elves[0][1] + elves[1][1] + elves[2][1])

file.close()
