#!/user/bin/python

def valid(limits, value):
    for limit in limits:
        if value >= limit[0] and value <= limit[1]:
            return True
    return False

def parseRule(line, rulesMap):
    splitted = line.split(':')
    name = splitted[0]
    ruleValues = splitted[1].split('or')
    limits = []
    for ruleValue in ruleValues:
        values = ruleValue.split('-')
        low = int(values[0])
        high = int(values[1])
        limits.append((low, high))
    rulesMap[name] = lambda x: valid(limits, x)

def errorRateForTicket(ticketLine, rules):
    values = [int(x) for x in ticketLine.split(',')]
    for value in values:
        validValue = False
        for rule in rules.values():
            if rule(value) is True:
                validValue = True
                break
        if validValue is False:
            return value
    return None

rules = {}
parseStep = 0
myticket = ''
errorRates = []
with open("../input.txt", 'r') as input:
    for line in input.readlines():
        if line == '\n':
            continue
        if 'your ticket' in line:
            parseStep = 1
            continue
        elif 'nearby tickets' in line:
            print(myticket)
            parseStep = 2
            continue
        
        if parseStep == 0:
            parseRule(line, rules)
        elif parseStep == 1:
            myticket = line
        else:
            errorValue = errorRateForTicket(line, rules)
            if errorValue is not None:
                errorRates.append(errorValue)
        

print(errorRates)
print(sum(errorRates))