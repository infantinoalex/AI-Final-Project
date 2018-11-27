import unittest
import Game

class TestGameClass(unittest.TestCase) :

    def test_Constructor(self) :
        # Arrange & Act
        game = Game()

        # Assert
        self.assertTrue(game.bunch)     

    def test_IsGoalState_FalseCase(self) :
        # Arrange
        game = Game()

        # Act
        game.Play()
        result = game.IsGoalState()

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