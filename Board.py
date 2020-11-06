
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

