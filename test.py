def diskOnRow(diskList, rowIndex, disk):
    countDiskRed = 0
    countDiskYellow = 0
    letters = []
    for column in range(len(diskList)):
        if diskList[rowIndex][column] == "R" or diskList[rowIndex][column] == "Y":
            letters.append(diskList[rowIndex][column])
    
    print(letters)
    for i in range(len(letters)):
        if letters[i] == "R":
            countDiskRed += 1
        else:
            countDiskRed = 0

        if letters[i] == "Y" and not countDiskYellow != 4:
            countDiskYellow += 1
        else:
            countDiskYellow = 0
    print(countDiskRed)
    if countDiskRed == 4 and countDiskYellow == 0:
       # whoWinner(disk.upper(), countDiskRed)
        return True

    elif countDiskYellow == 4 and countDiskRed == 0:
        #whoWinner(disk.upper(), countDiskYellow)
        return True

    return False

data = [
        [0, "R", "R", "R", "R", "Y", 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
]

print(diskOnRow(data, 0, "R"))