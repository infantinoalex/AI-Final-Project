"""

Contains the Board class
The Board is the place where all the tiles are played; it starts off enpty, and 
then holds every word which gets played throughout the game

"""

class Board :

    def __init__(self) :
        self.size = 21
        self.board = []
        self.anchors = []

        blank_row = []
        for i in range(self.size) :
            blank_row.append(' ')
        for i in range(self.size) :
            self.board.append(blank_row)

    def PrintBoard(self) :
        for i in range(21) :
            if (i == 0) :
                print(end=" ")
                for j in range(21) :
                    print('+---', end="")
                print('+')
            for j in range(21) :
                print(' |', self.board[i][j], end="")
            print(' |')
            print(end=" ")
            for j in range(21) :
                print('+---', end="")
            print('+')