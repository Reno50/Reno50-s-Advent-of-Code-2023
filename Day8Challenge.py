import math
# I know, using a dictionary would literally be so much easier
# Silly me implemented all of Node before I realized it wouldn't have been harder

class Node():
    def __init__(self, line: str) -> None:
        value = line[0:3]
        left = line[7:10]
        right = line[12:15]
        self.left = left
        self.right = right
        self.val = value
    def left(self) -> str:
        return self.left
    def right(self) -> str:
        return self.right
    def __lt__(self, other):
        return self.val < other.val
    def __eq__(self, other):
        if type(other) == None: return False
        return self.val == other.val
    def __le__(self, other):
        return self.val <= other.val
    def __gt__(self, other):
        return self.val > other.val
    def __ge__(self, other):
        return self.val >= other.val
    def __ne__(self, other):
        return self.val != other.val
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return self.val
def objectiveOne():
    with open("Day8Content.txt", "r") as file:
        lines = file.readlines()
        instructions = lines[0].strip()
        currentPath = ""
        network = []
        for line in lines[2:]:
            network.append(Node(line))
        network.sort()
        beginning = findInNetwork("AAA", network)
        current = beginning
        index = 0
        counter = 0
        while current.val != "ZZZ":
            currentPath += str(current) + "->"
            counter += 1
            #print(index)
            nextInstruction = instructions[index]
            if nextInstruction == "L":
                current = findInNetwork(current.left, network)
                #print(f"Looked left for {current}")
            else:
                current = findInNetwork(current.right, network)
                #print(f"Looked right for {current}")
            if index < len(instructions) - 1: index += 1
            else: index = 0
        print(counter)
        
def objectiveTwo():
    with open("Day8Content.txt", "r") as file:
        lines = file.readlines()
        instructions = lines[0].strip()
        beginnings = []
        network = []
        for line in lines[2:]:
            network.append(Node(line))
        #network.sort() ? why does this change anything wtf?
        for node in network:
            if node.val[2] == "A":
                beginnings.append(node)
        current = beginnings[:]
        index = 0
        counter = [0 for i in range(len(beginnings))]
        for i in range(len(beginnings)):
            while current[i].val[2] != "Z":
                counter[i] += 1
                nextInstruction = instructions[index]
                if nextInstruction == "L":
                    current[i] = findInNetwork(current[i].left, network)
                else:
                    current[i] = findInNetwork(current[i].right, network)
                if index < len(instructions) - 1: index += 1
                else: index = 0
        print(counter)
        print(math.lcm(*(counter)))

def findInNetwork(item: str, network: list) -> Node:
    currentItem = network[0]
    index = 0
    while currentItem.val != item:
        currentItem = network[index]
        index += 1
    return currentItem

objectiveTwo()