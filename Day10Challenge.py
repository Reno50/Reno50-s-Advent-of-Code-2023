lines = []
with open("Day10Content.txt", "r") as file:
    lines = file.readlines()

# Directions are defined as 0 = North, 1 = East, 2 = South, 3 = West

def nextPipe(direction: int, currentLocation: [int, int]) -> str:
    # currentLocation is defined as [y, x] since that is how lines of the file work
    # North is technically the row index - 1 because the file is 0 at the top
    match direction:
        case 0:
            return lines[currentLocation[0] - 1][currentLocation[1]]
        case 1:
            return lines[currentLocation[0]][currentLocation[1] + 1]
        case 2:
            return lines[currentLocation[0] + 1][currentLocation[1]]
        case 3:
            return lines[currentLocation[0]][currentLocation[1] - 1]
        
def pathLength(direction: int, startLocation: [int, int], debug=False) -> int:
    # same conventions as nextPipe
    # Finds the length of the path back to start location, -1 if it fails
    nextSpot = ""
    counter = 0
    nextDir = direction
    nextLocation = startLocation
    breakTime = len(lines) * len(lines[0])
    while counter <= breakTime:
        nextSpot = nextPipe(nextDir, nextLocation)
        if nextDir == 0:
            nextLocation = [nextLocation[0] - 1, nextLocation[1]]
        elif nextDir == 1:
            nextLocation = [nextLocation[0], nextLocation[1] + 1]
        elif nextDir == 2:
            nextLocation = [nextLocation[0] + 1, nextLocation[1]]
        else:
            nextLocation = [nextLocation[0], nextLocation[1] - 1]
        # This match is to get the right direction, or if it finds something that breaks the path
        match nextSpot:
            case "|":
                if nextDir % 2 == 1:
                    if debug: print("Ran into a wall")
                    return -1 # Coming from east or west doesn't work
            case "-":
                if nextDir % 2 == 0:
                    if debug: print("Ran into a horizontal wall")
                    return -1 # Coming from north or south doesn't work
            case "L":
                if nextDir == 2:
                    nextDir = 1
                elif nextDir == 3:
                    nextDir = 0
                else:
                    if debug: print(f"Ran into an L at {nextLocation} facing {nextDir}")
                    return -1
            case "J":
                if nextDir == 2:
                    nextDir = 3
                elif nextDir == 1:
                    nextDir = 0
                else:
                    if debug: print(f"Ran into a J at {nextLocation} facing {nextDir}")
                    return -1
            case "7":
                if nextDir == 1:
                    nextDir = 2
                elif nextDir == 0:
                    nextDir = 3
                else:
                    if debug: print(f"Ran into a 7 at {nextLocation} facing {nextDir}")
                    return -1
            case "F":
                if nextDir == 3:
                    nextDir = 2
                elif nextDir == 0:
                    nextDir = 1
                else:
                    if debug: print(f"Ran into an F at {nextLocation} facing {nextDir}")
                    return -1
            case ".":
                if debug: print(f"Ran into a dot at {nextLocation}")
                return -1
            case "S":
                if debug: print("Hooray!")
                return counter # Perhaps add one here? I don't know for sure though
        counter += 1
    if debug: print("Breaktime was hit")
    return -1 # Breaktime was hit

def objectiveOne():
    startPoint = []
    yCount = 0
    x = 0
    for line in lines:
        x = line.count('S')
        if x != 0:
            break
        yCount += 1
    startPoint = [yCount, lines[yCount].index("S")]
    paths = []
    for i in range(4):
        paths.append((pathLength(i, startPoint) // 2) + 1)
    print(max(paths))

if __name__ == "__main__":
    objectiveOne()