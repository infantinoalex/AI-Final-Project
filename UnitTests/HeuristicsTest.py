import unittest
import os
import sys 
unitTestPath = os.path.dirname(__file__) + "/../Source"
sys.path.append(unitTestPath)

from Heuristics import *

class TestTilesClass(unittest.TestCase) :

    def test_HeuristicScoreWord_AnyWord_ReturnsZero(self) :
        # Arrange
        expected = 0
        hand = []
        word = "TEST"
        heuristic = Heuristic()

        # Act
        result = heuristic.ScoreWord(word, hand)

        # Assert
        self.assertEqual(result, expected)

    def test_LongestWordHeuristicScoreWord_FourLetterWord_ReturnsFour(self) :
        # Arrange
        expected = 4
        hand = []
        word = "FOUR"
        heuristic = LongestWordHeuristic()

        # Act
        result = heuristic.ScoreWord(word, hand)

        # Assert
        self.assertEqual(result, expected)

    def test_LetterScoringHeuristicScoreWord_A_ReturnsOne(self) :
        # Arrange
        expected = 1
        hand = []
        word = "A"
        heuristic = LetterScoringHeuristic()

        # Act
        result = heuristic.ScoreWord(word, hand)

        # Assert
        self.assertEqual(result, expected)

    def test_LetterScoringHeuristicScoreWord_QUEEN_ReturnsFourteen(self) :
        # Arrange
        expected = 14
        hand = []
        word = "QUEEN"
        heuristic = LetterScoringHeuristic()

        # Act
        result = heuristic.ScoreWord(word, hand)

        # Assert
        self.assertEqual(result, expected)

if __name__ == '__main__' :
    unittest.main()
