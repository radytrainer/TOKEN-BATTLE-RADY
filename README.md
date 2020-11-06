# THE DISKS BATTLE
## PRESENTATION OF THE GAME
Objective: Connect four of your disks in a row while preventing your opponent from doing the same. But,
look out -- your opponent can sneak up on you and win the game!

DEMO: https://lululataupe.com/jeux-tablettes/tout-age/puissance-4/

### RULES
1. Game start with an empty game board
2. The 2 players alternatively drop one of their disk into an unfilled column
3. The first player who can connect 4 disk horizontally, vertically or in diagonal, win
4. Note: If the board fills up before either player achieves four in a row, then the game is a draw

### BOARD
The board is a grid of 7 columns and 6 rows

## ARCHITECTURE 
We want to separate the game data and functions, from the interaction in
- In console in a first step
- Using a graphical library (Arcade Python) in a second step 

Therefore:
- Usage of console (get player actions and display the board and messages) should be only located in
GameCOnsole.py
- Use of graphical interface ( get mouse events, display the board, display messages) should be only located in
Game2D.py
- The data (current status of the board) and functions to play (clear the board, add a disk to a column, see how is
winning..) should be only located in Board.py


