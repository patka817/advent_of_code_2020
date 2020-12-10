#!/user/bin/python

# 5 test, 25 real
preambleCount = 25
allowedLowestIndex = 0
numbers = []

def isValid(value, amongNumbers):
    #print(amongNumbers)
    for first in amongNumbers:
        for second in amongNumbers:
            if first + second == value:
                return True

    return False
    
with open("../input.txt", 'r') as input:
    for line in input.readlines():
        numbers.append(int(line))
    #print(numbers)

valueIndex = preambleCount
while valueIndex < len(numbers):
    value = numbers[valueIndex]
    #print("Doing value {}".format(value))
    if isValid(value, numbers[valueIndex-preambleCount:valueIndex]) is False:
        print(value)
        break
    else:
        valueIndex += 1


