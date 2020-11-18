import Board
import logic

isWon = True 
while isWon:

    row = int(input("Row: "))
    col = int(input("Col: "))
    sign = str(input("Sign: "))

    logic.insertGrid(Board.data, row, col, sign.upper())
    print(logic.getGrid(Board.data))

    if logic.diskOnRow(Board.data, row, sign) or logic.diskOnColumn(Board.data, col, sign):
        isWon = False 
    