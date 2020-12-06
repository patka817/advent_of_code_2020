#!/user/bin/python
import re
# key:value 



inputValues = []
with open("input.txt", 'r') as input:
    groupYesAnswers = set()
    for line in input.readlines():
        # print(line)
        if line == "\n":
            inputValues.append(groupYesAnswers)
            groupYesAnswers = set()
        else:
            questions = [char for char in line.strip()]
            # print(questions)
            groupYesAnswers.update(questions)

    inputValues.append(groupYesAnswers) # get the last

print(sum([len(x) for x in inputValues]))