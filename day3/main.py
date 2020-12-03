#!/user/bin/python

#
inputValues = []
modulus = 0

with open("input.txt", 'r') as input:
    inputValues = [l.strip() for l in input.readlines()]
    modulus = len(inputValues[0])

def calcSlope(deltaX, deltaY):
    posX = 0
    posY = 0
    trees = 0
    while posY < len(inputValues)-1:
        posX = (posX + deltaX) % modulus
        posY = posY + deltaY
        #print("X: {}, Y: {}".format(posX, posY))
        char = inputValues[posY][posX]
        if char == '#':
            trees = trees + 1
    return trees


res1 = calcSlope(1, 1)
res2 = calcSlope(3, 1)
res3 = calcSlope(5, 1)
res4 = calcSlope(7, 1)
res5 = calcSlope(1, 2)

print(res1*res2*res3*res4*res5)
