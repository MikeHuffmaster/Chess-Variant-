# Name: Mike Huffmaster
# Github: MikeHuffmaster
# Date: 12/9/2023
# Description:  This program is a variant of chess that follows the movement of a chess game, but does not include
#              the rules for check or checkmate.  This program also does not include the rules for castling, en passant,
#              or pawn promotion.  The winner is declared when all pieces of one type are captured. For example, if all
#              the black pawns are captured, then white wins the game.
import copy
import string


class GameBoard:
    """
    initializes the game board, and communicates with the ChessVar class
    """

    def __init__(self):

        self._board = None
        self._initial_board = [[''] * 8 for _ in range(8)]
        self._captured_pieces = {'WHITE': [], "BLACK": []}  # Keeps track of captured pieces
        self._move_history = []  # Saves the current state of the board after each move

        self.initialize_board()

    def initialize_board(self):
        """
        Initializes the board with the pieces in their starting positions
        :return:
        """
        for row in range(0, 8):
            for col in range(0, 8):
                _col_let = string.ascii_lowercase[col]  # Convert column number to letter

                # White pieces are capitalized, black pieces are lowercase, N stands for knight
                if row == 1:
                    self._initial_board[row][col] = "P"
                elif row == 6:
                    self._initial_board[row][col] = "p"
                elif row == 0:
                    if _col_let == "a" or _col_let == "h":
                        self._initial_board[row][col] = "R"
                    elif _col_let == "b" or _col_let == "g":
                        self._initial_board[row][col] = "N"
                    elif _col_let == "c" or _col_let == "f":
                        self._initial_board[row][col] = "B"
                    elif _col_let == "d":
                        self._initial_board[row][col] = "Q"
                    elif _col_let == "e":
                        self._initial_board[row][col] = "K"
                elif row == 7:  # lowercase black players pieces, N stands for knight
                    if _col_let == "a" or _col_let == "h":
                        self._initial_board[row][col] = "r"
                    elif _col_let == "b" or _col_let == "g":
                        self._initial_board[row][col] = "n"
                    elif _col_let == "c" or _col_let == "f":
                        self._initial_board[row][col] = "b"
                    elif _col_let == "d":
                        self._initial_board[row][col] = "q"
                    elif _col_let == "e":
                        self._initial_board[row][col] = "k"

        self._board = copy.deepcopy(self._initial_board)  # Creates a copy of the initial board

    def get_piece(self, row, col):
        """
        Gets the piece at the specified row and column
        :param row: The row the piece is on
        :param col: The column the piece is on
        :return: The piece at the specified row and column
        """
        piece_type = str(self._board[row][col])

        if piece_type == 'P':
            return Pawn("WHITE")
        elif piece_type == "p":
            return Pawn("BLACK")
        elif piece_type == "R":
            return Rook("WHITE")
        elif piece_type == "r":
            return Rook("BLACK")
        elif piece_type == "N":
            return Knight("WHITE")
        elif piece_type == "n":
            return Knight("BLACK")
        elif piece_type == "B":
            return Bishop("WHITE")
        elif piece_type == "b":
            return Bishop("BLACK")
        elif piece_type == "Q":
            return Queen("WHITE")
        elif piece_type == "q":
            return Queen("BLACK")
        elif piece_type == "K":
            return King("WHITE")
        elif piece_type == "k":
            return King("BLACK")
        elif piece_type == ".":
            return None
        else:
            return None

    def set_piece(self, row, col, piece):
        """
        Sets the piece at the specified row and column
        :param row: The row the piece is on
        :param col: The column the piece is on
        :param piece: The piece to set
        """
        self._board[row][col] = piece

    def refresh_board(self, start_point, end_point):
        """
        refreshes the board to the updated version
        :param start_point: the square the piece starts on
        :param end_point: the square the piece moved to
        """

        _start_col = ord(start_point[0]) - ord('a')  # Convert column letter to integer
        _start_row = int(start_point[1]) - 1  # Convert row number to integer
        _end_col = ord(end_point[0]) - ord('a')  # Convert column letter to integer
        _end_row = int(end_point[1]) - 1  # Convert row number to integer

        current_state = "\n".join([" ".join(str(piece) for piece in row) for row in self._board])
        self._move_history.append(current_state)

    def show_board(self):
        """
        show the current board
        return: The current board
        """
        print("\n   Current Board")
        print("  " + " ".join(string.ascii_lowercase[:8]))
        for row_num, row in enumerate(self._board[::-1], start=1):  # enumerate the board
            print(9 - row_num, end=" ")  # print the row number
            for col in row:  # print the column
                print(col if col else '.', end=" ")
            print()

    @property
    def captured_pieces(self):
        return self._captured_pieces


class ChessVar:
    """
    Controls the unique gameplay of a variant of chess by
    overseeing the games layout, tracking each players turns,
    setting rules for valid moves, captures, and wins, and provides
    methods for the gameplay

    communicates with the GameBoard class
    """

    def __init__(self):
        """
        Initiates a game of ChessVar

        sets current player to white, sets game state as unfinished, and sets up
        game board
        """
        self._current_player = "WHITE"  # Keeps track of the current player
        self._game_state = "UNFINISHED"  # Keeps track of the current state of the game
        self._game_board = GameBoard()
        self._current_turn = 1  # Keeps track of the current turn
        self._move_history = []  # Saves the current state of the board after each move

    def get_game_state(self):
        """
        Gets the current state of the game
        :return: "UNFINISHED", "WHITE_WON", "BLACK_WON"
        """
        return self._game_state

    def make_move(self, start_point, end_point):
        """
        Moves the chess piece if it is a valid move
        :param start_point: start point of the piece
        :param end_point: end point of the piece
        :return:True or False if move is Valid or Invalid
        """

        if self._game_state != "UNFINISHED":
            return False

        # If is_valid, refresh board(start_point, end_point)
        _start_row = int(start_point[1]) - 1  # Convert row number to integer
        _start_col = ord(start_point[0]) - ord('a')  # Convert column letter to integer
        _end_row = int(end_point[1]) - 1  # Convert row number to integer
        _end_col = ord(end_point[0]) - ord('a')  # Convert column letter to integer

        piece = self._game_board.get_piece(_start_row, _start_col)

        if piece and piece.get_color == self._current_player:

            if piece and piece.is_valid_move(_start_row, _start_col, _end_row, _end_col,
                                             self._game_board):  # Check if the move is valid
                captured_piece = self._game_board.get_piece(_end_row, _end_col)  # capture the piece
                self._game_board.set_piece(_end_row, _end_col, piece)  # move the piece
                self._game_board.set_piece(_start_row, _start_col, ".")

                if captured_piece and captured_piece is not None:  # Check if there is a piece at the end point
                    self._game_board.captured_pieces[self._current_player].append(captured_piece)

                current_state = "\n".join([" ".join(str(piece) for piece in row) for row in self._game_board._board])
                self._move_history.append(current_state)
                self._game_board.refresh_Board(start_point, end_point)

                self._current_turn += 1  # Increment the turn number

                # Determine the current player based on the turn number
                self._current_player = "WHITE" if self._current_turn % 2 == 1 else "BLACK"

                for color in ["WHITE", "BLACK"]:
                    piece_count = {'p': 8, 'r': 2, 'n': 2, 'b': 2, 'q': 1, 'k': 1}  # set the amount of pieces

                    for piece_type, count in piece_count.items():
                        captured_count = len(
                            [p for p in self._game_board.captured_pieces[color] if str(p).lower() == piece_type])

                        if captured_count == count:
                            self._game_state = "WHITE_WON" if color == "WHITE" else "BLACK_WON"
                            return True  # Game is over

                return True  # Valid move, game is not over

            self._current_player = "WHITE" if self._current_turn % 2 == 1 else "BLACK"
            return False  # Invalid move, game is not over


class ChessPiece:
    """
    Creates the chess pieces and their attributes
    """

    def __init__(self, color, piece_type):
        """
        Creates the chess pieces and their attributes
        :param color: the color of the piece
        :param piece_type: the type of piece
        """
        self.get_color = color
        self._piece_type = piece_type

    def get_color(self):
        """
        Gets the color of the piece
        :return: color of the piece
        """
        return self.get_color


class Pawn(ChessPiece):
    """
    Creates the pawn piece and its attributes
    """

    def __init__(self, color):
        super().__init__(color, piece_type="Pawn")

    def __str__(self):
        return "P" if self.get_color == "WHITE" else "p"  # string representation of the piece

    def is_valid_move(self, start_row, start_col, end_row, end_col, game_board):

        """
        Determines if the move desired is a valid move based on piece and row/col
        :param start_row: Starting Row of piece
        :param start_col: Starting column of piece
        :param end_row: Desired end row of piece
        :param end_col: Desired end column of piece
        :param game_board: The current game board
        :return: True if move is valid, false if invalid
        """
        if not (0 <= end_row < 8 and 0 <= end_col < 8):  # Check if the piece is moving off the board
            return False

        end_piece = game_board.get_piece(end_row, end_col)  # get the piece at the end point

        if end_piece and end_piece.get_color == self.get_color:
            return False  # Check if the piece is moving to a square with a piece of the same color

        if self.get_color == "WHITE":
            middle_piece = game_board.get_piece(2, start_col)

            # Check if the piece is moving forward two spaces on its first turn and the space is empty
            if start_row == end_row - 2 and start_col == end_col and middle_piece is None:
                return True

            elif start_row == end_row - 1 and start_col == end_col and end_piece.get_color == "BLACK":
                return False

            elif start_row == end_row - 1 and start_col == end_col and end_piece is None:
                return True

            # Check if the piece is moving diagonally to capture a piece
            elif end_row == start_row + 1 and (end_col == start_col or abs(end_col - start_col) == 1):
                return end_piece is not None and end_piece.get_color == "BLACK"

        elif self.get_color == "BLACK":
            middle_piece = game_board.get_piece(5, start_col)

            # Check if the piece is moving forward two spaces on its first turn and the space is empty
            if start_row == end_row + 2 and start_col == end_col and middle_piece is None:
                return True

            elif start_row == end_row + 1 and start_col == end_col and end_piece.get_color == "WHITE":
                return False

            elif start_row == end_row + 1 and start_col == end_col and end_piece is None:
                return True

            # Check if the piece is moving diagonally to capture a piece
            elif end_row == start_row - 1 and (end_col == start_col or abs(end_col - start_col) == 1):
                return end_piece is not None and end_piece.get_color == "WHITE"

        return False


class Rook(ChessPiece):
    """
    Creates the rook piece and its attributes
    """

    def __init__(self, color):
        super().__init__(color, piece_type="Rook")

    def __str__(self):
        return "R" if self.get_color == "WHITE" else "r"  # string representation of the piece

    def is_valid_move(self, start_row, start_col, end_row, end_col, game_board):
        """
        Determines if the move desired is a valid move based on piece and row/col
        :param self: the piece
        :param start_row: starting row of piece
        :param start_col: starting column of piece
        :param end_row: end row of piece
        :param end_col: end column of piece
        :param game_board: the current game board
        :return: True if move is valid, false if invalid
        """
        if not (0 <= end_row < 8 and 0 <= end_col < 8):  # Check if the piece is moving off the board
            return False

        end_piece = game_board.get_piece(end_row, end_col)

        if end_piece and end_piece.get_color == self.get_color:
            return False  # Check if the piece is moving to a square with a piece of the same color

        if start_row == end_row:  # Check if the piece is moving horizontally
            return self.is_valid_horizontal_move(start_row, start_col, end_col, game_board)
        elif start_col == end_col:  # Check if the piece is moving vertically
            return self.is_valid_vertical_move(start_col, start_row, end_row, game_board)

        return False

    def is_valid_horizontal_move(self, row, start_col, end_col, game_board):
        """
        Determines if the move desired is a valid horizontal move based on piece and row/col
        :param row: The row the piece is on
        :param start_col: the starting column of the piece
        :param end_col: the ending column of the piece
        :param game_board: the current game board
        :return: true if move is valid, false if invalid
        """
        step = 1 if start_col < end_col else -1
        for col in range(start_col + step, end_col, step):
            current_piece = game_board.get_piece(row, col)
            if current_piece is not None and current_piece.get_color == self.get_color:
                return False
        return True

    def is_valid_vertical_move(self, col, start_row, end_row, game_board):
        """
        Determines if the move desired is a valid vertical move based on piece and row/col
        :param col: the column the piece is on
        :param start_row: the starting row of the piece
        :param end_row: the ending row of the piece
        :param game_board: the current game board
        :return: true if move is valid, false if invalid
        """
        step = 1 if start_row < end_row else -1
        for row in range(start_row + step, end_row, step):
            current_piece = game_board.get_piece(row, col)
            if current_piece is not None and current_piece.get_color == self.get_color:
                return False
        return True


class Knight(ChessPiece):
    """
    Creates the knight piece and its attributes
    """

    def __init__(self, color):
        super().__init__(color, piece_type="Knight")

    def __str__(self):
        return "N" if self.get_color == "WHITE" else "n"  # string representation of the piece

    def is_valid_move(self, start_row, start_col, end_row, end_col, game_board):
        """
        Determines if the move desired is a valid move based on piece and row/col
        :param start_row: Starting Row of piece
        :param start_col: Starting column of piece
        :param end_row: End row of piece
        :param end_col: End column of piece
        :param game_board: The current game board
        :return: True if move is valid, false if invalid
        """

        if not (0 <= end_row < 8 and 0 <= end_col < 8):  # Check if the piece is moving off the board
            return False

        end_piece = game_board.get_piece(end_row, end_col)

        if end_piece and end_piece.get_color == self.get_color:
            return False  # Check if the piece is moving to a square with a piece of the same color

        if start_row == end_row or start_col == end_col:  # Check if the piece is moving in a straight line
            return False

        if abs(start_row - end_row) == 2 and abs(start_col - end_col) == 1 or abs(start_row - end_row) == 1 and abs(
                start_col - end_col) == 2:
            return True
        return False


class Bishop(ChessPiece):
    """
    Creates the bishop piece and its attributes
    """

    def __init__(self, color):
        super().__init__(color, piece_type="Bishop")

    def __str__(self):
        return "B" if self.get_color == "WHITE" else "b"  # string representation of the piece

    def is_valid_move(self, start_row, start_col, end_row, end_col, game_board):
        """
        Determines if the move desired is a valid move based on piece and row/col
        :param start_row: Starting Row of piece
        :param start_col: Starting column of piece
        :param end_row: End row of piece
        :param end_col: End column of piece
        :param game_board: The current game board
        :return: True if move is valid, false if invalid
        """
        if not (0 <= end_row < 8 and 0 <= end_col < 8):  # Check if the piece is moving off the board
            return False

        end_piece = game_board.get_piece(end_row, end_col)

        if end_piece and end_piece.get_color == self.get_color:
            return False  # Check if the piece is moving to a square with a piece of the same color

        if start_row == end_row or start_col == end_col:  # Check if the piece is moving in a straight line
            return False

        if abs(start_row - end_row) != abs(start_col - end_col):
            return False  # Check if the piece is moving diagonally

        row_dir = 1 if start_row < end_row else -1  # Check if the piece is moving up or down
        col_dir = 1 if start_col < end_col else -1  # Check if the piece is moving left or right
        row, col = start_row + row_dir, start_col + col_dir  # move the piece

        while row != end_row and col != end_col:  #
            if game_board.get_piece(row, col) is not None:
                return False  # there are pieces in the way
            row += row_dir  # move the piece
            col += col_dir  # move the piece
        return True


class Queen(ChessPiece):
    """
    Creates the queen piece and its attributes, combination of rook and bishop moves
    """

    def __init__(self, color):
        super().__init__(color, piece_type="Queen")

    def __str__(self):
        return "Q" if self.get_color == "WHITE" else "q"  # string representation of the piece

    def is_valid_move(self, start_row, start_col, end_row, end_col, game_board):
        """
        Determines if the move desired is a valid move based on piece and row/col
        :param start_row: Starting Row of piece
        :param start_col: Starting column of piece
        :param end_row: End row of piece
        :param end_col: End column of piece
        :param game_board: The current game board
        :return: True if move is valid, false if invalid
        """
        if not (0 <= end_row < 8 and 0 <= end_col < 8):  # Check if the piece is moving off the board
            return False

        end_piece = game_board.get_piece(end_row, end_col)

        if end_piece and end_piece.get_color == self.get_color:
            return False  # Check if the piece is moving to a square with a piece of the same color

        if abs(start_row - end_row) != abs(start_col - end_col):
            if start_row != end_row and start_col != end_col and abs(start_row - end_row) != abs(start_col - end_col):
                return False  # Check if the piece is moving diagonally

        row_dir = 1 if start_row < end_row else -1  # Check if the piece is moving up or down
        col_dir = 1 if start_col < end_col else -1  # Check if the piece is moving left or right
        row, col = start_row + row_dir, start_col + col_dir

        while row != end_row and col != end_col:  # Check if there are pieces in the way
            if end_piece is not None:
                return False

            row += row_dir  # move the piece
            col += col_dir  # move the piece

        return True


class King(ChessPiece):
    """
    Creates the king piece and its attributes
    """

    def __init__(self, color):
        super().__init__(color, piece_type="King")

    def __str__(self):
        return "K" if self.get_color == "WHITE" else "k"  # string representation of the piece

    def is_valid_move(self, start_row, start_col, end_row, end_col, game_board):
        """
        Determines if the move desired is a valid move based on piece and row/col
        :param start_row: Starting Row of piece
        :param start_col: Starting column of piece
        :param end_row: End row of piece
        :param end_col: End column of piece
        :param game_board: The current game board
        :return: True if move is valid, false if invalid
        """

        if not (0 <= end_row < 8 and 0 <= end_col < 8):  # Check if the piece is moving off the board
            return False

        end_piece = game_board.get_piece(end_row, end_col)

        if end_piece and end_piece.get_color == self.get_color:
            return False  # Check if the piece is moving to a square with a piece of the same color

        return abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1  # Check if the piece is moving one space


# Test the game board

# game = ChessVar()
# game._game_board.show_board()
#
# # # Test a couple of moves
# game.make_move("e2", "e4")
# game._game_board.show_board()
# game.make_move("e7", "e5")
# game._game_board.show_board()
# game.make_move("a7", 'a5')
# game._game_board.show_board()
# game.make_move("a4", 'a5')
# game._game_board.show_board()

# Test the game state
# print("Test game state:", game.get_game_state())

# Test normal movement
# print("Test normal movement:", game.make_move("e1", "e2"))
# game._game_board.show_board()

# Test captures
# print("Test captures:", game.make_move("d7", "d5"))
# game._game_board.show_board()
# game.make_move("e4", "d5")
# game._game_board.show_board()


# Test turn order
# print("Test turn order:", game.make_move("e2", "e4"))
# game._game_board.show_board()

# # Test win for black by capturing both of white's knights
# game.make_move("b8", "c6")
# game._game_board.show_board()
# game.make_move("g1", "f3")
# game._game_board.show_board()  #
# game.make_move("c6", "a5")
# game._game_board.show_board()
# game.make_move("f3", "g5")
# game._game_board.show_board()
# game.make_move("d8", "g5")
# game._game_board.show_board()
# game.make_move("e2", "e3")
# game._game_board.show_board()
# game.make_move("g5", "e3")
# game._game_board.show_board()
# print("Test win for black:", game.get_game_state())

# Test win for white by capturing black's queen
# game.make_move("d7", "d6")
# game._game_board.show_board()
# game.make_move("g5", "f7")
# game._game_board.show_board()
# game.make_move("a8", "b8")
# game._game_board.show_board()
# game.make_move("f7", "d8")
# game._game_board.show_board()
# print("Test win for white:", game.get_game_state())
