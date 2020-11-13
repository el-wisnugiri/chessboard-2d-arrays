class Pieces:
    def __init__(self, piece=int, color=str):
        self.piece = piece
        self.color = color

    def __str__(self) -> str:
        if self.piece == 1:
            piece = 'P'

        elif self.piece == 2:
            piece = 'R'

        elif self.piece == 3:
            piece = 'N'

        elif self.piece == 4:
            piece = 'B'

        elif self.piece == 5:
            piece = 'Q'

        elif self.piece == 6:
            piece = 'K'

        if self.color.upper() == 'WHITE':
            return str(piece)
        else:
            return str(piece).lower()
