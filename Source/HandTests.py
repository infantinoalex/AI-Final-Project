import unittest
from Hand import Hand
from Tile import Tile

class TestHandClass(unittest.TestCase) :

    def test_GetPlayerName_ValidName_ReturnsName(self) :
        # Arrange
        playerName = "Player One"
        hand = Hand(playerName)

        # Act
        result = hand.GetPlayerName()

        # Assert
        self.assertEqual(result, playerName)

    def test_PeekHand_EmptyHand_ReturnsFalse(self) :
        # Arrange
        playerName = "Player One"
        hand = Hand(playerName)

        # Act
        result = hand.PeekHand()

        # Assert
        self.assertFalse(result)

    def test_AddTileToHand_ValidTile_TileInHand(self) :
        # Arrange
        playerName = "Player One"
        hand = Hand(playerName)

        letter = 'A'
        value = 1
        tile = Tile(letter, value)

        # Act
        hand.AddTileToHand(tile)
        result = hand.PeekHand()

        # Assert
        self.assertIn(tile, result)

    def test_AddTilesToHand_ValidTiles_TilesInHand(self) :
        # Arrange
        playerName = "Player One"
        hand = Hand(playerName)

        letterA = 'A'
        valueA = 1
        tileA = Tile(letterA, valueA)

        letterB = 'B'
        valueB = 2
        tileB = Tile(letterB, valueB)

        expected = [tileA, tileB]

        # Act
        hand.AddTilesToHand(expected)
        result = hand.PeekHand()

        # Assert
        self.assertEqual(result, expected)

    def test_RemoveTileFromHand_TileInHand_TileRemoved(self) :
        # Arrange
        playerName = "Player One"
        hand = Hand(playerName)

        letter = 'A'
        value = 1
        tile = Tile(letter, value)

        hand.AddTileToHand(tile)
        beforeRemove = hand.PeekHand()
        self.assertIn(tile, beforeRemove)

        # Act
        hand.RemoveTileFromHand(tile)
        result = hand.PeekHand()

        # Assert
        self.assertNotIn(tile, result)

    def test_RemoveTileFromHand_TileNotInHand_RaisesException(self) :
        # Arrange
        playerName = "Player One"
        hand = Hand(playerName)

        letter = 'A'
        value = 1
        tile = Tile(letter, value)

        # Act & Asssert
        self.assertRaises(ValueError, hand.RemoveTileFromHand, tile)

    def test_CheckIfHandIsEmpty_HandIsEmpty_ReturnsTrue(self) :
         # Arrange
        playerName = "Player One"
        hand = Hand(playerName)

        # Act
        result = hand.IsHandEmpty()

        # Assert
        self.assertTrue(result)

    def test_CheckIfHandIsEmpty_HandIsNotEmpty_ReturnsFalse(self) :
         # Arrange
        playerName = "Player One"
        hand = Hand(playerName)

        letter = 'A'
        value = 1
        tile = Tile(letter, value)

        hand.AddTileToHand(tile)

        # Act
        result = hand.IsHandEmpty()

        # Assert
        self.assertFalse(result)
    
if __name__ == '__main__' :
    unittest.main()