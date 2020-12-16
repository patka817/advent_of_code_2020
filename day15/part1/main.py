#!/user/bin/python

numbersIndexes = {}
spokenNumbers = []
startingNumbers= []

def incrementNumberIndex(number, index):
    if number in numbersIndexes:
        numbersIndexes[number].append(index)
        numbersIndexes[number] = numbersIndexes[number][-2:]
    else:
        numbersIndexes[number] = [index]

with open("../test.txt", 'r') as input:
    for line in input.readlines():
        startingNumbers = [int(x) for x in line.split(",")]
        startingNumbers.reverse()

spokenNumbersLength = 0
while len(spokenNumbers) < 2020:
    if len(startingNumbers) > 0:
        nextNumber = startingNumbers.pop()
        spokenNumbers.append(nextNumber)
        incrementNumberIndex(nextNumber, spokenNumbersLength)
        spokenNumbersLength += 1
    else:
        lastSpoken = spokenNumbers[-1]
        lastSpokenIndex = spokenNumbersLength
        thisNumber = -1
        if lastSpoken in numbersIndexes and len(numbersIndexes[lastSpoken]) > 1:
            indexes = numbersIndexes[lastSpoken]
            thisNumber = indexes[-1] - indexes[-2]
        else:
            thisNumber = 0
            
        spokenNumbers.append(thisNumber)
        incrementNumberIndex(thisNumber, spokenNumbersLength)
        spokenNumbersLength += 1
        

print(spokenNumbers[-1])

    
