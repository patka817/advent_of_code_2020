#!/user/bin/python

result = 0
results = []
with open("input.txt", 'r') as input:
    groupAllYesAnswers = set()
    first = True
    questions = []
    for line in input:
        if line == "\n":
            results.append(len(groupAllYesAnswers))
            groupAllYesAnswers = set()
            questions = []
            first = True
        else:
            questions = [char for char in line.strip()]
            if first:
                groupAllYesAnswers = set(questions)
                first = False
            else:
                groupAllYesAnswers.intersection_update(set(questions))
    results.append(len(groupAllYesAnswers))

print(sum(results))