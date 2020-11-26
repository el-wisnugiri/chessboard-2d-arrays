from classes.chessboard import ChessBoard
from classes.player import Player


if __name__ == '__main__':
    # the turn counter determined the player turn
    # if the counter is even, its white turn. else, its black turn
    counter = 0
    board = ChessBoard()
    board.print_board()
    board.write_pieces()

    while True:
        if counter % 2 == 0:
            print(f'{Player(0)} turn')
        else:
            print(f'{Player(1)} turn')
        move_input = str(input("Please enter a move (input x to quit the game): "))

        if move_input == "x":
            break
        elif move_input.upper() == 'O-O' or move_input.upper() == 'O-O-O':
            if board.castling_move(move_input):
                counter += 1
        elif board.move_piece(move_input):
            # increment counter for each move that returns True
            counter += 1
