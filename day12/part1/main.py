#!/user/bin/python

degrees = {'E': 0, 'N': 90, 'W': 180, 'S': 270 }

def parseRow(row):
    action = row[0]
    value = row[1:].strip()
    return (action, int(value))

def turnRight(currentDirection, value):
    if value > 360:
        raise RuntimeError()
    degrees = 360 - value
    return turnLeft(currentDirection, degrees)

def turnLeft(currentDirection, value):
    curDeg = degrees[currentDirection]
    nextDeg = (curDeg + value) % 360
    for (key, degree) in degrees.items():
        print("{}: {}".format(key, degree))
        if degree == nextDeg:
            return key
    raise RuntimeError("Failed to get dir from degree change {} with current degree {}".format(value, curDeg))

def actionResolver(action, value, direction):
    if action == 'N':
        return (value, 0, direction)
    elif action == 'S':
        return (-value, 0, direction)
    elif action == 'E':
        return (0, value, direction)
    elif action == 'W':
        return (0, -value, direction)
    elif action == 'F':
        return actionResolver(direction, value, direction)
    elif action == 'R':
        return (0, 0, turnRight(direction, value))
    elif action == 'L':
        return (0, 0, turnLeft(direction, value))
    raise RuntimeError()


def result(north, east):
    return abs(north) + abs(east)

direction = 'E'
northValue = 0
eastValue = 0

with open("../input.txt", 'r') as input:
    for line in input.readlines():
        (action, value) = parseRow(line)
        (northChange, eastChange, newDirection) = actionResolver(action, value, direction)
        direction = newDirection
        northValue += northChange
        eastValue += eastChange

print(direction)
print(northValue)
print(eastValue)
print(result(northValue, eastValue))