import os
import sys 
unitTestPath = os.path.dirname(__file__) + "/../Source"
sys.path.append(unitTestPath)

import unittest
from Word import Word 
from Tile import Tile

class TestWordClass(unittest.TestCase) :

        def test_Constructor_CallWithDefaultParameters_WordSetCorrectly(self) :

            # Arrange
            expectedTiles = None
            expectedString = ''
            expectedScore = 0
            expectedPrime = 1
            
            # Act
            testWord = Word()
            actualTiles = testWord.GetTiles()
            actualString = testWord.GetString()
            actualScore = testWord.GetScore()
            actualPrime = testWord.GetPrime()

            # Assert
            self.assertEqual(expectedTiles, actualTiles)
            self.assertEqual(expectedString, actualString)
            self.assertEqual(expectedScore, actualScore)
            self.assertEqual(expectedPrime, actualPrime)


        def test_Constructor_CallWithTiles_WordSetCorrectly(self) :

            # Arrange
            c = Tile('C', 3, 0.04049934678472928, 29)
            a = Tile('A', 1, 0.07633656680151722, 7)
            t = Tile('T', 1, 0.06566549066880407, 17)          
            expectedTiles = [c, a, t]
            expectedString = 'CAT'
            expectedScore = 5
            expectedPrime = 29 * 7 * 17

            # Act
            testWord = Word(expectedTiles)
            actualTiles = testWord.GetTiles()
            actualString = testWord.GetString()
            actualScore = testWord.GetScore()
            actualPrime = testWord.GetPrime()

            # Assert
            self.assertEqual(expectedTiles, actualTiles)
            self.assertEqual(expectedString, actualString)
            self.assertEqual(expectedScore, actualScore)
            self.assertEqual(expectedPrime, actualPrime)
            


if __name__ == '__main__' :
    unittest.main()
