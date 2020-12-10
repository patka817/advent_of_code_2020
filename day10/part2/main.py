#!/user/bin/python

adapters = []
joltageMaxDiff = 3

def findCandidates(currentJoltage, joltages):
    candidates = [x for x in joltages if currentJoltage+joltageMaxDiff >= x and x > currentJoltage]
    # print("Candidates for {} is {}".format(currentJoltage, candidates))
    return candidates

skipped = 0
invalidAdapterPaths = []
validAdaptersStarts = {} # key: adapter joltage, value: nr of branches it have that are valid 
def findSolution(soughtJoltage, currentJoltage, adapters):
    global invalidAdapterPaths
    global validAdaptersStarts
    global skipped
    if currentJoltage == soughtJoltage:
        return 1
    candidates = findCandidates(currentJoltage, adapters)
    if len(candidates) == 0 or currentJoltage > soughtJoltage:
        return 0
    
    count = 0
    for candidate in candidates:
        candAdapters = [x for x in adapters if x != candidate]
        if candidate in invalidAdapterPaths:
            skipped += 1
            continue
        elif candidate in validAdaptersStarts:
            count += validAdaptersStarts[candidate]
        else:
            subcount = findSolution(soughtJoltage, candidate, candAdapters)
            if subcount > 0:
                validAdaptersStarts[candidate] = subcount
                count += subcount
            else:
                invalidAdapterPaths.append(candidate)

    return count
    
with open("../input.txt", 'r') as input:
    for line in input.readlines():
        adapters.append(int(line))

deviceAdapterJoltage = max(adapters)+3
adapters.append(deviceAdapterJoltage)
print(findSolution(deviceAdapterJoltage, 0, adapters))


