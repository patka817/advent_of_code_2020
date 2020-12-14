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
        else:
            res[idx] = char
    # print("parsed mask {}".format(mask))
    return res

def applyMask(mask, dec):
    binaries = [decimalToBin(dec)]
    for key in mask:
        if mask[key] == 1 or mask[key] == '1':
            for binary in binaries:
                binary[key] = 1
        elif mask[key] == 'X':
            copies = []
            for binary in binaries:
                copycat = binary.copy()
                binary[key] = 1
                copycat[key] = 0
                copies.append(copycat)
            binaries.extend(copies)
    
    maskedDecimals = [binlistToDecimal(binary) for binary in binaries]
    #print("Masked {} to {}".format(dec, maskedDecimals))
    return maskedDecimals

def doMem(line, mask, mem):
    decValue = int(line.split('=')[1].strip())
    # print(line.split('[')[1])
    memIdx = int(line.split('[')[1].split(']')[0])
    # print("mem[{}] = {}".format(memIdx, decValue))
    indexes = applyMask(mask, memIdx)
    # print("Value {} -> indexes {}".format(decValue, indexes))
    for index in indexes:
        mem[index] = decValue

mem = {}
mask = {}
with open("../input.txt", 'r') as input:
    for idx, line in enumerate(input.readlines()):
        if 'mask' in line:
            mask = parseMask(line)
        else:
            doMem(line, mask, mem)

nonZeroes = [mem[x] for x in mem if mem[x] != 0]
# print(mem)
# print(len(mem))
print(sum(nonZeroes))
