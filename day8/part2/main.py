#!/user/bin/python

accumulator = 0
visited = []
originalCommands = []
commands = []
changedIndexes = []
index = 0

def acc(value, index):
    global accumulator
    accumulator += value
    return index+1

def jmp(value, index):
    return index+value

def nop(value, index):
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

def changeNextInstruction():
    global commands
    for (index, tuple) in enumerate(commands):
        if tuple[0] == 'nop' and index not in changedIndexes:
            changedIndexes.append(index)
            commands[index] = ("jmp", tuple[1])
            break
        elif tuple[0] == 'jmp' and index not in changedIndexes:
            changedIndexes.append(index)
            commands[index] = ("nop", tuple[1])
            break

def reset():
    global accumulator
    global visited
    global index
    global commands
    visited = []
    accumulator = 0
    commands = readCommands()
    index = 0

def readCommands():
    commands = []
    with open("../input.txt", 'r') as input:
        for line in input.readlines():
            commandAndValue = line.split(" ")
            command = commandAndValue[0].strip()
            value = int(commandAndValue[1].strip())
            commands.append((command, value))
    return commands

commands = readCommands()
while index < len(commands):
    next = commands[index]
    nextIndex = callFunc(next, index)
    visited.append(index)
    if nextIndex in visited:
        reset()
        changeNextInstruction()
    else:
        index = nextIndex

print(accumulator)