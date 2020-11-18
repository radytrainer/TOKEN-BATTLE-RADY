
def insertGrid(grid, rowIndex, colIndex, sign):
    lastIndex = len(grid) - 1
    for row in range(len(grid)):
        for col in range(len(grid[row])):
          if grid[rowIndex][colIndex] == 0:
                grid[rowIndex][colIndex] = sign
          else:
              lastIndex -= 1
              
    return grid 


def getGrid(grid):
    rows = ""
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            rows += str(grid[row][col]) + " "
        rows += "\n"
    return rows

def whoWinner(sign, numbers):
    if sign == "R" and numbers == 4:
        print("Red Win")

    if sign == "Y" and numbers == 4:
        print("Yellow Win")

def diskOnRow(diskList, rowIndex, disk):
    countDisk = 0
    for column in range(len(diskList)):
        if diskList[rowIndex][column] == disk.upper():
            countDisk += 1
            whoWinner(disk.upper(), countDisk)
    if countDisk == 4:
        return True
    return False


def diskOnColumn(diskList, columunIndex, disk):
    countDisk = 0
    for row in range(len(diskList)):
        if diskList[row][columunIndex] == disk.upper():
            countDisk += 1
            whoWinner(disk.upper(), countDisk)
    if countDisk == 4:
        return True
    return False


    