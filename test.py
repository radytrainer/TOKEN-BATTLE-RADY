
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

def diskOnRow(diskList, rowIndex, disk):
    countDiskRed = 0
    countDiskYellow = 0
    letterR = []
    letterY = []
    for column in range(len(diskList) + 1):
        if diskList[rowIndex][column] == "R":
            letterR.append(column)
        elif diskList[rowIndex][column] == "Y":
            letterY.append(column)

    countDiskRed = counter(letterR) 
    countDiskYellow = counter(letterY)

    print(letterR)
    if countDiskRed == 4:
       # whoWinner(disk.upper(), countDiskRed)
        return True

    elif countDiskYellow == 4:
        #whoWinner(disk.upper(), countDiskYellow)
        return True
    else:
        return False

data = [
    ["Y", "Y", "Y", "R", "R", "R", "R"],
    [0, 0, 0, 0, 0, 0, 0],
    [0, "R", 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, "Y", "Y", "R", "R", "R", "R"]
]

print(diskOnRow(data, 5, "R"))

