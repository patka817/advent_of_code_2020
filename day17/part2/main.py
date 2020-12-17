#!/user/bin/python

def getCubeState(w, x,y,z, state):    
    if w in state and z in state[w] and y in state[w][z] and x in state[w][z][y]:
        return state[w][z][y][x]
    else:
        return '.'

def nextStateForCube(w, x,y,z, state):
    cubeState = getCubeState(w,x,y,z, state)
    neighbours = []
    wDiffs = [w-1, w, w+1]
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
                for wDiff in wDiffs:
                    if xDiff == x and yDiff == y and zDiff == z and wDiff == w:
                        continue
                    neighbours.append(getCubeState(wDiff, xDiff, yDiff, zDiff, state))
    activeSum = sum([1 for x in neighbours if x == '#'])
    if cubeState == '.' and activeSum == 3:
        return "#"
    elif cubeState == '#' and activeSum in [2, 3]:
        return "#"
    else:
        return "."

def runCycle(state):
    minW = min(state)
    maxW = max(state)
    minZ = min(state[minW])
    maxZ = max(state[minW])
    minY = min(state[minW][minZ])
    maxY = max(state[minW][minZ])
    minX = min(state[minW][minZ][minY])
    maxX = max(state[minW][minZ][minY])
    nextState = {}
    for w in range(minW-1, maxW+2):
        nextState[w] = {}
        for z in range(minZ-1, maxZ+2):
            nextState[w][z] = {}
            for y in range(minY-1, maxY+2):
                nextState[w][z][y] = {}
                for x in range(minX-1, maxX+2):
                    cState = nextStateForCube(w, x, y, z, state)
                    nextState[w][z][y][x] = cState

    return nextState

def countActive(state):
    active = 0
    for w in state:
        for z in state[w]:
            for y in state[w][z]:
                active += sum([1 for x in state[w][z][y] if state[w][z][y][x] == '#'])
    return active


def printState(state):
    print("------------------------")
    for w in state:
        for z in state:
            print("Z={}, W={}".format(z, w))
            for y in sorted(state[w][z].keys()):
                xState = sorted(state[w][z][y].keys())
                xValues = [state[w][z][y][x] for x in xState]
                print("".join(xValues))
    print("------------------------")
    
state = {0: {0: {}}}
with open("../input.txt", 'r') as input:
    z = 0
    w = 0
    for (y, line) in enumerate(input.readlines()):
        state[w][z][y] = {}
        for (x, char) in enumerate(line.strip()):
            state[w][z][y][x] = char


for i in range(0,6):
    state = runCycle(state)
print(countActive(state))