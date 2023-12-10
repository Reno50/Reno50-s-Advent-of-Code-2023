def recursiveDerivative(array: list) -> list:
    ''' returns an array of the differences between the elements in a given array
        assumes the given array is an array of arrays
        goes all the way until it is entirely 0 or it is length 1
    >>> recursiveDerivative([[2, 2, 2]])
    [[2, 2, 2], [0, 0]]
    >>> recursiveDerivative([[0, 3, 6, 9, 12, 15]])
    [[0, 3, 6, 9, 12, 15], [3, 3, 3, 3, 3], [0, 0, 0, 0]]
    '''
    result = []
    for i in range(len(array[-1]) - 1):
        result.append(array[-1][i + 1] - array[-1][i])
    returnVal = array[:]
    returnVal.append(result)
    for val in returnVal[-1]:
        if val != 0:
            returnVal = recursiveDerivative(returnVal)
            break
    return returnVal

def buildUp(currentRow: list, previousRow: list) -> list:
    ''' This time returns the given row + 1 when given the derivative row
    >>> buildUp([2, 5, 9, 14], [3, 4, 5, 6])
    [2, 5, 9, 14, 20]
    >>> buildUp([0, 3, 6, 9, 12, 15], [3, 3, 3, 3, 3])
    [0, 3, 6, 9, 12, 15, 18]
    >>> buildUp([10, 13, 16, 21, 30, 45], [3, 3, 5, 9, 15, 23])
    [10, 13, 16, 21, 30, 45, 68]
    '''
    returnRow = currentRow[:]
    returnRow.append(currentRow[-1] + previousRow[-1])
    return returnRow

def buildBack(currentRow: list, previousRow: list) -> list:
    ''' Builds the element back, like buildUp but other side
    '''
    returnRow = currentRow[:]
    returnRow.insert(0, currentRow[0] - previousRow[0])
    return returnRow

def lastElement(array: list) -> int:
    '''Gets the next element of a given array
    >>> lastElement([0, 3, 6, 9, 12, 15])
    18
    >>> lastElement([1, 3, 6, 10, 15, 21])
    28
    >>> lastElement([10, 13, 16, 21, 30, 45])
    68
    '''
    recursive = recursiveDerivative([array[:]])
    result = [recursive[-1]]
    for i in range(len(recursive)):
        result.append(buildUp(recursive[len(recursive) - 1 - i], result[i]))
    return result[-1][-1]

def firstElement(array: list) -> int:
    recursive = recursiveDerivative([array[:]])
    result = [recursive[-1]]
    for i in range(len(recursive)):
        result.append(buildBack(recursive[len(recursive) - 1 - i], result[i]))
    return result[-1][0]

def objectiveOne():
    sumArray = []
    with open("Day9Content.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            sumArray.append(lastElement([int(i) for i in line.split()]))
    print(sum(sumArray))

def objectiveTwo():
    sumArray = []
    with open("Day9Content.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            sumArray.append(firstElement([int(i) for i in line.split()]))
    print(sum(sumArray))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    objectiveTwo()