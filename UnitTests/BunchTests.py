import os
import sys 
unitTestPath = os.path.dirname(__file__) + "/../Source"
sys.path.append(unitTestPath)

import unittest
import os
import sys 
unitTestPath = os.path.dirname(__file__) + "/../Source"
sys.path.append(unitTestPath)

from Bunch import Bunch
from Tile import Tile

class TestBunchClass(unittest.TestCase) :

    def test_Constructor_ShufflesProperly_TwoBunchesAreNotTheSame(self) :
        # Arrange & Act
        tiles = []
        tileA = Tile('A', 1, 1, 1)
        tileB = Tile('B', 2, 2, 3)
        tileC = Tile('C', 3, 3, 5)
        tiles.append(tileA)
        tiles.append(tileB)
        tiles.append(tileC)

        bunchOne = Bunch(tiles)
        bunchTwo = Bunch(tiles)

        # Assert
        self.assertNotEqual(bunchOne, bunchTwo)

    def test_Constructor_GetBunch_ExpectedTilesPresentInBunch(self) :
        # Arrange
        tiles = []
        tile = Tile('A', 1, 1, 1)
        tiles.append(tile)
        expected = 1
        bunch = Bunch(tiles)

        # Act
        result = len(bunch.GetBunch())

        # Assert
        self.assertEqual(result, expected)

    def test_ScoreBunch_ScoreOfOne_ScoreOfOne(self) :
        # Arrange
        tiles = []
        tile = Tile('A', 1, 1, 1)
        tiles.append(tile)
        expected = 1
        bunch = Bunch(tiles)

        # Act
        result = bunch.ScoreBunch()

        # Assert
        self.assertEqual(result, expected)

    def test_IsBunchEmpty_BunchNotEmpty_ReturnsFalse(self) :
        # Arrange
        tiles = []
        tileA = Tile('A', 1, 1, 1)
        tileB = Tile('B', 2, 2, 3)
        tiles.append(tileA)
        tiles.append(tileB)
        bunch = Bunch(tiles)

        # Act
        result = bunch.IsBunchEmpty()

        # Assert
        self.assertFalse(result)

    def test_DealFromBunch_DealTwoTiles_TwoTilesDealt(self) :
        # Arrange
        tiles = []
        tileA = Tile('A', 1, 1, 1)
        tileB = Tile('B', 1, 1, 1)
        tiles.append(tileA)
        tiles.append(tileB)
        expected = 2
        bunch = Bunch(tiles)

        # Act
        resultingBunch = bunch.DealFromBunch(expected)
        result = len(resultingBunch)

        # Assert
        self.assertEqual(result, expected)

    def test_DealFromBunch_DealMoreTilesThanInBunch_ReturnsWholeBunch(self) :
        # Arrange
        tiles = []
        tileA = Tile('A', 1, 1, 1)
        tileB = Tile('B', 1, 1, 1)
        tiles.append(tileA)
        tiles.append(tileB)
        toDeal = 10
        expected = 2
        bunch = Bunch(tiles)

        # Act
        resultingBunch = bunch.DealFromBunch(toDeal)
        result = len(resultingBunch)

        # Assert
        self.assertEqual(result, expected)

    def test_Peel_ValidBunch_ReturnsTilesFromBunch(self) :
        # Arrange
        tiles = []
        tile = Tile('A', 1, 1, 1)
        tiles.append(tile)
        bunch = Bunch(tiles)

        # Act
        result = bunch.Peel()

        # Assert
        self.assertTrue(result) 

    def test_isBunchEmpty_BunchIsEmpty_ReturnsTrue(self) :
        # Arrange
        tiles = []
        bunch = Bunch(tiles)

        # Act
        bunch.DealFromBunch(144)
        result = bunch.IsBunchEmpty()

        # Assert
        self.assertTrue(result) 

if __name__ == '__main__' :
    unittest.main()