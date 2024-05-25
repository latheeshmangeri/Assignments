import sys

class NimGame:
    def __init__(self, red, blue, version="standard"):
        self.red = red
        self.blue = blue
        self.version = version
        self.first_player = "computer"
        self.depth = None
        #self.points = 0

    def start_game(self, first_player="computer", depth=None):
        self.first_player = first_player
        self.depth = depth
        print("Starting game with {} marbles ({} red, {} blue) in {} version".format(self.red + self.blue, self.red, self.blue, self.version))
        if first_player == "computer":
            self.computer_turn()
        else:
            self.human_turn()

    def computer_turn(self):
        print("Computer's turn...")
        
        move_order = self.get_move_order()

        best_move = self.minimax(self.red, self.blue, move_order, maximizing_player=True, alpha=float('-inf'), beta=float('inf'))[1]
        
        if best_move[1] == 'red':
            take_red = min(best_move[0], self.red)
            self.red -= take_red
            #self.points = self.points + take_red*2
            print("Computer took {} red marbles.".format(take_red))
        else:
            take_blue = min(best_move[0], self.blue)
            self.blue -= take_blue
            #self.points = self.points + take_blue*3
            print("Computer took {} blue marbles.".format(take_blue))
        print("Red: {}, Blue: {}".format(self.red, self.blue))

        # Check if the computer loses
        if self.red == 0 or self.blue == 0:
            if self.version=='standard':
                self.end_game("Computer Wins by")
            elif self.version=='misere':
                self.end_game("You Win & Computer Loses by")
        else:
            self.human_turn()

    def minimax(self, red, blue, move_order, maximizing_player, alpha, beta):
        if red == 0 or blue == 0:
            if self.version == "standard":
                return (-1, None)  # If the opponent wins, return a loss
            else:
                return (1, None)   # If the opponent wins, return a win
        
        if maximizing_player:
            max_eval = float('-inf')
            best_move = None
            for move in move_order:
                num, color = move
                if color == 'red' and red >= num:
                    eval = self.minimax(red - num, blue, move_order, False, alpha, beta)[0]
                    if eval > max_eval:
                        max_eval = eval
                        best_move = (num, color)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
                elif color == 'blue' and blue >= num:
                    eval = self.minimax(red, blue - num, move_order, False, alpha, beta)[0]
                    if eval > max_eval:
                        max_eval = eval
                        best_move = (num, color)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            return (max_eval, best_move)
        else:
            min_eval = float('inf')
            best_move = None
            for move in move_order:
                num, color = move
                if color == 'red' and red >= num:
                    eval = self.minimax(red - num, blue, move_order, True, alpha, beta)[0]
                    if eval < min_eval:
                        min_eval = eval
                        best_move = (num, color)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
                elif color == 'blue' and blue >= num:
                    eval = self.minimax(red, blue - num, move_order, True, alpha, beta)[0]
                    if eval < min_eval:
                        min_eval = eval
                        best_move = (num, color)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return (min_eval, best_move)

    def human_turn(self):
        print("Your turn...")
        while True:
            try:
                num = int(input("Enter number of marbles to take: "))
                color = input("Enter color (red/blue): ").strip().lower()
                if color == 'red':
                    if num <= self.red:
                        self.red -= num
                        break
                elif color == 'blue':
                    if num <= self.blue:
                        self.blue -= num
                        break
                print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Check if the player loses
        if self.red == 0 or self.blue == 0:
            if self.version=='standard':
                self.end_game("You Win & Computer Loses by")
            elif self.version=='misere':
                self.end_game("Computer Wins by")
        else:
            self.computer_turn()

    def end_game(self, winner):
        if self.red == 0 and self.blue == 0:
            print("It's a tie!")
        else:
            print("\nGame Over :: {} {}\n Red:: {}, Blue:: {}".format(winner, self.red*2+self.blue*3, self.red, self.blue))

    def get_move_order(self):
        if self.version == "standard":
            if self.red > self.blue:
                return [(2, 'red'),  (2, 'blue'), (1, 'red'), (1, 'blue')]
            else:
                return [(2, 'blue'), (2, 'red'),(1, 'blue'), (1, 'red')]
        else:
            if self.red < self.blue:
                return [(2, 'red'), (1, 'red'), (2, 'blue'), (1, 'blue')]
            else:
                return [(2, 'blue'), (1, 'blue'), (2, 'red'), (1, 'red')]

def main():
    if len(sys.argv) < 3:
        print("Usage: red_blue_nim.py <num-red> <num-blue> [version] [first-player] [depth]")
        return

    red = int(sys.argv[1])
    blue = int(sys.argv[2])

    version = "standard"
    first_player = "computer"
    depth = None

    if len(sys.argv) > 3:
        version = sys.argv[3]
    if len(sys.argv) > 4:
        first_player = sys.argv[4]
    if len(sys.argv) > 5:
        depth = int(sys.argv[5])

    game = NimGame(red, blue, version)
    game.start_game(first_player, depth)

if __name__ == "__main__":
    main()
