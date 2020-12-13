#!/user/bin/python

def parseRow(row):
    action = row[0]
    value = row[1:].strip()
    return (action, int(value))

def turnRight(wx, wy, value):
    if value > 360:
        raise RuntimeError()
    degrees = 360 - value
    return turnLeft(wx, wy, degrees)

def turnLeft(wx, wy, value):
    modVal = value % 360
    if modVal == 90:
        return (-wy, wx)
    elif modVal == 180:
        return (-wx, -wy)
    elif modVal == 270:
        return (wy, -wx)
    raise RuntimeError()

def waypointActionResolver(action, value, we, wn):
    if action == 'N':
        return (we, wn + value)
    elif action == 'S':
        return (we, wn - value)
    elif action == 'E':
        return (we + value, wn)
    elif action == 'W':
        return (we - value, wn)
    elif action == 'R':
        return turnRight(we, wn, value)
    elif action == 'L':
        return turnLeft(we, wn, value)
    raise RuntimeError()


def result(north, east):
    return abs(north) + abs(east)

waypointNorth = 1
waypointEast = 10
shipNorth = 0
shipEast = 0

with open("../input.txt", 'r') as input:
    for line in input.readlines():
        (action, value) = parseRow(line)
        if action == 'F':
            shipNorth += (waypointNorth*value)
            shipEast += (waypointEast*value)
        else:
            (east, north) = waypointActionResolver(action, value, waypointEast, waypointNorth)
            waypointNorth = north
            waypointEast = east

print(shipNorth)
print(shipEast)
print(result(shipNorth, shipEast))