from classes.pieces import Pieces


class ChessBoard:
    def __init__(self):
        self.rows = []
        for x in [chr(i) for i in range(ord('a'), ord('i'))]:
            self.rows.append(x)
        # the initial board
        self.chess_board = []
        for col in range(8, 0, -1):
            append_list = ['.' for unused in self.rows]
            self.chess_board.append(append_list)

        self.initial_pieces()
        self.board = self.get_single_list()
        self.squares = [
            'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1',
            'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',
            'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
            'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4',
            'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5',
            'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6',
            'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7',
            'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8',
        ]

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
        # print the axis_x
        print(" ", *self.rows, sep=" ")
        # print axis_y and the rows
        for col in initial_board:
            print(axis_y, *col, sep=' ')
            axis_y -= 1
        print("-----------------")

    def write_pieces(self):
        state = []
        for col in self.chess_board:
            for x in col:
                state.append(x)
        with open('chess.txt', 'r+') as file:
            file.write("%s\n" % "".join(state[::-1]))  # i flip the array because i did it upside down, sorry

    def get_single_list(self):
        single_board = []
        for col in self.chess_board:
            for x in col:
                single_board.append(x)
        return single_board[::-1]

    def get_piece(self, square):
        index = self.squares.index(square)
        piece = self.board[index]
        # return the pieces on the targeted square inside the box
        return piece

    # the move for each color will be "before-destination", example a2-a3.
    def move_piece(self, move):
        # so if the move is a2-a3 it will be split as an array like this ['a2', 'a3']
        piece_move = move.split('-')
        original_square = piece_move[0]
        destination_square = piece_move[1]
        piece_in_before = self.get_piece(original_square)
        piece_in_destination = self.get_piece(destination_square)

        # get the original matrix x and y for the 2d list to be able to move the pieces
        axis_x_original = ord(original_square[0]) - 97
        axis_y_original = 8 - int(original_square[1])

        # get the destination matrix x and y for the 2d list to be able to move the pieces
        axis_x_destination = ord(destination_square[0]) - 97
        axis_y_destination = 8 - int(destination_square[1])

        if piece_in_destination == '.' or None:
            self.chess_board[axis_y_destination][axis_x_destination] = str(piece_in_before)
            self.chess_board[axis_y_original][axis_x_original] = '.'
        self.print_board()
