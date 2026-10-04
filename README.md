# Unbeatable Tic-Tac-Toe AI

A Tic-Tac-Toe game where you play against an AI that uses the **Minimax algorithm**. Built with Python and Tkinter.

You play as **X** and the computer plays as **O**.

## Features

- Play against an AI opponent
- Simple graphical interface with a 3×3 board
- Minimax algorithm for smart decision making
- Win, lose and draw detection
- Restart button to play again

## Technologies Used

- Python
- Tkinter
- Minimax Algorithm

## How to Run

1. Make sure Python is installed on your computer.
2. Download or clone this repository.
3. Open the project folder in a terminal.
4. Run the command:

   py tic_tac_toe.py

## How It Works

The game uses the **Minimax algorithm**, a decision-making technique used in two-player games.

1. **Player move:** You click a cell and an **X** is placed on the board.
2. **Result check:** The program checks if someone has won or if the board is full (draw).
3. **Computer thinks:** If the game is not over, the computer tries every empty cell. For each one, it simulates all the possible moves that could follow until the game ends.
4. **Scoring:** Every possible ending gets a score:
   - Computer (O) wins: **+1**
   - Player (X) wins: **-1**
   - Draw: **0**
5. **Best move:** The computer assumes you will also play your best. It picks the move with the highest score and places an **O**.
6. **Repeat:** The game continues until someone wins or it ends in a draw. A message box shows the result, and the board resets for a new game.

Because the computer looks at every possible future outcome, it never makes an avoidable losing move. The best result you can get against it is a draw.

## Project Info

- **Domain:** Artificial Intelligence
