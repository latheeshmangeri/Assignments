
# Assignment 2 - Game Playing Problems

Latheesh Mangeri


Your task is to build an agent to play two versions (standard and misère) of  the variant of a game called nim (called red-blue nim against a human player). The game consists of two piles of marbles (red and blue). On each players turn they pick a pile and remove one or two marbles from it (if possible). If on their turn, either pile is empty then they lose in the standard version and win in the misère version. The amount they lose (or win) is dependent on the number of marbles left (2 for every red marble and 3 for every blue marble). So if on the computer player turn, it has 0 red marbles and 3 blue marbles, it loses 9 points in the standard version (or wins 9 points in the misère version).  
  
Your program should be called red\_blue\_nim and the command line invocation should follow the following format:  
  
red\_blue\_nim.py &lt;num-red&gt; &lt;num-blue&gt; &lt;version&gt; &lt;first-player&gt; &lt;depth&gt;  

* &lt;num-red&gt; and &lt;num-blue&gt; are required. (Number of red and blue marbles respectively)
* &lt;version&gt; is either

* standard - Player loses if either pile empty on their turn \[default option if &lt;version&gt; is not given\]  
    
* misere - Player wins if either pile empty on their turn  
    

*  &lt;first-player&gt; can be

* computer - play a full game from given state with computer starting the game followed by human \[default option if &lt;first-player&gt; is not given\]
* human - play a full game from given state with human starting the game followed by computer

* &lt;depth&gt;  only used if depth limited search (Extra Credit) is implemented.

For a full game,  

* On Computer turn, the program should use MinMax with Alpha Beta Pruning to determine the best move to make and perform the move.

* For move ordering in standard version, use:

* Pick 2 red marble
* Pick 2 blue marble
* Pick 1 red marble
* Pick 1 blue marble

* For misère version, invert that order.  
    

* On Human turn, the program should use a prompt to get the move from the human user and perform the move.

The program should alternate between these turns till the game ends (when the players run out of either red or blue marbles). Once the game ends, calculate who won and their final score and display it to the user.  
  

### Extra Credit (20 Points):

If your program determines computer move by using depth limited MinMax search with alpha beta pruning then you will be given 20 points extra credit. You will need to come up with a eval function to use with the program also. Please submit a text file describing the reasoning behind your eval function for full credit.  


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
```bash
python red_blue_nim.py 10 10 standard computer 2
```
   
