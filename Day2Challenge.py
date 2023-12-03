# Written to solve day 2 of the 2023 advent of code
import os

def checkGame(inputGame: str) -> bool:
    ''' Checks the given game against the maximum 
        Returns True if it exceeds maximum
        The input is in the form 1 green, 3 red, 6 blue;
        Order does not matter, as they are not ordered coherently in the file
    >>> checkGame("20 red, 2 green, 3 blue")
    True
    >>> checkGame("10 green;")
    False
    >>> checkGame("1 red, 20 blue;")
    True
    >>> checkGame("12 red, 13 green, 14 blue;")
    False
    '''
    maximum = {"red": 12, "green": 13, "blue": 14}
    for key in maximum:
        x = inputGame.find(key) # This returns the index of the last character in the key
        number = 0
        if x != -1:
            if x == 2: # This means that it is only one digit long and at the begining, so we don't want to look to early in the string
                number = int(inputGame[x-2])
            else:
                number = int(inputGame[x-3:x].lstrip()) # This deals with single digits that aren't at the beginning edge just fine
        if number > maximum[key]:
            return True
    return False # If none of the numbers are too big

def parseGame(inputGame: str) -> {"red": int, "green": int, "blue": int}:
    returnValues = {"red": 0, "green": 0, "blue": 0}
    for key in returnValues:
        x = inputGame.find(key) # This returns the index of the last character in the key
        number = 0
        if x != -1:
            if x == 2: # This means that it is only one digit long and at the begining, so we don't want to look to early in the string
                number = int(inputGame[x-2])
            else:
                number = int(inputGame[x-3:x].lstrip()) # This deals with single digits that aren't at the beginning edge just fine
            returnValues[key] = number
    return returnValues

def parseLine(inputLine: str) -> (bool, int):
    '''Input is a line from the file, chops it up into games and uses checkGame on each
        Again, returns True if it exceeds the max
    >>> parseLine("Game 2: 2 red, 50 blue, 10 green; 15 green, 20 red; 205 blue")
    (True, 2)
    >>> parseLine("Game 45: 5 blue")
    (False, 45)
    >>> parseLine("Game 33: 6 green, 2 blue, 2 red; 1 red, 3 green, 7 blue; 9 blue, 1 green; 10 blue, 1 green, 1 red; 8 blue, 4 red, 6 green; 1 green, 2 red, 7 blue")
    (False, 33)
    >>> parseLine("Game 6: 1 green, 4 red; 1 blue, 19 red, 5 green; 15 red, 1 green, 1 blue; 8 green, 12 red; 19 green, 7 red; 2 blue, 14 red, 12 green")
    (True, 6)
    '''
    gameNumber = inputLine[:].split(":")[0]
    gameRemovedInput = inputLine[:].split(":")[1]
    gameArray = gameRemovedInput.split(";")
    lineNumber = int(gameNumber[5:])
    for i in range(len(gameArray)):
        if checkGame(gameArray[i]):
            return (True, lineNumber)
    return (False, lineNumber)

def powerPerLine(inputLine: str) -> int:
    '''Given a line from the file, get the maximum values over all the games in the line and multiply them together
    >>> powerPerLine("Game 1: 2 red, 3 blue, 5 green")
    30
    >>> powerPerLine("Game 2: 4 red, 5 green; 6 red, 7 blue;")
    210
    '''
    gameNumber = inputLine[:].split(":")[0]
    gameRemovedInput = inputLine[:].split(":")[1]
    gameArray = gameRemovedInput.split(";")
    lineNumber = int(gameNumber[5:])
    maximumValues = {"red": 0, "green": 0, "blue": 0}
    for i in range(len(gameArray)):
        x = parseGame(gameArray[i])
        for key in x:
            if x[key] > maximumValues[key]:
                maximumValues[key] = x[key]
    return maximumValues["red"] * maximumValues["blue"] * maximumValues["green"]


def firstObjective() -> int:
    sum = 0
    with open("Day2Content.txt", 'r') as file:
        for line in file:
            x = parseLine(line)
            if not x[0]:
                sum += x[1]
    return sum

def secondObjective() -> int:
    sum = 0
    with open("Day2Content.txt", 'r') as file:
        for line in file:
            sum += powerPerLine(line)
    return sum


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(firstObjective())
    print(secondObjective())