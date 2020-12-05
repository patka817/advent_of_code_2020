#!/user/bin/python
import re
# key:value 

rows = 128
columns = 8
nrRowChar = 7
nrOfColChar = 3

def calcSeatIDFromBoarding(boarding):
    [row, col] = calcRowCol(boarding)
    return calcSeat(row, col)

def calcSeat(row, col):
    return row*8+col

def calcRowCol(boarding):
    minRow = 0
    maxRow = rows-1
    for char in boarding[:nrRowChar]:
        [minRow, maxRow] = calcInterval(minRow, maxRow, char)
    
    print("rows {} {}".format(minRow, maxRow))
    
    minCol = 0
    maxCol = columns-1
    for char in boarding[-nrOfColChar:]:
        [minCol, maxCol] = calcInterval(minCol, maxCol, char)
    print("cols {} {}".format(minCol, maxCol))
    return [minRow, minCol]
    

def calcInterval(intervalMin, intervalMax, char):
    if char in ['F', 'L']:
        return lowerHalf(intervalMin, intervalMax)
    elif char in ['B', 'R']:
        return upperHalf(intervalMin, intervalMax)
    raise RuntimeError

def upperHalf(min, max):
    halfDst = (max - min + 1)/2
    return [min+halfDst, max]

def lowerHalf(min, max):
    halfDst = (max - min + 1)/2
    return [min, max - halfDst]

inputValues = []
with open("input.txt", 'r') as input:
    for line in input.readlines():
        inputValues.append(line.strip())
    # print(inputValues)

res = max([calcSeatIDFromBoarding(boarding) for boarding in inputValues])
print(res)