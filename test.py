board = [
    ["Y", "Y", "R", "R", "R", "Y"], 
    ["R", "R", "R", "R", "R", "Y"], 
    ["T", "R", "R", "R", "R", "Y"], 
    ["R", "R", "R", "R", "R", "Y"], 
    ["R", "Y", "R", "R", "R", "Y"], 
    
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

print(isSignWonOnColumn(0, "R"))