import unittest
import os
import sys 
unitTestPath = os.path.dirname(__file__) + "/../Source"
sys.path.append(unitTestPath)

from Hand import Hand
from Tile import Tile

class TestHandClass(unittest.TestCase) :

    def test_GetPlayerName_ValidName_ReturnsName(self) :
        # Arrange
        playerName = "Player One"
        tiles = []
        tile = Tile('A', 1, 1, 1)
        tiles.append(tile)
        hand = Hand(playerName, tiles)

        # Act
        result = hand.GetPlayerName()

        # Assert
        self.assertEqual(result, playerName)

    def test_PeekHand_EmptyHand_ReturnsFalse(self) :
        # Arrange
        playerName = "Player One"
        tiles = []
        hand = Hand(playerName, tiles)

        # Act
        result = hand.PeekHand()

        # Assert
        self.assertFalse(result)

    def test_AddTileToHand_ValidTile_TileInHand(self) :
        # Arrange
        playerName = "Player One"
        tiles = []
        hand = Hand(playerName, tiles)

        letter = 'A'
        value = 1
        frequency = 1
        primeNumber = 1
        tile = Tile(letter, value, frequency, primeNumber)

        # Act
        hand.AddTileToHand(tile)
        result = hand.PeekHand()

        # Assert
        self.assertIn(tile, result)

    def test_AddTilesToHand_ValidTiles_TilesInHand(self) :
        # Arrange
        playerName = "Player One"
        tiles = []
        hand = Hand(playerName, tiles)

        letterA = 'A'
        valueA = 1
        frequencyA = 1
        primeNumberA = 1
        tileA = Tile(letterA, valueA, frequencyA, primeNumberA)

        letterB = 'B'
        valueB = 2
        frequencyB = 1
        primeNumberB = 1
        tileB = Tile(letterB, valueB, frequencyB, primeNumberB)

        expected = [tileA, tileB]

        # Act
        hand.AddTilesToHand(expected)
        result = hand.PeekHand()

        # Assert
        self.assertEqual(result, expected)

    def test_RemoveTileFromHand_TileInHand_TileRemoved(self) :
        # Arrange
        playerName = "Player One"
        tiles = []
        letter = 'A'
        value = 1
        frequency = 1
        primeNumber = 1
        tile = Tile(letter, value, frequency, primeNumber)
        tiles.append(tile)
        hand = Hand(playerName, tiles)

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
        tiles = []
        hand = Hand(playerName, tiles)

        letter = 'A'
        value = 1
        frequency = 1
        primeNumber = 1
        tile = Tile(letter, value, frequency, primeNumber)

        # Act & Asssert
        self.assertRaises(ValueError, hand.RemoveTileFromHand, tile)

    def test_CheckIfHandIsEmpty_HandIsEmpty_ReturnsTrue(self) :
         # Arrange
        playerName = "Player One"
        tiles = []
        hand = Hand(playerName, tiles)

        # Act
        result = hand.IsHandEmpty()

        # Assert
        self.assertTrue(result)

    def test_CheckIfHandIsEmpty_HandIsNotEmpty_ReturnsFalse(self) :
         # Arrange
        playerName = "Player One"
        tiles = []
        letter = 'A'
        value = 1
        frequency = 1
        primeNumber = 1
        tile = Tile(letter, value, frequency, primeNumber)
        tiles.append(tile)
        hand = Hand(playerName, tiles)

        # Act
        result = hand.IsHandEmpty()

        # Assert
        self.assertFalse(result)
    
if __name__ == '__main__' :
    unittest.main()