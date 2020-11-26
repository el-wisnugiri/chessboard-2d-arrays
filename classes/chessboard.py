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
        self.write_pieces()
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

        # update the state of the board each time the player made a successful move

    @staticmethod
    def update_board_file(ori, destination):
        with open('chess.txt', 'r+') as file:
            # seek the index position of original square of the piece
            file.seek(ori)
            # read the piece string from the file
            piece = file.read(1)
            # seek the original position and replace it with '.'
            file.seek(ori)
            file.write('.')
            # overwrite the piece in the destination index position in the file
            file.seek(destination)
            file.write(piece)

    # the move for each color will be "before-destination", example a2-a3.
    def move_piece(self, move):
        # player turn var to check the turn
        player_turn = str
        if self.identifier % 2 == 0:
            player_turn = Player(0)
        else:
            player_turn = Player(1)
        move_validator = int

        # so if the move is a2-a3 it will be split as an array like this ['a2', 'a3']
        piece_move = move.split('-')
        original_square = piece_move[0]
        destination_square = piece_move[1]

        # get the original index and destination index to update the board state in the txt file
        ori_index = self.get_file_index(original_square)
        destination_index = self.get_file_index(destination_square)

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

        # check of the move target is an empty square
        if piece_in_before == '.' and piece_in_destination == '.':
            print('-- Invalid Move --')
            print('There is no pieces that can be move there')
            move_validator = self.player_turn(-1)

        elif piece_in_destination == '.' or None:
            # check if the player turn is black, the player cannot move the white pieces
            # this statement checks if the player turn color is the same color as the pieces that he wanted to move
            if str(player_turn) == piece_color.lower():
                self.chess_board[axis_y_destination][axis_x_destination] = str(piece_in_before)
                self.chess_board[axis_y_original][axis_x_original] = '.'
                self.update_board_file(ori_index, destination_index)
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
                print(f'{player_turn} cannot capture {piece_color} pieces')
                move_validator = self.player_turn(-1)
            # if its different color killed the target
            else:
                self.chess_board[axis_y_destination][axis_x_destination] = str(piece_in_before)
                self.chess_board[axis_y_original][axis_x_original] = '.'
                self.update_board_file(ori_index, destination_index)
                print(f'EZ KILL from {piece_color}')
                move_validator = self.player_turn(0)

        # update the board if the player made a successful move
        self.board = self.get_single_list(self.chess_board)
        # print the board
        self.print_board()
        # validate the move, if the move_validator int is not 0. then its not a valid move
        if move_validator == 0:
            self.identifier += 1
            return True
        return False

    # my complicated castling logic
    def castling_move(self, castling):
        # player turn var to check the turn
        player_turn = str
        if self.identifier % 2 == 0:
            player_turn = Player(0)
        else:
            player_turn = Player(1)
        move_validator = int

        # get the ori and destination square for white king (king side castling)
        ori_square_white_king = 'e1'
        destination_square_white_king = 'g1'

        # get the original index and destination index to update the board state in the txt file
        ori_white_king_index = self.get_file_index(ori_square_white_king)
        destination_white_king_index = self.get_file_index(destination_square_white_king)

        # get the ori and destination square for white king (queen side castling)
        destination_square_white_king_qs = 'c1'

        # get the original index and destination index to update the board state in the txt file (Queen Side)
        destination_white_king_index_qs = self.get_file_index(destination_square_white_king_qs)

        # get the ori and destination square for black king (king side)
        ori_square_black_king = 'e8'
        destination_square_black_king = 'g8'

        # get the original index and destination index to update the board state in the txt file
        ori_black_king_index = self.get_file_index(ori_square_black_king)
        destination_black_king_index = self.get_file_index(destination_square_black_king)

        # get the ori and destination square for black king (queen side)
        destination_square_black_king_qs = 'c8'

        # get the original index and destination index to update the board state in the txt file (Queen Side)
        destination_black_king_index_qs = self.get_file_index(destination_square_black_king_qs)

        # get the ori and destination square for white rook if we castle king side
        ori_square_white_rook_ks = 'h1'
        destination_square_white_rook_ks = 'f1'

        # get the original index and destination index to update the board state in the txt file
        ori_white_rook_ks_index = self.get_file_index(ori_square_white_rook_ks)
        destination_white_rook_ks_index = self.get_file_index(destination_square_white_rook_ks)

        # get the ori and destination square for white rook if we castle queen side
        ori_square_white_rook_qs = 'a1'
        destination_square_white_rook_qs = 'd1'

        # get the original index and destination index to update the board state in the txt file (Queen Side)
        ori_white_rook_qs_index = self.get_file_index(ori_square_white_rook_qs)
        destination_white_rook_qs_index = self.get_file_index(destination_square_white_rook_qs)

        # get the ori and destination square for black rook if we castle king side
        ori_square_black_rook_ks = 'h8'
        destination_square_black_rook_ks = 'f8'

        # get the original index and destination index to update the board state in the txt file
        ori_black_rook_ks_index = self.get_file_index(ori_square_black_rook_ks)
        destination_black_rook_ks_index = self.get_file_index(destination_square_black_rook_ks)

        # get the ori and destination square for black rook if we castle king side
        ori_square_black_rook_qs = 'a8'
        destination_square_black_rook_qs = 'd8'

        # get the original index and destination index to update the board state in the txt file
        ori_black_rook_qs_index = self.get_file_index(ori_square_black_rook_qs)
        destination_black_rook_qs_index = self.get_file_index(destination_square_black_rook_qs)

        # get white king piece in its ori square
        ori_white_king = self.get_piece(ori_square_white_king)

        # get black king piece in its ori square
        ori_black_king = self.get_piece(ori_square_black_king)

        # get white rook piece in its ori square on king side (ks)
        ori_white_rook_ks = self.get_piece(ori_square_white_rook_ks)

        # get white rook piece in its ori square on king side (qs)
        ori_white_rook_qs = self.get_piece(ori_square_white_rook_qs)

        # get black rook piece in its ori square on king side (ks)
        ori_black_rook_ks = self.get_piece(ori_square_black_rook_ks)

        # get black rook piece in its ori square on king side (qs)
        ori_black_rook_qs = self.get_piece(ori_square_black_rook_qs)

        # get the original matrix x and y of white king for the 2d list in order to move the pieces
        axis_x_ori_white_king = ord(ori_square_white_king[0]) - 97
        axis_y_ori_white_king = 8 - int(ori_square_white_king[1])

        # get the original matrix x and y of black king for the 2d list in order to move the pieces
        axis_x_ori_black_king = ord(ori_square_black_king[0]) - 97
        axis_y_ori_black_king = 8 - int(ori_square_black_king[1])

        # get the original matrix x and y of white rook for the 2d list in order to move the pieces
        axis_x_ori_white_rook_ks = ord(ori_square_white_rook_ks[0]) - 97
        axis_y_ori_white_rook_ks = 8 - int(ori_square_white_rook_ks[1])

        # get the original matrix x and y of white rook for the 2d list in order to move the pieces (Queen Side)
        axis_x_ori_white_rook_qs = ord(ori_square_white_rook_qs[0]) - 97
        axis_y_ori_white_rook_qs = 8 - int(ori_square_white_rook_qs[1])

        # get the original matrix x and y of black rook for the 2d list in order to move the pieces
        axis_x_ori_black_rook_ks = ord(ori_square_black_rook_ks[0]) - 97
        axis_y_ori_black_rook_ks = 8 - int(ori_square_black_rook_ks[1])

        # get the original matrix x and y of black rook for the 2d list in order to move the pieces (Queen Side)
        axis_x_ori_black_rook_qs = ord(ori_square_black_rook_qs[0]) - 97
        axis_y_ori_black_rook_qs = 8 - int(ori_square_black_rook_qs[1])

        # get the destination matrix x and y of white king for the 2d list in order to move the pieces
        axis_x_destination_white_king = ord(destination_square_white_king[0]) - 97
        axis_y_destination_white_king = 8 - int(destination_square_white_king[1])

        # get the destination matrix x and y of white king for the 2d list in order to move the pieces (Queen Side)
        axis_x_destination_white_king_qs = ord(destination_square_white_king_qs[0]) - 97
        axis_y_destination_white_king_qs = 8 - int(destination_square_white_king_qs[1])

        # get the destination matrix x and y of black king for the 2d list in order to move the pieces
        axis_x_destination_black_king = ord(destination_square_black_king[0]) - 97
        axis_y_destination_black_king = 8 - int(destination_square_black_king[1])

        # get the destination matrix x and y of black king for the 2d list in order to move the pieces (Queen Side)
        axis_x_destination_black_king_qs = ord(destination_square_black_king_qs[0]) - 97
        axis_y_destination_black_king_qs = 8 - int(destination_square_black_king_qs[1])

        # get the destination matrix x and y for the 2d list in order to move the pieces
        axis_x_destination_white_rook_ks = ord(destination_square_white_rook_ks[0]) - 97
        axis_y_destination_white_rook_ks = 8 - int(destination_square_white_rook_ks[1])

        # get the destination matrix x and y for the 2d list in order to move the pieces (Queen Side)
        axis_x_destination_white_rook_qs = ord(destination_square_white_rook_qs[0]) - 97
        axis_y_destination_white_rook_qs = 8 - int(destination_square_white_rook_qs[1])

        # get the destination matrix x and y for the 2d list in order to move the pieces
        axis_x_destination_black_rook_ks = ord(destination_square_black_rook_ks[0]) - 97
        axis_y_destination_black_rook_ks = 8 - int(destination_square_black_rook_ks[1])

        # get the destination matrix x and y for the 2d list in order to move the pieces (Queen Side)
        axis_x_destination_black_rook_qs = ord(destination_square_black_rook_qs[0]) - 97
        axis_y_destination_black_rook_qs = 8 - int(destination_square_black_rook_qs[1])

        # Castling on King Side
        if castling.upper() == 'O-O':
            if str(player_turn) == 'white' and self.castle_white_king_side():
                # move the king
                self.chess_board[axis_y_destination_white_king][axis_x_destination_white_king] = str(ori_white_king)
                self.chess_board[axis_y_ori_white_king][axis_x_ori_white_king] = '.'
                # move the rook on king side
                self.chess_board[axis_y_destination_white_rook_ks][axis_x_destination_white_rook_ks] = str(
                    ori_white_rook_ks)
                self.chess_board[axis_y_ori_white_rook_ks][axis_x_ori_white_rook_ks] = '.'
                # update king move in txt file
                self.update_board_file(ori_white_king_index, destination_white_king_index)
                # update rook move in txt file
                self.update_board_file(ori_white_rook_ks_index, destination_white_rook_ks_index)
                print('-- Valid Move --')
                print(f'{player_turn} just castled!')
                move_validator = self.player_turn(0)

            elif str(player_turn) == 'black' and self.castle_black_king_side():
                # move the king
                self.chess_board[axis_y_destination_black_king][axis_x_destination_black_king] = str(ori_black_king)
                self.chess_board[axis_y_ori_black_king][axis_x_ori_black_king] = '.'
                # move the rook on king side
                self.chess_board[axis_y_destination_black_rook_ks][axis_x_destination_black_rook_ks] = str(
                    ori_black_rook_ks)
                self.chess_board[axis_y_ori_black_rook_ks][axis_x_ori_black_rook_ks] = '.'
                # update king move in txt file
                self.update_board_file(ori_black_king_index, destination_black_king_index)
                # update rook move in txt file
                self.update_board_file(ori_black_rook_ks_index, destination_black_rook_ks_index)
                print('-- Valid Move --')
                print(f'{player_turn} just castled!')
                move_validator = self.player_turn(0)

            else:
                print('-- Invalid Move --')
                print('Cannot castle if there is pieces between rook and king')
                move_validator = self.player_turn(-1)

        # Castling on Queen Side
        elif castling.upper() == 'O-O-O':
            if str(player_turn) == 'white' and self.castle_white_queen_side():
                self.chess_board[axis_y_destination_white_king_qs][axis_x_destination_white_king_qs] = str(
                    ori_white_king)
                self.chess_board[axis_y_ori_white_king][axis_x_ori_white_king] = '.'
                # move the rook on king side
                self.chess_board[axis_y_destination_white_rook_qs][axis_x_destination_white_rook_qs] = str(
                    ori_white_rook_qs)
                self.chess_board[axis_y_ori_white_rook_qs][axis_x_ori_white_rook_qs] = '.'
                # update king move in txt file
                self.update_board_file(ori_white_king_index, destination_white_king_index_qs)
                # update rook move in txt file
                self.update_board_file(ori_white_rook_qs_index, destination_white_rook_qs_index)
                print('-- Valid Move --')
                print(f'{player_turn} just castled!')
                move_validator = self.player_turn(0)

            elif str(player_turn) == 'black' and self.castle_black_queen_side():
                self.chess_board[axis_y_destination_black_king_qs][axis_x_destination_black_king_qs] = str(
                    ori_white_king)
                self.chess_board[axis_y_ori_black_king][axis_x_ori_black_king] = '.'
                # move the rook on king side
                self.chess_board[axis_y_destination_black_rook_qs][axis_x_destination_black_rook_qs] = str(
                    ori_black_rook_qs)
                self.chess_board[axis_y_ori_black_rook_qs][axis_x_ori_black_rook_qs] = '.'
                # update king move in txt file
                self.update_board_file(ori_black_king_index, destination_black_king_index_qs)
                # update rook move in txt file
                self.update_board_file(ori_black_rook_qs_index, destination_black_rook_qs_index)
                print('-- Valid Move --')
                print(f'{player_turn} just castled!')
                move_validator = self.player_turn(0)

            else:
                print('-- Invalid Move --')
                print('Cannot castle if there is pieces between rook and king')
                move_validator = self.player_turn(-1)

        # update the board if the player made a successful move
        self.board = self.get_single_list(self.chess_board)
        # print the board
        self.print_board()
        # validate the move, if the move_validator int is not 0. then its not a valid move
        if move_validator == 0:
            self.identifier += 1
            return True
        return False

    # check the pieces color, if its lower cases then its black pieces
    @staticmethod
    def check_piece_color(piece):
        if piece.islower():
            return 'black'
        else:
            return 'white'

    # return num that later will be used to validate a move
    # a valid move will be identified by 0 and other than 0 is an invalid move
    @staticmethod
    def player_turn(num):
        if num == 0:
            return num
        return num

    # get the index position of a piece and this will be used to do seek and overwrite
    def get_file_index(self, square):
        squares = self.squares
        index = squares.index(square)

        return index

    # validate castling on white king side
    def castle_white_king_side(self):
        square_one = self.get_piece('f1')
        square_two = self.get_piece('g1')

        if square_one == '.' and square_two == '.':
            return True
        return False

    # validate castling on white queen side
    def castle_white_queen_side(self):
        square_one = self.get_piece('b1')
        square_two = self.get_piece('c1')
        square_three = self.get_piece('d1')

        if square_one == '.' and square_two == '.' and square_three == '.':
            return True
        return False

    # validate castling on black king side
    def castle_black_king_side(self):
        square_one = self.get_piece('f8')
        square_two = self.get_piece('g8')

        if square_one == '.' and square_two == '.':
            return True
        return False

    # validate castling on black queen side
    def castle_black_queen_side(self):
        square_one = self.get_piece('b8')
        square_two = self.get_piece('c8')
        square_three = self.get_piece('d8')

        if square_one == '.' and square_two == '.' and square_three == '.':
            return True
        return False
