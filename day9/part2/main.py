#!/user/bin/python

# 5 test, 25 real
preambleCount = 25
allowedLowestIndex = 0
numbers = []
invalidNumberIndex = -1
invalidNumber = -1

def isValid(value, amongNumbers):
    #print(amongNumbers)
    for first in amongNumbers:
        for second in amongNumbers:
            if first + second == value:
                return True

    return False

def tryFindContSet(summedValue, numbers):
    startIndex = 0
    values = []
    index = startIndex
    while startIndex < len(numbers):
        values.append(numbers[index])
        if sum(values) == summedValue and len(values) > 1:
            break
        elif sum(values) > summedValue:
            startIndex += 1
            values = []
            index = startIndex
        else:
            index += 1
    return values

    
with open("../input.txt", 'r') as input:
    for line in input.readlines():
        numbers.append(int(line))
    #print(numbers)

valueIndex = preambleCount
while valueIndex < len(numbers):
    value = numbers[valueIndex]
    #print("Doing value {}".format(value))
    if isValid(value, numbers[valueIndex-preambleCount:valueIndex]) is False:
        invalidNumberIndex = valueIndex
        invalidNumber = value
        break
    else:
        valueIndex += 1

contSet = tryFindContSet(invalidNumber, numbers[:invalidNumberIndex])
print(min(contSet) + max(contSet))