#!/user/bin/python

def getAdjacentFreeCount(seatX, seatY, map):
    maxX = len(map[0])-1
    maxY = len(map)-1
    count = 0
    xDiffs = [1, -1, 0]
    yDiffs = [1, -1, 0]
    if seatX == 0:
        xDiffs = [1, 0]
    elif seatX == maxX:
        xDiffs = [-1, 0]

    if seatY == 0:
        yDiffs = [1, 0]
    elif seatY == maxY:
        yDiffs = [-1, 0]
    
    free = 0
    occu = 0
    for x in xDiffs:
        for y in yDiffs:
            if x == 0 and y == 0:
                continue
            nextX = seatX+x
            nextY = seatY+y
            while True:
                if nextX > maxX or nextX < 0:
                    break
                elif nextY > maxY or nextY < 0:
                    break
                if map[nextY][nextX] == 'L':
                    free += 1
                    break
                elif map[nextY][nextX] == '#':
                    occu += 1
                    break
                
                nextX = nextX+x
                nextY = nextY+y

    return [free, occu]


def getChange(seatX, seatY, map):
    current = map[seatY][seatX]
    if current == '.':
        return '.'
    
    [free, occu] = getAdjacentFreeCount(seatX, seatY, map)
    if current == 'L' and occu == 0:
        return '#'
    elif current == '#' and occu >= 5:
        return 'L'
    return current

def doRound(map):
    newMap = []
    for (y, row) in enumerate(map):
        newMap.append([])
        for (x, char) in enumerate(row):
            change = getChange(x, y, map)
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
