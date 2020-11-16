BOARD_ROWS = 6
BOARD_COLUMNS = 7

def hasDiskOnCell (disksPositions, cellX, cellY):
    hasDisk = False
    if (cellX > 5 and cellY > 5) and (cellX < 0 and cellY < 0):
        hasDisk = False
    else: 
        for disk in disksPositions:
            if disk[0] == cellX and disk[1] == cellY :
                hasDisk = True
    return hasDisk


def getPlayerStartFirst(message):
    hasStart = False
    if message.upper() == "R":
        hasStart = True
    return hasStart


def diskOnRow(diskList, rowIndex, disk):
    countDisk = 0
    for column in range(len(diskList)):
        if diskList[rowIndex][column] == disk:
            countDisk += 1
    if countDisk == 4:
        return True
    return False


def diskOnColumn(diskList, columunIndex, disk):
     countDisk = 0
    for row in range(len(diskList)):
        if diskList[row][columunIndex] == disk:
            countDisk += 1
    if countDisk == 4:
        return True
    return False


def diskDiamontionl(diskList, disk):
    return False

