from classes.pieces import Pieces


class ChessBoard:
    def __init__(self):
        self.rows = []
        for x in [chr(i) for i in range(ord('a'), ord('i'))]:
            self.rows += x

        self.chess_board = []
        for square in range(8, 0, -1):
            append_list = ['.' for unused in self.rows]
            self.chess_board.append(append_list)

        self.initial_pieces()

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
    def print_chess_board(self):

        initial_board = self.chess_board
        axis_y = 8
        # print the axis_x
        print(" ", *self.rows, sep=" ")
        # print axis_y and the rows
        for col in initial_board:
            print(axis_y, *col, sep=' ')
            axis_y -= 1

    def write_pieces(self):
        state = []
        for col in self.chess_board:
            for x in col:
                state.append(x)
        with open('chess.txt', 'r+') as file:
            file.write("%s\n" % "".join(state))
