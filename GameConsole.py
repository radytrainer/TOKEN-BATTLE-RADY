import Board
import GameLogic

def printBoard():
    rows = ""
    for row in range(len(Board.database)):
        for col in range(len(Board.database[row])):
            rows += str(Board.database[row][col]) + " "
        rows += "\n"
    print(rows)


isWon = True 
while isWon:
    col = int(input("Col: "))
    sign = str(input("Sign (R/Y): "))

    GameLogic.insertGrid(col, sign.upper())
    printBoard()

    if GameLogic.diskOnRow(Board.database, len(Board.database) - 1, sign) or GameLogic.diskOnColumn(Board.database, col, sign):
        isWon = False 
    