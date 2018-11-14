import os
import sys 
unitTestPath = os.path.dirname(__file__) + "/../Source"
sys.path.append(unitTestPath)

import unittest
from Tile import Tile

class TestTilesClass(unittest.TestCase) :

    def test_GetLetter_ValidLetter_ReturnsLetter(self) :
        # Arrange
        letter = 'K'
        score = 2
        frequency = 1
        primeNumber = 1

        tile = Tile(letter, score, frequency, primeNumber)

        # Act
        result = tile.GetLetter()

        # Assert
        self.assertEqual(result, letter)

    def test_GetScore_ValidScore_ReturnsScore(self) :
        # Arrange
        letter = 'K'
        score = 2
        frequency = 1
        primeNumber = 1

        tile = Tile(letter, score, frequency, primeNumber)

        # Act
        result = tile.GetScore()

        # ASsert
        self.assertEqual(result, score)

    def test_IsVowel_LetterIsVowel_ReturnsTrue(self) :
        # Act
        letter = 'A'
        score = 2
        frequency = 1
        primeNumber = 1

        tile = Tile(letter, score, frequency, primeNumber)

        # Act
        result = tile.IsVowel()

        # Assert
        self.assertTrue(result) 

    def test_IsVowel_LetterIsConsonant_ReturnsFalse(self) :
        # Act
        letter = 'B'
        score = 2
        frequency = 1
        primeNumber = 1

        tile = Tile(letter, score, frequency, primeNumber)

        # Act
        result = tile.IsVowel()

        # Assert
        self.assertFalse(result) 

    def test_GetFrequency_ValidFrequency_ReturnsFrequency(self) :
        # Act
        letter = 'B'
        score = 2
        frequency = 1
        primeNumber = 1

        tile = Tile(letter, score, frequency, primeNumber)

        # Act
        result = tile.GetFrequency()

        # Assert
        self.assertEqual(frequency, result)

    def test_GetPrime_ValidPrimeNumber_ReturnsPrimeNumber(self) :
        # Act
        letter = 'B'
        score = 2
        frequency = 1
        primeNumber = 1

        tile = Tile(letter, score, frequency, primeNumber)

        # Act
        result = tile.GetPrime()

        # Assert
        self.assertEqual(primeNumber, result)

if __name__ == '__main__' :
    unittest.main()
