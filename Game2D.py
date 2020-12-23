

import arcade
import GameLogic as logic 


SQUARE_SIZE = 30
SQUARE_COUNT = 10
MARGIN = 50
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 600
SCREEN_TITLE = "PNC Arcade tutorial"
LINE_WEIGHT = 2


currentPlay = logic.currentPlayer
# Print Board Circle
def printBoard():
    for i in range(1, logic.ROW_GRID + 2):
        for j in range(1, logic.COL_GRID + 1):
            arcade.draw_circle_outline(i * (SQUARE_SIZE + MARGIN),j* (SQUARE_SIZE + MARGIN), SQUARE_SIZE, arcade.color.BLACK, LINE_WEIGHT)

class MyGame(arcade.Window):
 
    def __init__(self, width, height, title):
        # Set up the application. This function is called only one time at the beginning
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.TEAL)

    def on_draw(self):
        # Rendering
        arcade.start_render()
        # Print board
        printBoard()
        arcade.draw_text(currentPlay,50, 20, arcade.color.BLACK, 14)
             
          
    def on_mouse_press(self, x, y, button, modifiers):
        # Called when the user presses a mouse button.
        print("Click at coordinates:" + str(x) + "," + str(y))
        print("Index:" + str(int( (x - MARGIN) / (SQUARE_SIZE + MARGIN))) + ", " + str(int( (y - MARGIN) / (SQUARE_SIZE + MARGIN))))
        currentPlay = logic.switchPlayer()
       
        
def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
 
if __name__ == "__main__":
    main()