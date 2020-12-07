#!/user/bin/python

rules = {}

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
            containing_dict[ruleBagID] = int(count)
    return BagRule(bagID, containing_dict)

def getBagCount(bagID, count):
    print("Getting bag {} with count {}".format(bagID, count))
    rule = rules[bagID]
    result = count
    if len(rule.contains) == 0:
        return result
    
    for (id, subcount) in rule.contains.items():
        result += getBagCount(id, subcount*count)
    return result


with open("../input.txt", 'r') as input:
    for line in input.readlines():
        bagRule = extractBagRule(line)
        rules[bagRule.id] = bagRule


bags = getBagCount("shiny gold", 1)
bagsWithoutShinyGold = bags -1
print(bagsWithoutShinyGold)
