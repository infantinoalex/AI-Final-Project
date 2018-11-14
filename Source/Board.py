"""

Contains the Board class
The Board is the place where all the tiles are played; it starts off empty, and 
then holds every word which gets played throughout the game

"""

import numpy as np
from Tile import Tile
from Anchor import Anchor
from Word import Word

class Board :

    def __init__(self) :
        self.size = 21
        self.board = np.empty([self.size, self.size], dtype=str)
        self.anchors = [Anchor()]

        for i in range(self.size) :
            for j in range(self.size) :
                self.board[i, j] = ' '

    def GetAnchors(self) :
        return self.anchors

    def PlaceTile(self, tile, xPos, yPos) :
        self.board[xPos, yPos] = tile.GetLetter()

    def PlaceWord(self, word, anchor, anchorIndex, playDirection) :
        relXPos = anchor.GetXPos()
        relYPos = anchor.GetYPos()
        if playDirection == 'across' :
            relXPos-= anchorIndex
            for tile in word.GetTiles() :
                self.PlaceTile(tile, relXPos, relYPos)
                relXPos+= 1
                np.append(self.anchors, Anchor([tile], relXPos, relYPos))
        if playDirection == 'down' :
            relYPos-= anchorIndex
            for tile in word.GetTiles() :
                self.PlaceTile(tile, relXPos, relYPos)
                relYPos+= 1
                np.append(self.anchors, Anchor([tile], relXPos, relYPos))
        np.append(self.anchors, Anchor(word.GetTiles(), relXPos, relYPos))
        np.delete(self.anchors, anchor, 0)


    def PrintBoard(self) :
        for i in range(21) :
            if (i == 0) :
                print(end=" ")
                for j in range(21) :
                    print('+---', end="")
                print('+')
            for j in range(21) :
                print(' |', self.board[j][i], end="")
            print(' |')
            print(end=" ")
            for j in range(21) :
                print('+---', end="")
            print('+')