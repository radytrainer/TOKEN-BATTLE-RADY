
import arcade
import GameLogic as logic 


SQUARE_SIZE = 30
SQUARE_COUNT = 10
MARGIN = 50
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 600
SCREEN_TITLE = "PNC Arcade tutorial"
LINE_WEIGHT = 2
OFFSET_X = 100
OFFSET_y = 70

currentPlay = logic.currentPlayer

# Print Board Circle
def printBoard():
    for i in range(0, logic.ROW_GRID):
        for j in range(0, logic.COL_GRID):
            if  logic.board[i][j] == "R": 

                arcade.draw_circle_filled(i * (SQUARE_SIZE + MARGIN) + OFFSET_X, j* (SQUARE_SIZE + MARGIN) + OFFSET_y, SQUARE_SIZE,arcade.color.YELLOW)
            elif logic.board[i][j] == "Y":

                arcade.draw_circle_filled(i * (SQUARE_SIZE + MARGIN) + OFFSET_X, j* (SQUARE_SIZE + MARGIN) + OFFSET_y, SQUARE_SIZE,arcade.color.RED)
            else:
                arcade.draw_circle_outline(i * (SQUARE_SIZE + MARGIN) + OFFSET_X,j* (SQUARE_SIZE + MARGIN) + OFFSET_y, SQUARE_SIZE, arcade.color.BLACK, LINE_WEIGHT)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        # Set up the application. This function is called only one time at the beginning
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.TEAL)

    def on_draw(self):
        # Rendering
        arcade.start_render()
        print("update")
        # Print board
        printBoard()
        arcade.draw_text(currentPlay,50, 10, arcade.color.BLACK, 14)
         
          
    def on_mouse_press(self, x, y, button, modifiers):
        # Called when the user presses a mouse button.
        #print("Click at coordinates:" + str(x) + "," + str(y))
        #print("Index:" + str(int( (x - MARGIN) / (SQUARE_SIZE + MARGIN))) + ", " + str(int( (y - MARGIN) / (SQUARE_SIZE + MARGIN))))
        columunIndex = int((x - MARGIN) / (SQUARE_SIZE + MARGIN))
        rowIndex = int((y - MARGIN) / (SQUARE_SIZE + MARGIN))
        
       # currentPlay = logic.switchPlayer()
        if logic.canPlay(columunIndex):
            logic.play(columunIndex)
    
        
        
def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
 
if __name__ == "__main__":
    main()