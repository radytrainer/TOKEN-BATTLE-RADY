import Board
import logic

 def printBoard():
    rows = ""
    for row in range(len(Board.database)):
        for col in range(len(Board.database[row])):
            rows += str(Board.database[row][col]) + " "
        rows += "\n"
    return rows

isWon = True 
while isWon:
    col = int(input("Col: "))
    sign = str(input("Sign (R/Y): "))

    logic.insertGrid(Board.database, col, sign.upper())
    print(printBoard())

    if logic.diskOnRow(Board.database, len(Board.database) - 1, sign) or logic.diskOnColumn(Board.database, col, sign):
        isWon = False 
    