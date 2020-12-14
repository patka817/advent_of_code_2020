#!/user/bin/python

def decimalToBin(dec):
    binRep = []
    binRep[:0] = bin(dec)[2:]
    paddings = 36 - len(binRep)
    return [0]*paddings + binRep

def binlistToDecimal(bin):
    asString = "".join([str(x) for x in bin])
    binaryString = "0b" + asString
    return int(binaryString, 2)

def parseMask(line):
    mask = line.split('=')[1].strip()
    res = {}
    for (idx, char) in enumerate(mask):
        if char != 'X':
            res[idx] = int(char)
    return res

def applyMask(mask, dec):
    binary = decimalToBin(dec)
    for key in mask:
        binary[key] = mask[key]
    maskedDecimal = binlistToDecimal(binary)
    print('masked {} to {}'.format(dec, maskedDecimal))
    return maskedDecimal

def doMem(line, mask, mem):
    decValue = int(line.split('=')[1].strip())
    print(line.split('[')[1])
    memIdx = int(line.split('[')[1].split(']')[0])
    print("mem[{}] = {}".format(memIdx, decValue))
    maskedVal = applyMask(mask, decValue)
    mem[memIdx] = maskedVal

mem = {}
mask = {}
with open("../input.txt", 'r') as input:
    for idx, line in enumerate(input.readlines()):
        if 'mask' in line:
            mask = parseMask(line)
        else:
            doMem(line, mask, mem)

nonZeroes = [mem[x] for x in mem if mem[x] != 0]

print(sum(nonZeroes))
