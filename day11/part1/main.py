#!/user/bin/python

def getAdjacentFreeCount(seatX, seatY, map):
    count = 0
    xDiffs = [1, -1, 0]
    yDiffs = [1, -1, 0]
    if seatX == 0:
        xDiffs = [1, 0]
    elif seatX == len(map[0])-1:
        xDiffs = [-1, 0]

    if seatY == 0:
        yDiffs = [1, 0]
    elif seatY == len(map)-1:
        yDiffs = [-1, 0]
    
    free = 0
    occu = 0
    for x in xDiffs:
        for y in yDiffs:
            if x == 0 and y == 0:
                continue
            # print("[{}][{}] : {}".format(y, x, map[seatY+y][seatX+x]))
            if map[seatY+y][seatX+x] == 'L':
                free += 1
            elif map[seatY+y][seatX+x] == '#':
                occu += 1
    return [free, occu]


def getChange(seatX, seatY, map):
    current = map[seatY][seatX]
    if current == '.':
        return '.'
    
    [free, occu] = getAdjacentFreeCount(seatX, seatY, map)
    # print("(y: {}, x: {}) free {} occu: {}".format(seatY, seatX, free, occu))
    if current == 'L' and occu == 0:
        return '#'
    elif current == '#' and occu >= 4:
        return 'L'
    return current

def doRound(map):
    newMap = []
    for (y, row) in enumerate(map):
        newMap.append([])
        for (x, char) in enumerate(row):
            change = getChange(x, y, map)
            # print("(y: {}, x: {}) {} -> {}".format(y, x, char, change))
            newMap[y].append(change)
    return newMap

def printMap(map):
    for row in map:
        print(row)

def readInput():
    map = []
    with open("../input.txt", 'r') as input:
        for idx,line in enumerate(input.readlines()):
            map.append([])
            for char in line.strip():
                map[idx].append(char)
            
    
    return map

def occuSeats(map):
    occu = 0
    for row in map:
        listOfOcc = [x for x in row if x == "#"]
        occu += len(listOfOcc)
    return occu

map = readInput()
while True:
    newMap = doRound(map)
    # print("*********")
    # printMap(newMap)
    # print("*********")
    if newMap == map:
        break
    map = newMap
print(occuSeats(map))
