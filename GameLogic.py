import Board

def insertGrid(colIndex, sign):
    lastIndex = len(Board.database) - 1
    added = False
    if colIndex < Board.COL_GRID and sign == "R" or sign == "Y":
        for i in range(len(Board.database)):
            if Board.database[lastIndex - i][colIndex] == 0 and not added:
                Board.database[lastIndex - i][colIndex] = sign
                added = True    

    return Board.database 


def whoWinner(sign, numbers):
    if sign == "R" and numbers >= 4:
        print("Red Win")

    if sign == "Y" and numbers >= 4:
        print("Yellow Win")

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
    if len(letterR) > 0:
        countDiskRed = counter(letterR) 
    if len(letterY) > 0:
        countDiskYellow = counter(letterY)

    if countDiskRed >= 4:
        whoWinner(disk.upper(), countDiskRed)
        return True

    elif countDiskYellow >= 4:
        whoWinner(disk.upper(), countDiskYellow)
        return True
    else:
        return False


def diskOnColumn(diskList, columunIndex, disk):
    countDisk = 0
    if columunIndex < Board.COL_GRID:
        for row in range(len(diskList)):
            if diskList[row][columunIndex] == disk.upper():
                countDisk += 1
    if countDisk == 4:
        whoWinner(disk.upper(), countDisk)
        return True
    return False


    