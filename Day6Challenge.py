# distance traveled = d = b*(t-b) where b is time spent pressing button and t is total
# 2 ms = 1 mm
# 3 ms = 2 mm, 2 mm
# 4 ms = 3 mm, 4 mm, 3 mm
# 5 ms = 4 mm, 6 mm, 6 mm, 4 mm
# 6 ms = 5 mm, 8 mm, 9 mm, 8 mm, 5 mm
# 7 ms = 6 mm, 10 mm, 12 mm, 12 mm, 10 mm, 6 mm
# 8 ms = 7 mm, 12 mm, 15 mm, 16 mm, 15 mm, 12 mm, 7 mm
# 9 ms = 8 mm, 14 mm, 18 mm, 20 mm, 20 mm, 18 mm, 14 mm, 8 mm
# 10 ms = 9 mm, 16 mm, 21 mm, 24 mm, 25 mm, 24 mm, 21 mm, 16 mm, 9 mm

def objectiveOne():
    with open("Day6Content.txt", "r") as file:
        lines = file.readlines()
        times = [int(i) for i in lines[0].split(":")[1].strip().split()]
        distances = [int(i) for i in lines[1].split(":")[1].strip().split()]
        recordOptions = 1 # Assumes we will at least beat one record
        counter = 0
        for time in times:
            records = 0
            for i in range(time):
                if ((i * (time - i)) - distances[counter]) > 0:
                    records += 1
            counter += 1
            print(f"{time} had a number of records {records}")
            recordOptions = recordOptions * records # records should never be zero, or else how would they have gotten the record??
        print(recordOptions)

def objectiveTwo():
    counter = 0
    with open("Day6Content.txt", "r") as file:
        lines = file.readlines()
        time = int(lines[0].split(":")[1].strip().replace(" ", ""))
        dist = int(lines[1].split(":")[1].strip().replace(" ", ""))
        for i in range(time):
            if ((i * (time - i)) - dist) > 0:
                counter += 1
    print(counter)
if __name__ == "__main__":
    #objectiveOne()
    objectiveTwo()