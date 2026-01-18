# tic-tac-toe
a basic game of tic-tac-toe where canvas size increases with the increasing levels. 

1. start with a 4x4 canvas 

2. obstacles spawn at random chunks in available canvas

3. if the user reaches the target point specified, the level is a "success"

4. in case of a *draw* or *loss* in the current level, 
a new canvas can be generated for teh same level using "(reload symbol)" button.

optionally, the user can be sent back to a canvas of previous level in case of a *loss*
that is (n)x(n) --> (n-1)x(n-1)

5. in case of a *success* : 
  a. passing a stage increases a row and a column
  b. the size(px) of grid may be adjusted(decreased) with the increase in number of cells in the grid

6. the session ends when user interacts with "close (cross symbol)" button
