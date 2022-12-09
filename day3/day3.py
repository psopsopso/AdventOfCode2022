with open("inputday3.txt") as f:
    data = f.read().splitlines()

priorityDictLowerCase = {}
for i in range(1, 27):
    priorityDictLowerCase[chr(i+96)] = i

priorityDictUpperCase = {}
for i in range(27, 53):
    priorityDictUpperCase[chr(i+38)] = i

PRIORITYDICT = priorityDictLowerCase | priorityDictUpperCase


def sumPriorities(data):
    sum = 0
    for line in data:
        compartmentsSize = len(line) // 2
        firstCompartment = line[:compartmentsSize]
        secondCompartment = line[compartmentsSize:]
        commonChar = ''.join(
            set(firstCompartment).intersection(secondCompartment))
        sum += PRIORITYDICT[commonChar]
    return sum


answerPartOne = sumPriorities(data)


def sumPrioritiesPartTwo(data):
    sum = 0
    for i in range(0, len(data), 3):
        tempArr = data[i:i+3]
        commonChar = ''.join(set.intersection(*map(set, tempArr)))
        sum += PRIORITYDICT[commonChar]
    return sum


answerPartTwo = sumPrioritiesPartTwo(data)

print(answerPartOne)
print(answerPartTwo)
