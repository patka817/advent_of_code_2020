#!/user/bin/python

def getCubeState(x,y,z, state):    
    if z in state and y in state[z] and x in state[z][y]:
        return state[z][y][x]
    else:
        return '.'

def nextStateForCube(x,y,z, state):
    cubeState = getCubeState(x,y,z, state)
    neighbours = []
    xDiffs = [x-1, x, x+1]
    yDiffs = [y-1, y, y+1]
    zDiffs = [z-1, z, z+1]
    for xDiff in xDiffs:
        # if xDiff < 0:
        #     continue
        for yDiff in yDiffs:
            # if yDiff < 0:
            #     continue
            for zDiff in zDiffs:
                if xDiff == x and yDiff == y and zDiff == z:
                    continue
                neighbours.append(getCubeState(xDiff, yDiff, zDiff, state))
    activeSum = sum([1 for x in neighbours if x == '#'])
    if cubeState == '.' and activeSum == 3:
        return "#"
    elif cubeState == '#' and activeSum in [2, 3]:
        return "#"
    else:
        return "."

def runCycle(state):
    minZ = min(state)
    maxZ = max(state)
    minY = min(state[minZ])
    maxY = max(state[minZ])
    minX = min(state[minZ][minY])
    maxX = max(state[minZ][minY])
    nextState = {}
    for z in range(minZ-1, maxZ+2):
        nextState[z] = {}
        for y in range(minY-1, maxY+2):
            nextState[z][y] = {}
            for x in range(minX-1, maxX+2):
                cState = nextStateForCube(x, y, z, state)
                nextState[z][y][x] = cState

    return nextState

def countActive(state):
    active = 0
    for z in state:
        for y in state[z]:
           active += sum([1 for x in state[z][y] if state[z][y][x] == '#'])
    return active


def printState(state):
    print("------------------------")
    for z in state:
        print("Z={}".format(z))
        for y in sorted(state[z].keys()):
            xState = sorted(state[z][y].keys())
            xValues = [state[z][y][x] for x in xState]
            print("".join(xValues))
    print("------------------------")
    
state = {0: {}}
with open("../test.txt", 'r') as input:
    z = 0
    for (y, line) in enumerate(input.readlines()):
        state[z][y] = {}
        for (x, char) in enumerate(line.strip()):
            state[z][y][x] = char


for i in range(0,6):
    state = runCycle(state)
printState(state)
print(countActive(state))