import GameLogic


def getColumnInput(letter):
    if letter.upper == "A":
        columnIndex = 0
    elif letter.upper == "B":
        columnIndex = 1
    elif letter.upper == "C":
        columnIndex = 2
    elif letter.upper == "D":
        columnIndex = 3
    elif letter.upper == "E":
        columnIndex = 4
    elif letter.upper == "F":
        columnIndex = 5
    elif letter.upper == "G":
        columnIndex = 6

def printBoard():
    rows = "A B C D E F G \n"
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
    