
def counter(listIndex):
    firstIndex = listIndex[0]
    count = 0
    for i in range(len(listIndex)):
        if firstIndex == listIndex[i] - 1 or firstIndex == listIndex[i]:
            firstIndex = listIndex[i]
            count += 1
        else:
            firstIndex = listIndex[i]
    return count 



def diskOnColumn(diskList, columunIndex, disk):
    countDiskRed = 0
    countDiskYellow = 0
    letterR = []
    letterY = []
    for row in range(len(diskList)):
        if diskList[row][columunIndex] == "R":
            letterR.append(row)
        elif diskList[row][columunIndex] == "Y":
            letterY.append(row)

    if len(letterR) > 0:
        countDiskRed = counter(letterR) 
    if len(letterY) > 0:
        countDiskYellow = counter(letterY)

    print(letterY)
    if countDiskRed >= 4:
       # whoWinner(disk.upper(), countDiskRed)
        return True

    elif countDiskYellow >= 4:
        #whoWinner(disk.upper(), countDiskYellow)
        return True
    else:
        return False

data = [
    ["Y", "Y", "Y", "R", "R", "R", "R"],
    ["Y",  0,   0,    0,   0,   0,  0],
    ["R", "R",  0,    0,   0,   0,  0],
    ["R", "R",  0,    0,   0,   0,  0],
    ["R",  0,  "R",   0,   0,   0,  0],
    ["R", "Y", "R", "Y", "Y", "R", "R"]
]

print(diskOnColumn(data, 0, "R"))

