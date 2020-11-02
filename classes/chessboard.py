class ChessBoard:
    def __init__(self):
        self.rows = []
        for x in [chr(i) for i in range(ord('a'), ord('i'))]:
            self.rows += x

        self.chess_board = []
        for col in range(8, 0, -1):
            dimensional_list = [(row + str(col)) for row in self.rows]
            self.chess_board.append(dimensional_list)

    def print_chess_board(self):
        for row in self.chess_board:
            print(row)
