#!/user/bin/python
import re
# key:value 

def validHeight(value):
    if 'cm' in value:
        h = int(value.strip('cm'))
        return h >= 150 and h <= 193
    elif 'in' in value:
        h = int(value.strip('in'))
        return h >= 59 and h <= 76

def validHCL(value):
    if value[0] != '#':
        return False
    value = value.strip('#')
    regex = re.compile('^[0-9a-f]{6}$')
    return regex.match(value) != None

def validECL(value):
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

rules = {'byr': (lambda value : int(value) >= 1920 and int(value) <= 2002),
             'iyr': (lambda value : int(value) >= 2010 and int(value) <= 2020), 
             'eyr': (lambda value : int(value) >= 2020 and int(value) <= 2030), 
             'hgt': (lambda value : validHeight(value)), 
             'hcl': (lambda value : validHCL(value)),
              'ecl': (lambda value : validECL(value)), 
              'pid': (lambda value : len(value) == 9 and int(value))
}


def isValid(passport):
    for (key, rule) in rules.items():
        keyWithSuffix = '{}:'.format(key)
        if keyWithSuffix not in passport:
            return False
        
        value = passport.split(keyWithSuffix)[1].split(' ')[0]
        if not rule(value):
            print("invalid {}: {}".format(key, value))
            return False
    return True


inputValues = []

with open("input.txt", 'r') as input:
    passport = ''
    for line in input.readlines():
        if line != '\n':
            passport = passport + ' ' + line.strip()
        else:
            inputValues.append(passport)
            passport = ''
    inputValues.append(passport)
    # print(inputValues)

valid = 0
for passport in inputValues:
    if isValid(passport):
        valid += 1

print(valid)
    