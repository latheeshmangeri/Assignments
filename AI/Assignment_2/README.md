
# Assignment 2
## Game Playing Problems

Latheesh Mangeri - 1002116009

Programming Language:
---------------------
Python 3.9.7

Code Structure:
---------------
The code consists of a single Python script, red_blue_nim.py, which implements the Nim game. It utilizes classes to represent the game state and methods for handling player turns, Minimax algorithm with Alpha-Beta pruning for computer moves, and evaluation functions. The code also supports two versions of the game: standard and misère.

How to Run the Code:
---------------------
1. Ensure you have Python installed on your system. You can download it from https://www.python.org/downloads/.

2. Download the red_blue_nim.py file to your local machine.

3. Open a terminal or command prompt.

4. Navigate to the directory where red_blue_nim.py is located using the 'cd' command.

5. Run the code using the following command format:
   python red_blue_nim.py <num-red> <num-blue> [version] [first-player] [depth]

   - <num-red>: Number of red marbles.
   - <num-blue>: Number of blue marbles.
   - [version]: (Optional) Specify the version of the game. Available options: "standard" (default), "misere".
   - [first-player]: (Optional) Specify which player starts the game. Available options: "computer" (default), "human".
   - [depth]: (Optional) Specify the depth for Minimax algorithm with Alpha-Beta pruning. Higher depth values result in a more thorough search, but may increase computation time. Default is None (full search).

6. Follow the prompts to input moves when it's the human player's turn.

7. The game will continue until one of the players wins.

Example Usage:
--------------
To start a game with 10 red marbles and 10 blue marbles, using the standard version, with the computer starting and a depth of 2 for the Minimax algorithm:
   python red_blue_nim.py 10 10 standard computer 2
