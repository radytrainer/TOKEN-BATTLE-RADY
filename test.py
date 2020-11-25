board = [
    ["0", "R", "0", "0", "0"],
    ["0", "R", "0", "0", "0"],
    ["0", "R", "0", "0", "0"],
    ["R", "R", "0", "0", "0"],
    ["R", "R", "0", "0", "0"],
]

def getRowIndexFor(column) :
    indexOf = -1
    for index in range(len(board)):
        if board[index][column] == "0":
            indexOf = index
    if indexOf >= 0:
        return indexOf
    return -1

print(getRowIndexFor(1))

