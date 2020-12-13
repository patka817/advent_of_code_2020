#!/user/bin/python

import math

def findTime(busID, offset, time, incrementFactor):
    while (time + offset) % busID != 0:
        time += incrementFactor
    return time

def parseBuses(row):
    return [int(x.strip()) for x in row.split(',') if x.strip() != 'x']

def parseOffsets(row):
    offsets = {}
    for (idx, id) in enumerate(row.split(',')):
        if id.strip() != 'x':
            offsets[int(id.strip())] = idx
    return offsets

buses = []
timeOffsets = {}
with open("../input.txt", 'r') as input:
    for idx, line in enumerate(input.readlines()):
        if idx == 0:
            continue
        else:
            buses = parseBuses(line)
            timeOffsets = parseOffsets(line)

busOffsets = [timeOffsets[x] for x in buses]

startBusID = buses[0]
minimalTime = 0
increment = 1

for idx, bus in enumerate(buses):
    offset = busOffsets[idx]
    minimalTime = findTime(bus, offset, minimalTime, increment)
    increment *= bus

print("minimal time: {}".format(minimalTime))
print(minimalTime)