import GameLogic as logic


def printBoard():
    rows = ""
    for row in range(len(logic.board)):
        for col in range(len(logic.board[row])):
            rows += str(logic.board[row][col]) + " "
        rows += "\n"
    print(rows)

while logic.getBoardStatus() == logic.ON_GOING:
    printBoard()

   # Get current player
    currentPlay = logic.switchPlayer()

    #Get Column index
    columunIndex = int(input(currentPlay + " Enter your column: "))

    if logic.isBoardColumFull(columunIndex):
        print("This column are full try other column!")

    #Check if can play on the column
    if logic.canPlay(columunIndex):
        logic.play(columunIndex)
    
    
    

if logic.getBoardStatus() == logic.YELLOW_WON:
    print("YELLOW PLAER IS WINNER")
elif logic.getBoardStatus() == logic.RED_WON:
    print("RED PLAYER IS WINNER")
else:
    print("BOARD FULL")

