import Board

def insertGrid(grid, colIndex, sign):
    lastIndex = len(grid) - 1
    added = False
    if colIndex < Board.COL_GRID and sign == "R" or sign == "Y":
        for i in range(len(grid)):
            if grid[lastIndex - i][colIndex] == 0 and not added:
                grid[lastIndex - i][colIndex] = sign
                added = True    

    return grid 


def whoWinner(sign, numbers):
    if sign == "R" and numbers == 4:
        print("Red Win")

    if sign == "Y" and numbers == 4:
        print("Yellow Win")

def diskOnRow(diskList, rowIndex, disk):
    countDiskRed = 0
    countDiskYellow = 0
    letters = []
    for column in range(len(diskList)):
        if diskList[rowIndex][column] == "R" or diskList[rowIndex][column] == "Y":
            letters.append(diskList[rowIndex][column])
        
    for i in range(len(letters)):
        if letters[i] == "R":
            countDiskRed += 1
        else:
            countDiskYellow += 1
            
    if countDiskRed == 4 and countDiskYellow == 0:
        whoWinner(disk.upper(), countDiskRed)
        return True

    elif countDiskYellow == 4 and countDiskRed == 0:
        whoWinner(disk.upper(), countDiskYellow)
        return True

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


    