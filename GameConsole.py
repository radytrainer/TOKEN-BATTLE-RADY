import Board

def main():

    whoStartFirst = str(input("Who start first? (R/Y) : "))
    start = Board.getPlayerStartFirst(whoStartFirst)

    isWin = True
    isPlayed = False
    boardColumnHeader = "\nA B C D E F G \n"
    boardWelcomeMessage = "\nWELCOME TO DISK-BATTLE!\n"
    boardUpdates = []
    while isWin:
        

        if start and not isPlayed:
            playerInput = eval(input("Player RED, Enter column to play: "))
            isPlayed = True

        else:
            playerInput = eval(input("Player YELLOW, Enter column to play: "))
            isPlayed = False
            start = True
        
        
        boardUpdates.append(playerInput)

        # Write your code here !
        result=""
        BOARD_ROWS = 6
        BOARD_COLUMNS = 7

        for row in range(BOARD_ROWS):
            for column in range(BOARD_COLUMNS):
                if Board.hasDiskOnCell(boardUpdates, row, column):
                    character = "R "
        
                else:
                    character = "0 "
                
                result+=character
            result+="\n"

        print(boardWelcomeMessage + boardColumnHeader + result)   


main()