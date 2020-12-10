#!/user/bin/python

adapters = []
joltageMaxDiff = 3

def findCandidates(currentJoltage, joltages):
    candidates = [x for x in joltages if currentJoltage+joltageMaxDiff >= x and x > currentJoltage]
    print("Candidates for {} is {}".format(currentJoltage, candidates))
    return candidates

    
with open("../input.txt", 'r') as input:
    for line in input.readlines():
        adapters.append(int(line))
    
    print(adapters)

diffs = {1: 0, 2: 0, 3: 0}
currentJoltage = 0
deviceAdapterJoltage = max(adapters)+3
adapters.append(deviceAdapterJoltage)
while currentJoltage < deviceAdapterJoltage:
    candidates = findCandidates(currentJoltage, adapters)
    candidate = min(candidates)
    diffs[candidate-currentJoltage] += 1
    currentJoltage = candidate

print(diffs)
print(diffs[1]*diffs[3])


