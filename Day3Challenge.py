import os

def topLine(firstLine: str, secondLine: str) -> int:
    return middleLine("." * len(firstLine), firstLine, secondLine)

def middleLine(firstLine: str, secondLine: str, thirdLine: str) -> int:
    '''Evaluates the secondLine numbers to see if they should be added'''
    isInNumber = False
    digitCounter = 0
    otherCounter = 0 # Great label
    characterBuffer = ""
    numbersFound = [] # Contains tuples of index, number of digits, characters
    for char in secondLine:
        if str.isdigit(char):
            characterBuffer += char
            isInNumber = True
            digitCounter += 1
        else:
            if isInNumber:
                numbersFound.append(((otherCounter - digitCounter), digitCounter, characterBuffer))
            isInNumber = False
            digitCounter = 0
            characterBuffer = ""
        otherCounter += 1
    # Now numbersFound contains a tuple for every number in the firstLine
    verified = [] # This will be an array with tuples, booleans for each number signifying if they should be added and then the actual numbers
    for number in numbersFound:
        isVerif = False
        if number[0] > 0: # So we don't indexError
            if secondLine[number[0] - 1] != "." or firstLine[number[0] - 1] != "." or thirdLine[number[0] - 1] != ".":
                isVerif = True
        if (number[0] + number[1]) < (len(secondLine) - 1): # Again, so we don't indexError
            if secondLine[number[0] + number[1]] != "." or firstLine[number[0] + number[1]] != "." or thirdLine[number[0] + number[1]] != ".":
                isVerif = True
        for i in range(number[1]):
            if firstLine[number[0] + i] != "." or thirdLine[number[0] + i] != ".":
                isVerif = True
        verified.append((isVerif, int(number[2])))
    sum = 0
    for num in verified:
        if num[0]:
            sum += num[1]
    return sum

def findNumberAtIndex(index: int, lineNum: int, firstLine: str, secondLine: str, thirdLine: str) -> int:
    '''Finds a number given a specific index and line number. lineNum is 0 to 2'''
    isInNumber = False
    digitCounter = 0
    otherCounter = 0 # Great label
    characterBuffer = ""
    numbersFound = [] # Contains tuples of index, row, number of digits, characters
    lineCounter = 0
    for line in [firstLine, secondLine, thirdLine]:
        isInNumber = False
        digitCounter = 0
        otherCounter = 0 # Great label
        characterBuffer = ""
        for char in line:
            if str.isdigit(char):
                characterBuffer += char
                isInNumber = True
                digitCounter += 1
            else:
                if isInNumber:
                    numbersFound.append(((otherCounter - digitCounter), lineCounter, digitCounter, characterBuffer))
                isInNumber = False
                digitCounter = 0
                characterBuffer = ""
            otherCounter += 1
        lineCounter += 1
    # Now numbersFound contains a tuple for every number

    for number in numbersFound:
        if number[1] == lineNum:
            if index > number[0] - 1 and index < number[0] + number[2] + 1:
                return int(number[3])
    return int(-1)

def topLineGears(firstLine: str, secondLine: str) -> int:
    return middleLineGears("." * len(firstLine), firstLine, secondLine)

def bottomLineGears(firstLine: str, secondLine: str) -> int:
    return topLineGears(secondLine, firstLine)

def middleLineGears(firstLine: str, secondLine: str, thirdLine: str) -> int:
    '''Evaluates the secondLine gears and returns the sum of all ratios'''
    otherCounter = 0
    gearsFound = [] # Contains indices of each gear
    for char in secondLine:
        if char == "*":
            gearsFound.append(otherCounter)
        otherCounter += 1
    # Now gearsFound contains an index for every gear
    sum = 0

    gearComponents = [] # This will be an array of tuples, each containing 2 numbers that make up the gear
    for gear in gearsFound:
        numbers = [[-1, -1, -1], 
                   [-1, -1, -1], 
                   [-1, -1, -1]]
        if str.isdigit(secondLine[gear - 1]): 
            x = findNumberAtIndex(gear - 1, 1, firstLine, secondLine, thirdLine)
            numbers[1][0] = x
        if str.isdigit(firstLine[gear - 1]):
            x = findNumberAtIndex(gear - 1, 0, firstLine, secondLine, thirdLine)
            numbers[0][0] = x
        if str.isdigit(thirdLine[gear - 1]):
            x = findNumberAtIndex(gear - 1, 2, firstLine, secondLine, thirdLine)
            numbers[2][0] = x
        if str.isdigit(secondLine[gear + 1]):
            x = findNumberAtIndex(gear + 1, 1, firstLine, secondLine, thirdLine)
            numbers[1][2] = x
        if str.isdigit(firstLine[gear + 1]):
            x = findNumberAtIndex(gear + 1, 0, firstLine, secondLine, thirdLine)
            numbers[0][2] = x
        if str.isdigit(thirdLine[gear + 1]):
            x = findNumberAtIndex(gear + 1, 2, firstLine, secondLine, thirdLine)
            numbers[2][2] = x
        if str.isdigit(firstLine[gear]): 
            x = findNumberAtIndex(gear, 0, firstLine, secondLine, thirdLine)
            numbers[0][1] = x
        if str.isdigit(thirdLine[gear]):
            x = findNumberAtIndex(gear, 2, firstLine, secondLine, thirdLine)
            numbers[2][1]
        temp = []
        for elementList in numbers:
            for element in elementList:
                if element != -1:
                    if temp.count(element) == 0:
                        temp.append(element)
        if len(temp) > 1:
            if len(temp) > 2:
                print(f"What just happened? Temp contains {temp}")
            else:
                sum += temp[0] * temp[1]
    return sum

def bottomLine(firstLine: str, secondLine: str) -> int:
    return topLine(secondLine, firstLine)

def objectiveOne() -> int:
    sum = 0
    with open("Day3Content.txt", 'r') as file:
        fileLines = file.readlines()
        sum += topLine(fileLines[0], fileLines[1])
        for i in range(len(fileLines) - 2):
            sum += middleLine(fileLines[i], fileLines[i + 1], fileLines[i + 2])
        sum += bottomLine(fileLines[len(fileLines) - 2], fileLines[len(fileLines) - 1])
    return sum

def objectiveTwo() -> int:
    sum = 0
    with open("Day3Content.txt") as file:
        fileLines = file.readlines()
        sum += topLineGears(fileLines[0], fileLines[1])
        for i in range(len(fileLines) - 2):
            sum += middleLineGears(fileLines[i], fileLines[i + 1], fileLines[i + 2])
        sum += bottomLineGears(fileLines[len(fileLines) - 2], fileLines[len(fileLines) - 1])
    return sum


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(objectiveTwo())