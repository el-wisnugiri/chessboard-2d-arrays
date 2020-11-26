class Player:
    def __init__(self, player=int):
        self.player = player

    def __str__(self) -> str:
        if self.player == 0:
            player = 'White'

        elif self.player == 1:
            player = 'Black'

        return str(player).lower()
