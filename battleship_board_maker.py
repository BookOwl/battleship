import random, sys

UP, DOWN, LEFT, RIGHT = range(4)
DIRECTIONS = UP, DOWN, LEFT, RIGHT
EMPTY = ' .'

class Ship:
    def __init__(self, char, length):
        self.char = char
        self.length = length
        self.orientation = random.choice(DIRECTIONS)
    def cells(self, x, y):
        if self.orientation is UP:
            return [(x, y+o) for o in range(self.length)]
        if self.orientation is DOWN:
            return [(x, y-o) for o in range(self.length)]
        if self.orientation is LEFT:
            return [(x-o, y) for o in range(self.length)]
        if self.orientation is RIGHT:
            return [(x+o, y) for o in range(self.length)]

class Board:
    def __init__(self, height, width, multiplier):
        self.board = [[EMPTY for _ in range(width)] for _ in range(height)]
        self.height = height
        self.width = width
        dreadnought= Ship(" 0", 7)
        carrier    = Ship(" 0", 5)
        battleship = Ship(" 0", 4)
        cruiser    = Ship(" 0", 3)
        submarine  = Ship(" 0", 3)
        destroyer  = Ship(" 0", 2)
        for i in range(multiplier):
            self.place(carrier)
            self.place(battleship)
            self.place(cruiser)
            self.place(submarine)
            self.place(destroyer)
            continue
        self.place(dreadnought)

    def set_cell(self, x, y, char):
        self.board[y][x] = char

    def get_cell(self, x, y):
        return self.board[y][x]

    def is_cell_empty(self, x, y):
        try:
            return x >= 0 and y >= 0 and self.get_cell(x, y) == EMPTY
        except IndexError:
            return False

    def place(self, ship):
        while True:
            x, y = random.randrange(self.width), random.randrange(self.height)
            cells = ship.cells(x, y)
            if all(self.is_cell_empty(*cell) for cell in cells):
                for cell in cells:
                    self.set_cell(*cell, ship.char)
                return

    def __str__(self):
        return "\n".join("".join(row) for row in self.board)

def main():
    try:
        height, width, multiplier = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    except:
        height, width = 10, 10, 7
    board = Board(height, width, multiplier)
    print(board)

if __name__ == '__main__':
    main()



