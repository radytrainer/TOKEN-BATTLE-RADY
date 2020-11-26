
ROW_GRID = 6
COL_GRID = 7

# CONSTANT
RED_PLAYER = "RED_PLAYER"
YELLOW_PLAYER = "YELLOW_PLAYER"

# Status
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

    for row in range(len(result)):
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
# @return  the row index to drop the disk or -1 if the column is full
def getRowIndexFor(column) :
    indexOf = -1
    for index in range(len(board)):
        if board[index][column] == "0":
            indexOf = index
    if indexOf >= 0:
        return indexOf
    return -1


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
    counter = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "0":
                counter += 1
    if counter > 0:
        return False 
    return True
#
# @papram list of numbers
# Count the  maximun consecutive list of numbers
#
def getMaximunConsecutiveNumbers(numbers):
    count = 1
    if len(numbers)> 0 :
        for i in range(1, len(numbers)):
            currentValue = numbers[i] 
            previousValue = numbers[i-1]

            if  currentValue == previousValue  + 1:
                count += 1
                if count >= 4:
                    return count
            else:
                count = 1
    return count


def isSignWonOnRow(rowIndex, sign):

    #  1 - Get the indexes for this sign
    signIndexes = []
    for column in range(len(board)):
        if board[rowIndex][column] == sign:
            signIndexes.append(column)

    # @ - Count the max list of consecutive index
    maxCOnsecutive = getMaximunConsecutiveNumbers(signIndexes)

    # Sign has won is more than 4 consecutive index
    return maxCOnsecutive >= 4

   

def isSignWonOnColumn(columunIndex, sign):
    #  1 - Get the indexes for this sign
    signIndexes = []
    for row in range(len(board)):
        if board[row][columunIndex] == sign:
            signIndexes.append(row)

    # @ - Count the max list of consecutive index
    maxCOnsecutive = getMaximunConsecutiveNumbers(signIndexes)

    # Sign has won is more than 4 consecutive index
    return maxCOnsecutive >= 4

def isSignWon(sign) :
    
    for row in range(len(board)):
        if isSignWonOnRow(row,sign):
            return True
    for row in range(len(board)):
        for col in range(len(board[row])):
            if isSignWonOnColumn(col,sign):
                return True
    return False



# @return the status of the board (red winm yellow winm on going etc..)
def getBoardStatus() :
    status = ""
    # 1 Check if board if full
    boardFull = isBoardFull()

     # 2 Check if YELLOW  won
    yellowWon = isSignWon("Y")

    # 3 Check if RED won
    redWon = isSignWon("R")

    if boardFull:
        status = BOARD_FULL
    elif yellowWon:
        status = YELLOW_WON
    elif redWon:
        status = RED_WON
    else:
        status = ON_GOING
   
    return status   
print(getBoardStatus())

