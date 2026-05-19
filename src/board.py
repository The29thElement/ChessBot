from const import *
from square import Square

class Board:


    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0,] for col in range(COLS)]

        self.create

    # the _ before the method name shows that it's a private method

    def _create(self):
    

        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        pass
