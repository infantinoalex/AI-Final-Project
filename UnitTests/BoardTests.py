import os
import sys 
unitTestPath = os.path.dirname(__file__) + "/../Source"
sys.path.append(unitTestPath)

import unittest
from Board import Board 
from Tile import Tile

class TestBoardClass(unittest.TestCase) :

    def test_PlaceTile_PlaceRandomTiles(self) :

        # Arrange
        testBoard = Board()
        tile1 = Tile('a', -1, -1.0, -1)
        tile2 = Tile('e', -1, -1.0, -1)
        tile3 = Tile('i', -1, -1.0, -1)
        tile4 = Tile('o', -1, -1.0, -1)
        tile5 = Tile('u', -1, -1.0, -1)

        # Act
        testBoard.PlaceTile(tile1, 9, 13)
        testBoard.PlaceTile(tile2, 16, 20)
        testBoard.PlaceTile(tile3, 7, 13)
        testBoard.PlaceTile(tile4, 20, 5)
        testBoard.PlaceTile(tile5, 16, 4)

        # Assert
        testBoard.PrintBoard()

    def test_PlaceTile_PlaceRandomWords(self) :

        # Arrange
        testBoard = Board()
        t = Tile('t', -1, -1.0, -1)
        e = Tile('e', -1, -1.0, -1)
        s = Tile('s', -1, -1.0, -1)
        i = Tile('i', -1, -1.0, -1)
        n = Tile('n', -1, -1.0, -1)
        g = Tile('g', -1, -1.0, -1)
        b = Tile('b', -1, -1.0, -1)
        c = Tile('c', -1, -1.0, -1)
        h = Tile('h', -1, -1.0, -1)

        testing = [t, e, s, t, i, n, g]
        bitch = [b, i, t, c, h]

        # Act
        anchor = testBoard.GetAnchors()
        testBoard.PlaceWord(testing, anchor, 3, 'across')
        testBoard.PlaceWord(bitch, anchor, 2, 'down')

        # Assert
        testBoard.PrintBoard()

if __name__ == '__main__' :
    unittest.main()
