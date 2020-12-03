#!/user/bin/python

# lower-upper char: password

def isValid(password, lowerLimit, upperLimit, char):
    firstHit = password[lowerLimit-1] == char
    secHit = password[upperLimit-1] == char
    return (firstHit and not secHit) or (not firstHit and secHit)
    #return occur >= lowerLimit and occur <= upperLimit

def extractLower(policy):
    return int(policy.split('-')[0])

def extractUpper(policy):
     return int(policy.split('-')[1].split(' ')[0])

def extractChar(policy):
    return policy.split(' ')[1].replace(':', '')

def extractPassword(policy):
    return policy.split(' ')[2]


inputValues = []
with open("input.txt", 'r') as input:
    inputValues = [l.strip() for l in input.readlines()]

result = 0
for policy in inputValues:
    password = extractPassword(policy)
    char = extractChar(policy)
    lower = extractLower(policy)
    upper = extractUpper(policy)
    if isValid(password, lower, upper, char):
        result = result + 1
print(result)