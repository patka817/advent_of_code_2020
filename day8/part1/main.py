#!/user/bin/python

accumulator = 0
visited = []
commands = []

def acc(value, index):
    global accumulator
    # global visited
    accumulator += value
    # visited.append(index)
    return index+1

def jmp(value, index):
    # global visited
    # visited.append(index)
    return index+value

def nop(value, index):
    # global visited
    # visited.append(index)
    return index+1

def callFunc(tuple, index):
    command = tuple[0]
    value = tuple[1]
    if command == "acc":
        return acc(value, index)
    elif command == "jmp":
        return jmp(value, index)
    elif command == "nop":
        return nop(value, index)
    else:
        raise RuntimeError

with open("../input.txt", 'r') as input:
    for line in input.readlines():
        commandAndValue = line.split(" ")
        command = commandAndValue[0].strip()
        value = int(commandAndValue[1].strip())
        commands.append((command, value))

index = 0
while index < len(commands):
    next = commands[index]
    nextIndex = callFunc(next, index)
    visited.append(index)
    if nextIndex in visited:
        print(accumulator)
        break
    index = nextIndex

