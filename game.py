from player import HumanPlayer, GeniusComputerPlayer, RandomComputerPlayer  # Import player classes from player.py
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Initialize board with empty spaces
        self.current_winner = None  # Track current winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # Print board with numbers indicating positions
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # Return list of available moves (indices with ' ')
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        # Check if there are empty squares left
        return ' ' in self.board

    def make_move(self, square, letter):
        # Make a move on the board
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check if the current move leads to a win
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # Left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # Right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

def play(game, x_player, o_player, print_game=True):
    # Function to play the game
    if print_game:
        game.print_board_nums()

    letter = 'X'  # Starting letter
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            
            #after we made our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X' # switches player
        
        #tiny break to make thing little bit easier to read
        if print_game:
            time.sleep(0.8)

    if print_game:
        print('It\'s a tie!')

if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(1000):

        x_player = RandomComputerPlayer('X')  # Create a Human player instance for 'X'
        o_player = GeniusComputerPlayer('O')  # Create a Random Computer player instance for 'O'
        t = TicTacToe()  # Create an instance of TicTacToe
        result = play(t, x_player, o_player, print_game=False)  # Start the game
        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        else:
            ties += 1
    
    print(f'After 100 iterations, we see {x_wins} X_wins, {o_wins} O_wins, and {ties} Ties')

