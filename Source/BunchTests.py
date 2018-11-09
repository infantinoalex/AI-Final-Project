import unittest
from Bunch import Bunch

class TestBunchClass(unittest.TestCase) :

    def test_Constructor_ShufflesProperly_TwoBunchesAreNotTheSame(self) :
        # Arrange & Act
        bunchOne = Bunch()
        bunchTwo = Bunch()

        # Assert
        self.assertNotEqual(bunchOne, bunchTwo)

    def test_Constructor_144TilesAdded_144TilesPresentInBunch(self) :
        # Arrange
        expected = 144
        bunch = Bunch()

        # Act
        result = len(bunch.GetBunch())

        # Assert
        self.assertEqual(result, expected)        

    def test_IsBunchEmpty_BunchNotEmpty_ReturnsFalse(self) :
        # Arrange
        bunch = Bunch()

        # Act
        result = bunch.IsBunchEmpty()

        # Assert
        self.assertFalse(result)

    def test_DealFromBunch_DealFiveTiles_FiveTilesDealt(self) :
        # Arrange
        expected = 5
        bunch = Bunch()

        # Act
        resultingBunch = bunch.DealFromBunch(expected)
        result = len(resultingBunch)

        # Assert
        self.assertEqual(result, expected)

    def test_DealFromBunch_DealMoreTilesThanInBunch_ReturnsWholeBunch(self) :
        # Arrange
        expected = 144
        toRemove = 200
        bunch = Bunch()

        # Act
        resultingBunch = bunch.DealFromBunch(expected)
        result = len(resultingBunch)

        # Assert
        self.assertEqual(result, expected)

    def test_isBunchEmpty_BunchIsEmpty_ReturnsTrue(self) :
        # Arrange
        bunch = Bunch()

        # Act
        bunch.DealFromBunch(144)
        result = bunch.IsBunchEmpty()

        # Assert
        self.assertTrue(result) 

if __name__ == '__main__' :
    unittest.main()