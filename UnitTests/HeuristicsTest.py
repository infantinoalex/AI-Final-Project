import unittest
import os
import sys 
unitTestPath = os.path.dirname(__file__) + "/../Source"
sys.path.append(unitTestPath)

from Heuristics import *
from Word import *
from Tile import *

class TestTilesClass(unittest.TestCase) :

    def test_HeuristicScoreWord_AnyWord_ReturnsZero(self) :
        # Arrange
        expected = 0
        hand = []
        word = "TEST"
        heuristic = NullHeuristic()

        # Act
        result = heuristic.ScoreWord(word, hand)

        # Assert
        self.assertEqual(result, expected)

    def test_LongestWordHeuristicScoreWord_FourLetterWord_ReturnsFour(self) :
        # Arrange
        expected = 4
        hand = []
        f = "F"
        o = "O"
        u = "U"
        r = "R"
        tiles = []
        fTile = Tile(f)
        oTile = Tile(o)
        uTile = Tile(u)
        rTile = Tile(r)
        tiles.append(fTile)
        tiles.append(oTile)
        tiles.append(uTile)
        tiles.append(rTile)
        word = Word(tiles)
        heuristic = LongestWordHeuristic()

        # Act
        result = heuristic.ScoreWord(word, hand)

        # Assert
        self.assertEqual(result, expected)

    def test_LetterScoringHeuristicScoreWord_A_ReturnsOne(self) :
        # Arrange
        expected = 1
        hand = []
        letter = "A"
        wordTile = Tile(letter)
        tiles = []
        tiles.append(wordTile)
        word = Word(tiles)
        heuristic = LetterScoringHeuristic()

        # Act
        result = heuristic.ScoreWord(word, hand)

        # Assert
        self.assertEqual(result, expected)

    def test_LetterScoringHeuristicScoreWord_QUEEN_ReturnsFourteen(self) :
        # Arrange
        expected = 14
        hand = []
        q = "Q"
        u = "U"
        e = "E"
        n = "N"
        tiles = []
        qTile = Tile(q)
        uTile = Tile(u)
        eTile = Tile(e)
        nTile = Tile(n)
        tiles.append(qTile)
        tiles.append(uTile)
        tiles.append(eTile)
        tiles.append(eTile)
        tiles.append(nTile)
        word = Word(tiles)
        heuristic = LetterScoringHeuristic()

        # Act
        result = heuristic.ScoreWord(word, hand)

        # Assert
        self.assertEqual(result, expected)

if __name__ == '__main__' :
    unittest.main()
