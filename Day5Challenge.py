import os
#This one actualy doesnt solve part 2 in any reasonable amount of time

def filterThroughMap(number: int, mapName: str, mapDeets: dict, lines: str) -> int:
    mapLines = lines[mapDeets[mapName][0]:mapDeets[mapName][0] + mapDeets[mapName][1]]
    currentNumber = int(number)
    for line in mapLines:
        dest, source, leng = [int(i) for i in line.split(" ")]
        if currentNumber in range(source, source + leng):
            currentNumber = (currentNumber - source) + dest
            break
    return currentNumber

def objectiveOne():
    mapDeets = {}
    destinations = []
    with open("Day5Content.txt", "r") as file:
        lines = file.readlines()
        mapDeets = {
            "soil": (lines.index("seed-to-soil map:\n") + 1, lines.index("soil-to-fertilizer map:\n") - lines.index("seed-to-soil map:\n") - 2),
            "fertilizer": (lines.index("soil-to-fertilizer map:\n") + 1, lines.index("fertilizer-to-water map:\n") - lines.index("soil-to-fertilizer map:\n") - 2),
            "water": (lines.index("fertilizer-to-water map:\n") + 1, lines.index("water-to-light map:\n") - lines.index("fertilizer-to-water map:\n") - 2),
            "light": (lines.index("water-to-light map:\n") + 1, lines.index("light-to-temperature map:\n") - lines.index("water-to-light map:\n") - 2),
            "temperature": (lines.index("light-to-temperature map:\n") + 1, lines.index("temperature-to-humidity map:\n") - lines.index("light-to-temperature map:\n") - 2),
            "humidity": (lines.index("temperature-to-humidity map:\n") + 1, lines.index("humidity-to-location map:\n") - lines.index("temperature-to-humidity map:\n") - 2),
            "location": (lines.index("humidity-to-location map:\n") + 1, len(lines) - 1 - lines.index("humidity-to-location map:\n"))
            } # This stores start and length of each map
        seeds = [int(i) for i in lines[0].split(":")[1].strip().split(" ")]
        counter = 0
        for seed in seeds:
            number = seed
            for key in mapDeets.keys():
                number = filterThroughMap(number, key, mapDeets, lines)
            destinations.append(number)
            counter += 1
    print(destinations)
    print(min(destinations))
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    objectiveOne()