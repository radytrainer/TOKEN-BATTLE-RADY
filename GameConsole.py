import Board
import logic

isWon = True 
while isWon:
    col = int(input("Col: "))
    sign = str(input("Sign: "))

    logic.insertGrid(Board.data, col, sign.upper())
    print(logic.getGrid(Board.data))

    if logic.diskOnRow(Board.data, len(Board.data) - 1, sign) or logic.diskOnColumn(Board.data, col, sign):
        isWon = False 
    