from classes.pieces import Pieces
from classes.player import Player


class ChessBoard:
    def __init__(self):
        # the rows, which are a to h
        self.rows = []
        for x in [chr(i) for i in range(ord('a'), ord('i'))]:
            self.rows.append(x)

        # the initial board
        self.chess_board = []
        for col in range(8, 0, -1):
            append_list = ['.' for unused in self.rows]
            self.chess_board.append(append_list)

        self.initial_pieces()
        self.board = self.get_single_list(self.chess_board)
        self.squares = [
            'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8',
            'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7',
            'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6',
            'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5',
            'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4',
            'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
            'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',
            'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1',
        ]
        self.identifier = 0

    # added the initial pieces to 2d arrays
    def initial_pieces(self):
        board_grid = self.chess_board
        # black pieces
        for p in range(8):
            board_grid[1][p] = str(Pieces(1, 'black'))
        board_grid[0][0] = str(Pieces(2, 'black'))
        board_grid[0][1] = str(Pieces(3, 'black'))
        board_grid[0][2] = str(Pieces(4, 'black'))
        board_grid[0][3] = str(Pieces(5, 'black'))
        board_grid[0][4] = str(Pieces(6, 'black'))
        board_grid[0][5] = str(Pieces(4, 'black'))
        board_grid[0][6] = str(Pieces(3, 'black'))
        board_grid[0][7] = str(Pieces(2, 'black'))

        # white pieces
        for p in range(8):
            board_grid[6][p] = str(Pieces(1, 'white'))
        board_grid[7][0] = str(Pieces(2, 'white'))
        board_grid[7][1] = str(Pieces(3, 'white'))
        board_grid[7][2] = str(Pieces(4, 'white'))
        board_grid[7][3] = str(Pieces(5, 'white'))
        board_grid[7][4] = str(Pieces(6, 'white'))
        board_grid[7][5] = str(Pieces(4, 'white'))
        board_grid[7][6] = str(Pieces(3, 'white'))
        board_grid[7][7] = str(Pieces(2, 'white'))

    # print the initial board
    def print_board(self):

        initial_board = self.chess_board
        axis_y = 8
        print("-----------------")
        # print the axis_x
        print(" ", *self.rows, sep=" ")
        # print axis_y and the rows
        for col in initial_board:
            print(axis_y, *col, sep=' ')
            axis_y -= 1
        print("-----------------")

    # write the pieces to a text file
    def write_pieces(self):
        state = []
        for col in self.chess_board:
            for x in col:
                state.append(x)
        with open('chess.txt', 'r+') as file:
            file.write("%s\n" % "".join(state))

    @staticmethod
    # pass by reference, passing the list as the params to get a single list
    def get_single_list(chessboard):
        single_board = []
        for col in chessboard:
            for x in col:
                single_board.append(x)
        return single_board

    # this method called to get what piece in a given square
    # for example a2 as the params and the pieces should be 'P' which is white pawn
    def get_piece(self, square):
        board = self.board
        squares = self.squares
        # get the index of a given square
        index = squares.index(square)
        piece = board[index]
        # return the pieces on the targeted square inside the box
        return piece

    # the move for each color will be "before-destination", example a2-a3.
    def move_piece(self, move):
        # so if the move is a2-a3 it will be split as an array like this ['a2', 'a3']
        piece_move = move.split('-')
        original_square = piece_move[0]
        destination_square = piece_move[1]

        # get the piece on targeted square
        piece_in_before = self.get_piece(original_square)
        piece_in_destination = self.get_piece(destination_square)

        # check the color of the piece that being moved and the target
        piece_color = self.check_piece_color(piece_in_before)
        piece_target_color = self.check_piece_color(piece_in_destination)

        # get the original matrix x and y for the 2d list in order to move the pieces
        axis_x_original = ord(original_square[0]) - 97
        axis_y_original = 8 - int(original_square[1])

        # get the destination matrix x and y for the 2d list in order to move the pieces
        axis_x_destination = ord(destination_square[0]) - 97
        axis_y_destination = 8 - int(destination_square[1])

        # player turn var to check the turn
        player_turn = str
        if self.identifier % 2 == 0:
            player_turn = Player(0)
        else:
            player_turn = Player(1)
        move_validator = int

        if piece_in_destination == '.' or None:
            # check if the player turn is black, the player cannot move the white pieces
            # this statement checks if the player turn color is the same color as the pieces that he wanted to move
            if str(player_turn) == piece_color.lower():
                self.chess_board[axis_y_destination][axis_x_destination] = str(piece_in_before)
                self.chess_board[axis_y_original][axis_x_original] = '.'
                print('-- Valid Move --')
                move_validator = self.player_turn(0)
            else:
                print('-- Invalid Move --')
                print(f'{player_turn} cannot move {piece_color} pieces')
                move_validator = self.player_turn(-1)

        else:
            # check if the piece that being moved targeted the same color
            if piece_color == piece_target_color:
                print('-- Invalid Move --')
                move_validator = self.player_turn(-1)
            # if its different color killed the target
            else:
                self.chess_board[axis_y_destination][axis_x_destination] = str(piece_in_before)
                self.chess_board[axis_y_original][axis_x_original] = '.'
                print(f'EZ KILL from {piece_color}')
                move_validator = self.player_turn(0)

        # update the board if the player made a successful move
        self.board = self.get_single_list(self.chess_board)
        # print the board
        self.print_board()
        if move_validator == 0:
            self.identifier += 1
            return True
        return False

    @staticmethod
    def check_piece_color(piece):
        if piece.islower():
            return 'black'
        else:
            return 'white'

    @staticmethod
    def player_turn(num):
        if num == 0:
            return num
        return num
