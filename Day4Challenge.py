# This seems to be a very inefficient way to do this problem
# There is certainly many better ways to do this, this is just the first way I thought of

import os

def cardValue(card: str) -> int:
    '''Returns the value of a given scratch card
    >>> cardValue("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
    8
    '''
    pieces = [card.split(":")[0], card.split(":")[1].split("|")[0], card.split(":")[1].split("|")[1]]
    winningNumbers = [number for number in pieces[1].split(" ")]
    cardNumbers = [number for number in pieces[2].split(" ")]
    while winningNumbers.count("") != 0:
        winningNumbers.remove("")
    while cardNumbers.count("") != 0:
        cardNumbers.remove("")
    value = 0
    winningNumbers = [int(num) for num in winningNumbers]
    cardNumbers = [int(num) for num in cardNumbers]
    for element in cardNumbers:
        if element in winningNumbers:
            if value == 0:
                value += 1
            else:
                value = value * 2
    return value

def matchingValues(card: str) -> int:
    '''Returns the number of matching numbers of a given scratch card
    >>> matchingValues("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
    4
    '''
    pieces = [card.split(":")[0], card.split(":")[1].split("|")[0], card.split(":")[1].split("|")[1]]
    winningNumbers = [number for number in pieces[1].split(" ")]
    cardNumbers = [number for number in pieces[2].split(" ")]
    while winningNumbers.count("") != 0:
        winningNumbers.remove("")
    while cardNumbers.count("") != 0:
        cardNumbers.remove("")
    value = 0
    winningNumbers = [int(num) for num in winningNumbers]
    cardNumbers = [int(num) for num in cardNumbers]
    for element in cardNumbers:
        if element in winningNumbers:
            value += 1
    return value

def objectiveTwo() -> int:
    # Forgot to keep objective 1 intact, oops
    # It is quite simple though, just add up cardValue() for each line
    sum = 0
    cards = []
    with open("Day4Content.txt", 'r') as file:
        done = False
        lines =  file.readlines()
        for i in range(len(lines)):
            cards.append(1) # Initializes cards as having one of each card
        indexCounter = 0 # This is the card number
        for card in cards: # For each card number
            for i in range(card): # For each card of this number
                for j in range(matchingValues(lines[indexCounter])): # For the value of the card, i.e. if card 1 is 4 the next 4 cards each get +1 copy
                    if indexCounter + j + 1 < len(lines):
                        cards[indexCounter + j + 1] += 1
                sum += 1 # Adds to sum each card of this number
            indexCounter += 1

    return sum

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(objectiveTwo())