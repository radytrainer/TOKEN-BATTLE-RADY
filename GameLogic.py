
ROW_GRID = 6
COL_GRID = 7

# CONSTANT
RED_PLAYER = "RED_PLAYER"
YELLOW_PLAYER = "YELLOW_PLAYER"

RED_WON = "RED_WON"
YELLOW_WON= "YELLOW_WON"
BOARD_FULL = "BOARD_FULL"
ON_GOING = "ON_GOING"


#  empty  cell = "0"
#  red  cell = "Y"
#  yellow   cell = "R"
def createBoard() :
    result = []
    for row in range(ROW_GRID):
        result.append([])

    for row in range(len(database)):
        for col in range(COL_GRID):
            result[row].append("0")

    return result



board = createBoard()

currentPlayer  = RED_PLAYER


def switchPlayer() :
    global currentPlayer

    if currentPlayer ==  RED_PLAYER:
        currentPlayer = YELLOW_PLAYER
    else :
        currentPlayer = RED_PLAYER




#
# Reset the board with no disks
#
def resetBoard() :
    global board
    board = createBoard()


# @param  column : the column index
# @return  the mrow index to drop the disk or -1 if the column is full
def getRowIndexFor(column) :
    return 0   # TODO

# @param  column : the column index
# @return  True if it s possible to drop a disk on column
def canPlay(column):
    return  getRowIndexFor(column) != -1


def play(column):
    global board

    # Get the row at this column
    row = getRowIndexFor(column)

    # Get the sign for currentplayer
    if currentPlayer ==  RED_PLAYER:
        sign = "R"
    else :
        sign = "Y"

    # UPdate  the board
    board[row][column] = sign

    # Siztch player
    switchPlayer() 


def isBoardFull():
    return False # TODO

def isSignWOn(sign) :
    return False



# @return the status of the board (red winm yellow winm on going etc..)
def getBoardStatus() :

    # 1 Check if board if full
    boardFull = isBoardFull()

    # 2 Check if YELLOW  won
    yelloWon = isSignWOn("Y")

    # 3 Check if RED won

    return ON_GOING     # TODO

#
# @papram list of numbers
# Count the  maximun consecutive list of numbers
#
def getMaximunConsecutiveNumbers(numbers):
    count = 0

    if len(numbers)> 0 :
        for i in range(1, len(numbers)):
            currentValue = numbers[i] 
            previousValue = numbers[i-1]

            if  currentValue == previousValue  + 1 :
                count += 1
            else 
                count = 0

    return count 


def isSignWonOnRow(rowIndex, sign):

    #  1 - Get the indexes for this sign
    signIndexes = []
    for column in range(len(board) + 1):
        if board[rowIndex][column] ==sign:
            signINdexes.append(column)

    # @ - Count the max list of consecutive index
    mqxCOnsecutive = getMaximunConsecutiveNumbers(signIndexes)

    t# Sign has won is more than 4 consecutive index
    return mqxCOnsecutive> = 4

   

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

    if countDiskRed >= 4:
        whoWinner(disk.upper(), countDiskRed)
        return True

    elif countDiskYellow >= 4:
        whoWinner(disk.upper(), countDiskYellow)
        return True
    else:
        return False
