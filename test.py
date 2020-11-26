board = [
    ["Y", "Y", "R", "R", "R", "Y"], 
    ["R", "0", "R", "R", "R", "Y"], 
    ["T", "R", "0", "0", "R", "Y"], 
    ["R", "R", "0", "0", "0", "Y"], 
    ["R", "0", "R", "R", "R", "Y"], 
    
]

def getMaximunConsecutiveNumbers(numbers):
    count = 1
    isGreaterThan4 = False
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

   

def isSignWon(sign) :
    
    for row in range(len(board)):
        if isSignWonOnRow(row,sign):
            return True
    for row in range(len(board)):
        for col in range(len(board[row])):
            if isSignWonOnColumn(col,sign):
                return True
    return False

print(isSignWon("Y"))