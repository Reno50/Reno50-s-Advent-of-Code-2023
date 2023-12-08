def cardValue(char):
    order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', "J"]
    return 13 - order.index(char)

class Hand(): # Represents a hand of cards
    def __init__(self, value: str, bid: int):
        # For part 2, comparisons are not changed but the way rank is figured out does
        self.value = value
        self.bid = bid
        self.rankedAs = 0 # High Card (Unique) = 0, One Pair = 1, Two Pair = 2, Three of a Kind = 3, Full House (2 and 3) = 4, Four of a Kind = 5, Five of a Kind = 6
        self.jUsed = False
        # MMM Yes efficiency
        onePair = False
        paired = ""
        twoPair = False
        threeOf = False
        fourOf = False
        fiveOf = False
        for char in self.value: # Could leave out the .value, __getitem__ should make it iterable anyway
            x = self.value.count(char)
            if x == 2:
                if char == paired and not twoPair:
                    onePair = True
                elif char != paired and paired != "":
                    onePair = False
                    twoPair = True
                elif paired == "":
                    paired = char
            elif x == 3:
                self.strongest = char
                threeOf = True
            elif x == 4:
                fourOf = True
            elif x == 5:
                fiveOf = True
        if onePair and not threeOf: self.rankedAs = 1
        elif twoPair: self.rankedAs = 2
        elif threeOf and not onePair: self.rankedAs = 3
        elif threeOf and onePair: self.rankedAs = 4
        elif fourOf: self.rankedAs = 5
        elif fiveOf: self.rankedAs = 6
        else: self.rankedAs = 0
        match self.rankedAs: # High Card (Unique) = 0, One Pair = 1, Two Pair = 2, Three of a Kind = 3, Full House (2 and 3) = 4, Four of a Kind = 5, Five of a Kind = 6
            case 0:
                # There can only be one J
                if self.value.count("J") == 1: self.rankedAs = 1; self.jUsed = True
            case 1:
                # There can be a pair of Js or a pair with one other J
                # Either way, rank is Three of a Kind
                if self.value.count("J") >= 1: self.rankedAs = 3; self.jUsed = True
            case 2:
                # There is two pairs, one of which could be Js, or neither is and there is one seperate J, it would be four of a kind and full house, respectively
                if self.value.count("J") == 2: self.rankedAs = 5; self.jUsed = True
                elif self.value.count("J") == 1: self.rankedAs = 4; self.jUsed = True
            case 3:
                # There is three Js or one J, four of a kind for both
                if self.value.count("J") == 3 or self.value.count("J") == 1: self.rankedAs = 5; self.jUsed = True
            case 4:
                # There can either be 2 Js or 3 Js, either way it should be five of a kind
                if self.value.count("J") >= 2: self.rankedAs = 6; self.jUsed = True
            case 5:
                # There can be one J or four Js
                if self.value.count("J") == 1: self.rankedAs = 6; self.jUsed = True
                if self.value.count("J") == 4: self.rankedAs = 6; self.jUsed = True
            case 6:
                pass
        if self.value == "JJ2JJ":
            print(f"Self.rankedAs is {self.rankedAs}")
    def __lt__(self, other):
        '''
        >>> Hand("J6233", 1) < Hand("66223", 1)
        False
        >>> Hand("T55J5", 1) < Hand("KTJJT", 1)
        True
        '''
        if self.rankedAs < other.rankedAs:
            return True
        elif self.rankedAs > other.rankedAs:
            return False
        #elif self.jUsed and not other.jUsed:
        #    return True
        #elif not self.jUsed and other.jUsed:
        #    return False
        else:
            counter = 0
            while counter < 5:
                if cardValue(self[counter]) < cardValue(other[counter]):
                    return True
                elif cardValue(self[counter]) > cardValue(other[counter]):
                    return False
                counter += 1
            return False # Because they are equal
    def __le__(self, other):
        return self < other or self == other
    def __eq__(self, other):
        if self.rankedAs < other.rankedAs:
            return False
        elif self.rankedAs > other.rankedAs:
            return False
        elif self.jUsed and not other.jUsed:
            return False
        elif not self.jUsed and other.jUsed:
            return False
        else:
            counter = 0
            while counter < 5:
                if cardValue(self[counter]) < cardValue(other[counter]):
                    return False
                elif cardValue(self[counter]) > cardValue(other[counter]):
                    return False
                counter += 1
            return True
    def __ne__(self, other):
        return not self == other
    def __gt__(self, other):
        return not self <= other
    def __ge__(self, other):
        return not self < other
    def __getitem__(self, ind):
        return self.value[ind]
    def __str__(self):
        return f"Hand({self.value}, {self.bid})"
    def __repr__(self):
        return self.__str__()

def objectiveOne():
    with open("Day7Content.txt", "r") as file:
        lines = file.readlines()
        handsDealt = []
        for line in lines:
            handsDealt.append(Hand(line.split()[0], int(line.split()[1])))
            #print(f"Card {handsDealt[-1]} was given a value of {handsDealt[-1].rankedAs}")
        handsDealt = list((sorted(handsDealt)))
        #print(handsDealt)
        result = 0
        counter = 1
        for hand in handsDealt:
            result += counter * hand.bid
            counter += 1
        print(result)

if __name__ == "__main__":
    objectiveOne()
    import doctest
    doctest.testmod()