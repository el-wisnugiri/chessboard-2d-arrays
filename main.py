from classes.chessboard import ChessBoard


if __name__ == '__main__':
    board = ChessBoard()
    board.print_board()
    board.write_pieces()
    # f = open('chess.txt', mode='r+')
    # f.truncate(0)
    # f.seek(0)
    while True:
        move_input = str(input("Please enter a move: "))
        if move_input == "x":
            break
        board.move_piece(move_input)