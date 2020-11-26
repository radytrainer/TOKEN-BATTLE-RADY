board = [
    ["R", "Y", "R", "R", "R"], 
    ["R", "R", "R", "R", "R"], 
    ["R", "R", "R", "R", "R"], 
    ["R", "R", "R", "R", "R"], 
    ["R", "R", "R", "R", "R"]
]

def isBoardFull():
    counter = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "0":
                counter += 1
    if counter > 0:
        return False 
    return True

print(isBoardFull())

