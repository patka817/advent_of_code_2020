#!/user/bin/python

class BagRule:
    def __init__(self, id, contains):
        self.id = id
        self.contains = contains

def extractBagRule(line):
    print(line)
    splitted = line.split("contain")
    
    bagID = splitted[0].split("bag")[0].strip()
    rules = [x.strip() for x in splitted[1].split(",")]
    containing_dict = {}
    print(bagID)
    print(rules)
    if rules == ["no other bags."]:
        print("!!!!!!!!")
    else:
        for rule in rules:
            count = rule[0]
            ruleBagID = rule[1:].split("bag")[0].strip()
            print("Rule")
            print(count)
            print(ruleBagID)
            containing_dict[ruleBagID] = count
    return BagRule(bagID, containing_dict)


rules = []
with open("../input.txt", 'r') as input:
    for line in input.readlines():
        rules.append(extractBagRule(line))


bagsToCheck = ["shiny gold"]
canContain = set()
while len(bagsToCheck) > 0:
    bagID = bagsToCheck.pop()
    for rule in rules:
        if bagID in rule.contains:
            print("{} contains {}".format(rule.id, bagID))
            bagsToCheck.append(rule.id)
            canContain.add(rule.id)

print(len(canContain))
