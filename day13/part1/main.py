#!/user/bin/python

import math

def parseBuses(row):
    return [int(x.strip()) for x in row.split(',') if x.strip() != 'x']

earliestDepTime = 0
buses = []
with open("../input.txt", 'r') as input:
    for idx, line in enumerate(input.readlines()):
        if idx == 0:
            earliestDepTime = int(line.strip())
        else:
            buses = parseBuses(line)
        
print(earliestDepTime)


factors = [ math.ceil(float(earliestDepTime)/float(x)) for x in buses]

print(buses)
print(factors)

minutesToWait = 9999999999
busID = -1
for (idx, factor) in enumerate(factors):
    id = buses[idx]
    waitTime = factor*id - earliestDepTime
    if waitTime < minutesToWait:
        minutesToWait = waitTime
        busID = id

print("busID: {}".format(busID))
print("Minutes to wait: {}".format(minutesToWait))
print("BusiD*mintuesToWait = {}".format(busID*minutesToWait))