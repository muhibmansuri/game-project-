class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # 3x3 board
        self.current_winner = None  # Track the winner

    def display_board(self):
        """Displays the current board."""
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
        """Displays the board numbers (0-8) for reference."""
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        """Returns a list of available indices (0-8)."""
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def empty_squares(self):
        """Returns True if there are empty squares on the board."""
        return " " in self.board

    def num_empty_squares(self):
        """Returns the number of empty squares."""
        return self.board.count(" ")

    def make_move(self, square, letter):
        """Makes a move on the board if valid."""
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        """Checks if the last move resulted in a win."""
        # check row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check column
        col_ind = square % 3
        column = [self.board[col_ind + i *3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # top-left to bottom-right
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # top-right to bottom-left
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

def play(game, x_player, o_player, print_game=True):
    """Controls the gameplay loop."""
    if print_game:
        game.print_board_nums()

    letter = "X"
    while game.empty_squares():
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} makes a move to square {square}")
                game.display_board()
                print("")

            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                return letter

            letter = "O" if letter == "X" else "X"  # switch player

    if print_game:
        print("It's a tie!")

class HumanPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f"{self.letter}'s turn. Input move (0-8): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
        return val

class RandomComputerPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        import random
        return random.choice(game.available_moves())

if __name__ == "__main__":
    x_player = HumanPlayer("X")
    # You can change this to HumanPlayer("O") to play against another person
    o_player = RandomComputerPlayer("O") 
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
