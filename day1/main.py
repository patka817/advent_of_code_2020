#!/bin/python



foundValues = []
result = None
end = False

inputValues = []
with open("input.txt", 'r') as input:
    inputValues = [int(l.strip()) for l in input.readlines()]
    print(inputValues)

for num, firstValue in enumerate(inputValues):
    if num == len(inputValues):
        print("END")
        break
    for secNum, secValue in enumerate(inputValues, start=num+1):
        if secNum == len(inputValues):
            print("END secNum")
            break
        if secValue + firstValue > 2020:
            print("Invalid, {} + {} > 2020".format(firstValue, secValue))
        for tNum, tVal in enumerate(inputValues, start=secNum+1):
            if firstValue + secValue + tVal == 2020:
                print("BINGO")
                print("result: {}".format(firstValue*secValue*tVal))
                exit(1)

    # for line in input.readlines():
    #     if end:
    #         print("end")
    #         break
    #     print("Handling {}".format(line))
    #     value = int(line.strip())
    #     for prevValue in foundValues:
    #         if (prevValue + value) == 2020:
    #             result = prevValue*value
    #             print(result)
    #             end = True
    #             break
    #     print("Done handling {}".format(value))
    #     foundValues.append(value)
                


print(result)