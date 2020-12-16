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

def isValidTicket(ticket, rules):
    for value in ticket:
        validValue = False
        for rule in rules.values():
            if rule(value) is True:
                validValue = True
                break
        if validValue is False:
            return False
    return True

def checkCandidates(ticket, rules, candidates):
    for (index, value) in enumerate(ticket):
        for (name, rule) in rules.items():
            if rule(value) is False:
                candidates[name].remove(index)


def filterCandidates(candidates):
    filtered = False
    claimedIndexes = []
    for c in candidates:
        if len(candidates[c]) == 1:
            claimedIndexes.append(candidates[c][0])
    for c in candidates:
        indexes = candidates[c]
        if len(indexes) > 1:
            for claimed in claimedIndexes:
                if claimed in indexes:
                    indexes.remove(claimed)
                    candidates[c] = indexes
                    filtered = True
    return filtered

candidates = {}
rules = {}
parseStep = 0
myticket = []
tickets = []
with open("../input.txt", 'r') as input:
    for line in input.readlines():
        if line == '\n':
            continue
        if 'your ticket' in line:
            parseStep = 1
            for ruleName in rules:
                candidates[ruleName] = []
                for i in range(len(rules)):
                    candidates[ruleName].append(i)
            continue
        elif 'nearby tickets' in line:
            parseStep = 2
            continue
        
        if parseStep == 0:
            parseRule(line, rules)
        elif parseStep == 1:
            myticket = [int(x) for x in line.split(',')]
        else:
            ticket = [int(x) for x in line.split(',')]
            if isValidTicket(ticket, rules):
                checkCandidates(ticket, rules, candidates)
while True:        
    if filterCandidates(candidates) is False:
        break
print(myticket)
print(candidates)
depIndexes = [index[0] for (name, index) in candidates.items() if 'departure' in name]
print(depIndexes)

result = 1
for idx in depIndexes:
    result *= myticket[idx]
print(result)