import os
import sys 
unitTestPath = os.path.dirname(__file__) + "/../Source"
sys.path.append(unitTestPath)

import unittest
from Board import Board 
from Tile import Tile
from Word import Word

class TestBoardClass(unittest.TestCase) :

    '''
    These tests verify that the PlaceWord function works
    '''

    def test_PlaceWord_DefaultAnchorAcross_WordPlacedCorrectly(self) :

        # Arrange
        board = Board()
        t = Tile('t', -1, -1.0, -1)
        e = Tile('e', -1, -1.0, -1)
        s = Tile('s', -1, -1.0, -1)
        i = Tile('i', -1, -1.0, -1)
        n = Tile('n', -1, -1.0, -1)
        g = Tile('g', -1, -1.0, -1)

        word = Word([t, e, s, t, i, n, g])

        # Act
        board.PlaceWord(word, board.GetAnchors()[0], 3, 'across')

        # Assert 
        # board.PrintBoard()
        self.assertEqual(board.GetBoard()[7, 10].GetLetter(), t.GetLetter())
        self.assertEqual(board.GetBoard()[8, 10].GetLetter(), e.GetLetter())
        self.assertEqual(board.GetBoard()[9, 10].GetLetter(), s.GetLetter())
        self.assertEqual(board.GetBoard()[10, 10].GetLetter(), t.GetLetter())
        self.assertEqual(board.GetBoard()[11, 10].GetLetter(), i.GetLetter())
        self.assertEqual(board.GetBoard()[12, 10].GetLetter(), n.GetLetter())
        self.assertEqual(board.GetBoard()[13, 10].GetLetter(), g.GetLetter())

    def test_PlaceWord_DefaultAnchorDown_WordPlacedCorrectly(self) :

        # Arrange
        board = Board()
        t = Tile('t', -1, -1.0, -1)
        e = Tile('e', -1, -1.0, -1)
        s = Tile('s', -1, -1.0, -1)
        i = Tile('i', -1, -1.0, -1)
        n = Tile('n', -1, -1.0, -1)
        g = Tile('g', -1, -1.0, -1)

        word = Word([t, e, s, t, i, n, g])

        # Act
        board.PlaceWord(word, board.GetAnchors()[0], 3, 'down')

        # Assert 
        # board.PrintBoard()
        self.assertEqual(board.GetBoard()[10, 7].GetLetter(), t.GetLetter())
        self.assertEqual(board.GetBoard()[10, 8].GetLetter(), e.GetLetter())
        self.assertEqual(board.GetBoard()[10, 9].GetLetter(), s.GetLetter())
        self.assertEqual(board.GetBoard()[10, 10].GetLetter(), t.GetLetter())
        self.assertEqual(board.GetBoard()[10, 11].GetLetter(), i.GetLetter())
        self.assertEqual(board.GetBoard()[10, 12].GetLetter(), n.GetLetter())
        self.assertEqual(board.GetBoard()[10, 13].GetLetter(), g.GetLetter())

    def test_PlaceWord_OneLetterAnchorAcross_WordPlacedCorrectly(self) :

        # Arrange
        board = Board()
        t = Tile('t', -1, -1.0, -1)
        e = Tile('e', -1, -1.0, -1)
        s = Tile('s', -1, -1.0, -1)
        i = Tile('i', -1, -1.0, -1)
        n = Tile('n', -1, -1.0, -1)
        g = Tile('g', -1, -1.0, -1)

        word = Word([t, e, s, t, i, n, g])

        # Act
        board.PlaceWord(word, board.GetAnchors()[0], 3, 'down')
        board.PlaceWord(word, board.GetAnchors()[3], 0, 'across')

        # Assert 
        # board.PrintBoard()
        self.assertEqual(board.GetBoard()[10, 10].GetLetter(), t.GetLetter())
        self.assertEqual(board.GetBoard()[11, 10].GetLetter(), e.GetLetter())
        self.assertEqual(board.GetBoard()[12, 10].GetLetter(), s.GetLetter())
        self.assertEqual(board.GetBoard()[13, 10].GetLetter(), t.GetLetter())
        self.assertEqual(board.GetBoard()[14, 10].GetLetter(), i.GetLetter())
        self.assertEqual(board.GetBoard()[15, 10].GetLetter(), n.GetLetter())
        self.assertEqual(board.GetBoard()[16, 10].GetLetter(), g.GetLetter())

    def test_PlaceWord_OneLetterAnchorDown_WordPlacedCorrectly(self) :

        # Arrange
        board = Board()
        t = Tile('t', -1, -1.0, -1)
        e = Tile('e', -1, -1.0, -1)
        s = Tile('s', -1, -1.0, -1)
        i = Tile('i', -1, -1.0, -1)
        n = Tile('n', -1, -1.0, -1)
        g = Tile('g', -1, -1.0, -1)

        word = Word([t, e, s, t, i, n, g])

        # Act
        board.PlaceWord(word, board.GetAnchors()[0], 3, 'across')
        board.PlaceWord(word, board.GetAnchors()[3], 0, 'down')

        # Assert 
        # board.PrintBoard()
        self.assertEqual(board.GetBoard()[10, 10].GetLetter(), t.GetLetter())
        self.assertEqual(board.GetBoard()[10, 11].GetLetter(), e.GetLetter())
        self.assertEqual(board.GetBoard()[10, 12].GetLetter(), s.GetLetter())
        self.assertEqual(board.GetBoard()[10, 13].GetLetter(), t.GetLetter())
        self.assertEqual(board.GetBoard()[10, 14].GetLetter(), i.GetLetter())
        self.assertEqual(board.GetBoard()[10, 15].GetLetter(), n.GetLetter())
        self.assertEqual(board.GetBoard()[10, 16].GetLetter(), g.GetLetter())

    '''
    These tests verify that the IsWordLegal happy path works
    '''

    def test_IsWordLegal_LegalWordDefaultAnchorAcross_ReturnsTrue(self) :

        # Arrange
        board = Board()
        t = Tile('t', -1, -1.0, -1)
        e = Tile('e', -1, -1.0, -1)
        s = Tile('s', -1, -1.0, -1)
        i = Tile('i', -1, -1.0, -1)
        n = Tile('n', -1, -1.0, -1)
        g = Tile('g', -1, -1.0, -1)

        word = Word([t, e, s, t, i, n, g])

        # Act
        results = board.IsWordLegal(word, board.GetAnchors()[0], 3, 'across')

        # Assert 
        self.assertTrue(results[0])

    def test_IsWordLegal_LegalWordDefaultAnchorDown_ReturnsTrue(self) :

        # Arrange
        board = Board()
        t = Tile('t', -1, -1.0, -1)
        e = Tile('e', -1, -1.0, -1)
        s = Tile('s', -1, -1.0, -1)
        i = Tile('i', -1, -1.0, -1)
        n = Tile('n', -1, -1.0, -1)
        g = Tile('g', -1, -1.0, -1)

        word = Word([t, e, s, t, i, n, g])

        # Act
        results = board.IsWordLegal(word, board.GetAnchors()[0], 3, 'down')

        # Assert 
        self.assertTrue(results[0])

    def test_IsWordLegal_LegalWordOneLetterAnchorAcross_ReturnsTrue(self) :

        # Arrange
        board = Board()
        t = Tile('t', -1, -1.0, -1)
        e = Tile('e', -1, -1.0, -1)
        s = Tile('s', -1, -1.0, -1)
        i = Tile('i', -1, -1.0, -1)
        n = Tile('n', -1, -1.0, -1)
        g = Tile('g', -1, -1.0, -1)

        word = Word([t, e, s, t, i, n, g])

        # Act
        board.PlaceWord(word, board.GetAnchors()[0], 3, 'down')
        results = board.IsWordLegal(word, board.GetAnchors()[3], 0, 'across')

        # Assert 
        self.assertTrue(results[0])
    
    def test_IsWordLegal_LegalWordOneLetterAnchorDown_ReturnsTrue(self) :

        # Arrange
        board = Board()
        t = Tile('t', -1, -1.0, -1)
        e = Tile('e', -1, -1.0, -1)
        s = Tile('s', -1, -1.0, -1)
        i = Tile('i', -1, -1.0, -1)
        n = Tile('n', -1, -1.0, -1)
        g = Tile('g', -1, -1.0, -1)

        word = Word([t, e, s, t, i, n, g])

        # Act
        board.PlaceWord(word, board.GetAnchors()[0], 3, 'across')
        results = board.IsWordLegal(word, board.GetAnchors()[3], 0, 'down')

        # Assert 
        self.assertTrue(results[0])
    
    '''
    These tests verify that the IsWordLegal function returns false 
    when a word is not big enough
    '''

    def test_IsWordLegal_0CharacterWordDefaultAnchor_ReturnsFalseTooSmall(self) :

        # Arrange
        board = Board()
        word = Word()

        # Act
        results = board.IsWordLegal(word, board.GetAnchors()[0], 0, 'across')

        # Assert 
        self.assertFalse(results[0])
        self.assertTrue(results[1], 'word not big enough')

        # Arrange
        board = Board()
        word = Word()

        # Act
        results = board.IsWordLegal(word, board.GetAnchors()[0], 0, 'down')

        # Assert 
        self.assertFalse(results[0])
        self.assertTrue(results[1], 'word not big enough')

    def test_IsWordLegal_0CharacterWordOneLetterAnchor_ReturnsFalseTooSmall(self) :

        # Arrange
        board = Board()
        t = Tile('t', -1, -1.0, -1)
        e = Tile('e', -1, -1.0, -1)
        s = Tile('s', -1, -1.0, -1)
        i = Tile('i', -1, -1.0, -1)
        n = Tile('n', -1, -1.0, -1)
        g = Tile('g', -1, -1.0, -1)

        word1 = Word([t, e, s, t, i, n, g])
        word2 = Word()

        # Act
        board.PlaceWord(word1, board.GetAnchors()[0], 3, 'down')
        results = board.IsWordLegal(word2, board.GetAnchors()[3], 0, 'across')

        # Assert 
        self.assertFalse(results[0])
        self.assertTrue(results[1], 'word not big enough')


    def test_IsWordLegal_1CharacterWordDefaultAnchor_ReturnsFalseTooSmall(self) :

        # Arrange
        board = Board()
        t = Tile('t', -1, -1.0, -1)
        word = Word([t])

        # Act
        results = board.IsWordLegal(word, board.GetAnchors()[0], 0, 'across')

        # Assert 
        self.assertFalse(results[0])
        self.assertTrue(results[1], 'word not big enough')

    def test_IsWordLegal_1CharacterWordOneLetterAnchor_ReturnsFalseTooSmall(self) :

        # Arrange
        board = Board()
        t = Tile('t', -1, -1.0, -1)
        e = Tile('e', -1, -1.0, -1)
        s = Tile('s', -1, -1.0, -1)
        i = Tile('i', -1, -1.0, -1)
        n = Tile('n', -1, -1.0, -1)
        g = Tile('g', -1, -1.0, -1)

        word1 = Word([t, e, s, t, i, n, g])
        word2 = Word([t])

        # Act
        board.PlaceWord(word1, board.GetAnchors()[0], 3, 'down')
        results = board.IsWordLegal(word2, board.GetAnchors()[3], 0, 'across')

        # Assert 
        self.assertFalse(results[0])
        self.assertTrue(results[1], 'word not big enough')


        # Arrange
        board = Board()
        t = Tile('t', -1, -1.0, -1)
        e = Tile('e', -1, -1.0, -1)
        s = Tile('s', -1, -1.0, -1)
        i = Tile('i', -1, -1.0, -1)
        n = Tile('n', -1, -1.0, -1)
        g = Tile('g', -1, -1.0, -1)

        word1 = Word([t, e, s, t, i, n, g])
        word2 = Word([t])

        # Act
        board.PlaceWord(word1, board.GetAnchors()[0], 3, 'across')
        results = board.IsWordLegal(word2, board.GetAnchors()[3], 0, 'down')

        # Assert 
        self.assertFalse(results[0])
        self.assertTrue(results[1], 'word not big enough')

    '''
    These tests verify that the IsWordLegal function returns false 
    when a word goes off the board
    '''

    def test_IsWordLegal_OffBoardWordDefaultAnchorAcross_ReturnsFalseOffBoard(self) :

        # Arrange
        board = Board()
        t = Tile('t', -1, -1.0, -1)
        word = Word([t, t, t, t, t, t, t, t, t, t, t, t, t, t, t])

        # Act
        results = board.IsWordLegal(word, board.GetAnchors()[0], 0, 'across')

        # Assert 
        self.assertFalse(results[0])
        self.assertTrue(results[1], 'word goes off the board')

    def test_IsWordLegal_OffBoardWordDefaultAnchorDown_ReturnsFalseOffBoard(self) :

        # Arrange
        board = Board()
        t = Tile('t', -1, -1.0, -1)
        word = Word([t, t, t, t, t, t, t, t, t, t, t, t, t, t, t])

        # Act
        results = board.IsWordLegal(word, board.GetAnchors()[0], 0, 'down')

        # Assert 
        self.assertFalse(results[0])
        self.assertTrue(results[1], 'word goes off the board')

    def test_IsWordLegal_OffBoardWordOneLetterAnchorAcross_ReturnsFalseOffBoard(self) :

        # Arrange
        board = Board()
        t = Tile('t', -1, -1.0, -1)
        e = Tile('e', -1, -1.0, -1)
        s = Tile('s', -1, -1.0, -1)
        i = Tile('i', -1, -1.0, -1)
        n = Tile('n', -1, -1.0, -1)
        g = Tile('g', -1, -1.0, -1)

        word1 = Word([t, e, s, t, i, n, g])
        word2 = Word([t, t, t, t, t, t, t, t, t, t, t, t, t, t, t])

        # Act
        board.PlaceWord(word1, board.GetAnchors()[0], 3, 'down')
        results = board.IsWordLegal(word2, board.GetAnchors()[3], 0, 'across')

        # Assert 
        self.assertFalse(results[0])
        self.assertTrue(results[1], 'word goes off the board')

    def test_IsWordLegal_OffBoardWordOneLetterAnchorDown_ReturnsFalseOffBoard(self) :

        # Arrange
        board = Board()
        t = Tile('t', -1, -1.0, -1)
        e = Tile('e', -1, -1.0, -1)
        s = Tile('s', -1, -1.0, -1)
        i = Tile('i', -1, -1.0, -1)
        n = Tile('n', -1, -1.0, -1)
        g = Tile('g', -1, -1.0, -1)

        word1 = Word([t, e, s, t, i, n, g])
        word2 = Word([t, t, t, t, t, t, t, t, t, t, t, t, t, t, t])

        # Act
        board.PlaceWord(word1, board.GetAnchors()[0], 3, 'across')
        results = board.IsWordLegal(word2, board.GetAnchors()[3], 0, 'down')

        # Assert 
        self.assertFalse(results[0])
        self.assertTrue(results[1], 'word goes off the board')

    '''
    These tests verify that the IsWordLegal function returns false 
    when the anchorIndex is not correct
    '''

    def test_IsWordLegal_OutOfRangeAnchorIndexWordOneLetterAnchor_ReturnsFalseBadAnchorIndex(self) :

        # Arrange
        board = Board()
        t = Tile('t', -1, -1.0, -1)
        e = Tile('e', -1, -1.0, -1)
        s = Tile('s', -1, -1.0, -1)
        i = Tile('i', -1, -1.0, -1)
        n = Tile('n', -1, -1.0, -1)
        g = Tile('g', -1, -1.0, -1)

        word = Word([t, e, s, t, i, n, g])

        # Act
        board.PlaceWord(word, board.GetAnchors()[0], 3, 'down')
        results = board.IsWordLegal(word, board.GetAnchors()[3], 12, 'across')

        # Assert 
        self.assertFalse(results[0])
        self.assertTrue(results[1], 'anchorIndex is invalid')

    def test_IsWordLegal_BadAnchorIndexWordOneLetterAnchor_ReturnsFalseBadAnchorIndex(self) :

        # Arrange
        board = Board()
        t = Tile('t', -1, -1.0, -1)
        e = Tile('e', -1, -1.0, -1)
        s = Tile('s', -1, -1.0, -1)
        i = Tile('i', -1, -1.0, -1)
        n = Tile('n', -1, -1.0, -1)
        g = Tile('g', -1, -1.0, -1)

        word = Word([t, e, s, t, i, n, g])

        # Act
        board.PlaceWord(word, board.GetAnchors()[0], 3, 'down')
        results = board.IsWordLegal(word, board.GetAnchors()[3], 2, 'across')

        # Assert 
        self.assertFalse(results[0])
        self.assertTrue(results[1], 'anchorIndex is invalid')

    '''
    These tests verify that the IsWordLegal function returns false
    when there is not space on the board for the word (aka it directly 
    overlays a tile which does not allow the word to be played)
    and true otherwise
    '''

    def test_IsWordLegal_LegalWordWithOverlapOneLetterAnchorAcross_ReturnsTrue(self) :

        # Arrange
        board = Board()
        a = Tile('a', 1, 0.07633656680151722, 7)
        c = Tile('c', 3, 0.04049934678472928, 29)
        d = Tile('d', 2, 0.03463176961381408, 31)
        e = Tile('e', 1, 0.11533383402651991, 2)
        g = Tile('g', 2, 0.02747732680328438, 47)
        i = Tile('i', 1, 0.0885545324304026, 5)
        k = Tile('k', 5, 0.009120399881348338, 73)
        n = Tile('n', 1, 0.06738530865210449, 13)
        r = Tile('r', 1, 0.07098146383333229, 11)
        v = Tile('v', 4, 0.009737640977740191, 71)
        w = Tile('w', 4, 0.007837320996926416, 79)
        y = Tile('y', 4, 0.016327226138708843, 61)

        weekend = Word([w, e, e, k, e, n, d])
        waiver = Word([w, a, i, v, e, r])
        eggy = Word([e, g, g, y])
        crying = Word([c, r, y, i, n, g])

        # Act
        board.PlaceWord(weekend, board.GetAnchors()[0], 3, 'across')
        board.PlaceWord(waiver, board.GetAnchors()[0], 0, 'down')
        board.PlaceWord(eggy, board.GetAnchors()[1], 0, 'down')
        results = board.IsWordLegal(crying, board.GetAnchors()[8], 3, 'across')

        # Assert 
        # board.PrintBoard()
        self.assertTrue(results[0])
    
    def test_IsWordLegal_LegalWordWithOverlapOneLetterAnchorDown_ReturnsTrue(self) :

        # Arrange
        board = Board()
        a = Tile('a', 1, 0.07633656680151722, 7)
        c = Tile('c', 3, 0.04049934678472928, 29)
        d = Tile('d', 2, 0.03463176961381408, 31)
        e = Tile('e', 1, 0.11533383402651991, 2)
        g = Tile('g', 2, 0.02747732680328438, 47)
        i = Tile('i', 1, 0.0885545324304026, 5)
        k = Tile('k', 5, 0.009120399881348338, 73)
        n = Tile('n', 1, 0.06738530865210449, 13)
        r = Tile('r', 1, 0.07098146383333229, 11)
        v = Tile('v', 4, 0.009737640977740191, 71)
        w = Tile('w', 4, 0.007837320996926416, 79)
        y = Tile('y', 4, 0.016327226138708843, 61)
        weekend = Word([w, e, e, k, e, n, d])
        waiver = Word([w, a, i, v, e, r])
        eggy = Word([e, g, g, y])
        crying = Word([c, r, y, i, n, g])

        # Act
        board.PlaceWord(weekend, board.GetAnchors()[0], 3, 'across')
        board.PlaceWord(waiver, board.GetAnchors()[0], 0, 'down')
        board.PlaceWord(crying, board.GetAnchors()[9], 3, 'across')
        results = board.IsWordLegal(eggy, board.GetAnchors()[1], 0, 'down')

        # Assert 
        self.assertTrue(results[0])
        
    def test_IsWordLegal_IllegalWordWithOverlapOneLetterAnchorAcross_ReturnsFalseWordFit(self) :

        # Arrange
        board = Board()
        a = Tile('a', 1, 0.07633656680151722, 7)
        d = Tile('d', 2, 0.03463176961381408, 31)
        e = Tile('e', 1, 0.11533383402651991, 2)
        g = Tile('g', 2, 0.02747732680328438, 47)
        i = Tile('i', 1, 0.0885545324304026, 5)
        k = Tile('k', 5, 0.009120399881348338, 73)
        n = Tile('n', 1, 0.06738530865210449, 13)
        r = Tile('r', 1, 0.07098146383333229, 11)
        v = Tile('v', 4, 0.009737640977740191, 71)
        w = Tile('w', 4, 0.007837320996926416, 79)
        y = Tile('y', 4, 0.016327226138708843, 61)
        weekend = Word([w, e, e, k, e, n, d])
        waiver = Word([w, a, i, v, e, r])
        eggy = Word([e, g, g, y])
        rink = Word([r, i, n, k])

        # Act
        board.PlaceWord(weekend, board.GetAnchors()[0], 3, 'across')
        board.PlaceWord(waiver, board.GetAnchors()[0], 0, 'down')
        board.PlaceWord(eggy, board.GetAnchors()[1], 0, 'down')
        results = board.IsWordLegal(rink, board.GetAnchors()[8], 1, 'across')

        # Assert 
        self.assertFalse(results[0])
        self.assertEqual(results[1], 'word does not fit in the board correctly')
    
    def test_IsWordLegal_IllegalWordWithOverlapOneLetterAnchorDown_ReturnsFalseWordFit(self) :

        # Arrange
        board = Board()
        a = Tile('a', 1, 0.07633656680151722, 7)
        d = Tile('d', 2, 0.03463176961381408, 31)
        e = Tile('e', 1, 0.11533383402651991, 2)
        g = Tile('g', 2, 0.02747732680328438, 47)
        i = Tile('i', 1, 0.0885545324304026, 5)
        k = Tile('k', 5, 0.009120399881348338, 73)
        n = Tile('n', 1, 0.06738530865210449, 13)
        r = Tile('r', 1, 0.07098146383333229, 11)
        v = Tile('v', 4, 0.009737640977740191, 71)
        w = Tile('w', 4, 0.007837320996926416, 79)
        y = Tile('y', 4, 0.016327226138708843, 61)
        weekend = Word([w, e, e, k, e, n, d])
        waiver = Word([w, a, i, v, e, r])
        eggy = Word([e, g, g, y])
        rink = Word([r, i, n, k])

        # Act
        board.PlaceWord(weekend, board.GetAnchors()[0], 3, 'across')
        board.PlaceWord(waiver, board.GetAnchors()[0], 0, 'down')
        board.PlaceWord(rink, board.GetAnchors()[9], 1, 'across')
        results = board.IsWordLegal(eggy, board.GetAnchors()[1], 0, 'down')

        # Assert 
        # board.PrintBoard()
        self.assertFalse(results[0])
        self.assertEqual(results[1], 'word does not fit in the board correctly')
    
    '''
    These tests verify that the IsWordLegal function returns false when
    the word that gets played creates an invalid word from the tiles
    surrounding the area where the word is played and true otherwise
    '''

    def test_IsWordLegal_LegalWordAddPrefixOneLetterAnchorAcross_ReturnsTrue(self) :

        # Arrange
        board = Board()
        b = Tile('b', 3, 0.019012035570253775, 59)
        e = Tile('e', 1, 0.11533383402651991, 2)      
        i = Tile('i', 1, 0.0885545324304026, 5)
        g = Tile('g', 2, 0.02747732680328438, 47)
        k = Tile('k', 5, 0.009120399881348338, 73)
        l = Tile('l', 1, 0.05340397735520395, 23)
        n = Tile('n', 1, 0.06738530865210449, 13)
        o = Tile('o', 1, 0.0653196336945477, 19)
        r = Tile('r', 1, 0.07098146383333229, 11)
        s = Tile('s', 1, 0.09480520300163461, 3)

        linkers = Word([l, i, n, k, e, r, s])
        belies = Word([b, e, l, i, e, s])
        nose = Word([n, o, s, e])
        ring = Word([r, i, n, g])     

        # Act
        board.PlaceWord(linkers, board.GetAnchors()[0], 3, 'across')
        board.PlaceWord(belies, board.GetAnchors()[1], 3, 'down')
        board.PlaceWord(nose, board.GetAnchors()[3], 3, 'down')
        results = board.IsWordLegal(ring, board.GetAnchors()[13], 2, 'across')
        
        # Assert 
        # board.PrintBoard()
        self.assertTrue(results[0])

    def test_IsWordLegal_LegalWordAddSuffixOneLetterAnchorAcross_ReturnsTrue(self) :

        # Arrange
        board = Board()
        a = Tile('a', 1, 0.07633656680151722, 7)
        b = Tile('b', 3, 0.019012035570253775, 59)
        e = Tile('e', 1, 0.11533383402651991, 2)      
        f = Tile('f', 4, 0.0126414510845898, 67)
        i = Tile('i', 1, 0.0885545324304026, 5)
        g = Tile('g', 2, 0.02747732680328438, 47)
        k = Tile('k', 5, 0.009120399881348338, 73)
        l = Tile('l', 1, 0.05340397735520395, 23)
        n = Tile('n', 1, 0.06738530865210449, 13)
        o = Tile('o', 1, 0.0653196336945477, 19)
        r = Tile('r', 1, 0.07098146383333229, 11)
        s = Tile('s', 1, 0.09480520300163461, 3)
        t = Tile('t', 1, 0.06566549066880407, 17)

        linkers = Word([l, i, n, k, e, r, s])
        nose = Word([n, o, s, e])
        fastest = Word([f, a, s, t, e, s, t])
        ring = Word([r, i, n, g])
        
        # Act
        board.PlaceWord(linkers, board.GetAnchors()[0], 3, 'across')
        board.PlaceWord(nose, board.GetAnchors()[4], 3, 'down')
        board.PlaceWord(fastest, board.GetAnchors()[5], 5, 'down')
        results = board.IsWordLegal(ring, board.GetAnchors()[6], 2, 'across')
        
        # Assert 
        # board.PrintBoard()
        self.assertTrue(results[0])

    def test_IsWordLegal_LegalWordAddPrefixAndSuffixOneLetterAnchorAcross_ReturnsTrue(self) :

        # Arrange
        board = Board()
        a = Tile('a', 1, 0.07633656680151722, 7)
        b = Tile('b', 3, 0.019012035570253775, 59)
        e = Tile('e', 1, 0.11533383402651991, 2)      
        f = Tile('f', 4, 0.0126414510845898, 67)
        i = Tile('i', 1, 0.0885545324304026, 5)
        g = Tile('g', 2, 0.02747732680328438, 47)
        k = Tile('k', 5, 0.009120399881348338, 73)
        l = Tile('l', 1, 0.05340397735520395, 23)
        n = Tile('n', 1, 0.06738530865210449, 13)
        o = Tile('o', 1, 0.0653196336945477, 19)
        r = Tile('r', 1, 0.07098146383333229, 11)
        s = Tile('s', 1, 0.09480520300163461, 3)
        t = Tile('t', 1, 0.06566549066880407, 17)

        linkers = Word([l, i, n, k, e, r, s])
        belies = Word([b, e, l, i, e, s])
        nose = Word([n, o, s, e])
        fastest = Word([f, a, s, t, e, s, t])
        ring = Word([r, i, n, g])
        

        # Act
        board.PlaceWord(linkers, board.GetAnchors()[0], 3, 'across')
        board.PlaceWord(belies, board.GetAnchors()[1], 3, 'down')
        board.PlaceWord(nose, board.GetAnchors()[3], 3, 'down')
        board.PlaceWord(fastest, board.GetAnchors()[4], 5, 'down')
        results = board.IsWordLegal(ring, board.GetAnchors()[12], 2, 'across')
        
        # Assert 
        # board.PrintBoard()
        self.assertTrue(results[0])


    def test_IsWordLegal_IllegalWordBadPrefixOneLetterAnchorAcross_ReturnsFalse(self) :

        # Arrange
        board = Board()
        b = Tile('b', 3, 0.019012035570253775, 59)
        e = Tile('e', 1, 0.11533383402651991, 2)      
        i = Tile('i', 1, 0.0885545324304026, 5)
        g = Tile('g', 2, 0.02747732680328438, 47)
        k = Tile('k', 5, 0.009120399881348338, 73)
        l = Tile('l', 1, 0.05340397735520395, 23)
        n = Tile('n', 1, 0.06738530865210449, 13)
        o = Tile('o', 1, 0.0653196336945477, 19)
        r = Tile('r', 1, 0.07098146383333229, 11)
        s = Tile('s', 1, 0.09480520300163461, 3)

        linkers = Word([l, i, n, k, e, r, s])
        belies = Word([b, e, l, i, e, s])
        nose = Word([n, o, s, e])
        sing = Word([s, i, n, g])     

        # Act
        board.PlaceWord(linkers, board.GetAnchors()[0], 3, 'across')
        board.PlaceWord(belies, board.GetAnchors()[1], 3, 'down')
        board.PlaceWord(nose, board.GetAnchors()[3], 3, 'down')
        results = board.IsWordLegal(sing, board.GetAnchors()[13], 2, 'across')
        
        # Assert 
        self.assertFalse(results[0])
        self.assertEqual(results[1], 'word creates an invalid word when placed')

    def test_IsWordLegal_IllegalWordBadSuffixOneLetterAnchorAcross_ReturnsFalse(self) :

        # Arrange
        board = Board()
        a = Tile('a', 1, 0.07633656680151722, 7)
        b = Tile('b', 3, 0.019012035570253775, 59)
        e = Tile('e', 1, 0.11533383402651991, 2)      
        f = Tile('f', 4, 0.0126414510845898, 67)
        i = Tile('i', 1, 0.0885545324304026, 5)
        g = Tile('g', 2, 0.02747732680328438, 47)
        k = Tile('k', 5, 0.009120399881348338, 73)
        l = Tile('l', 1, 0.05340397735520395, 23)
        n = Tile('n', 1, 0.06738530865210449, 13)
        o = Tile('o', 1, 0.0653196336945477, 19)
        r = Tile('r', 1, 0.07098146383333229, 11)
        s = Tile('s', 1, 0.09480520300163461, 3)
        t = Tile('t', 1, 0.06566549066880407, 17)

        linkers = Word([l, i, n, k, e, r, s])
        nose = Word([n, o, s, e])
        fattest = Word([f, a, t, t, e, s, t])
        ring = Word([r, i, n, g])
        
        # Act
        board.PlaceWord(linkers, board.GetAnchors()[0], 3, 'across')
        board.PlaceWord(nose, board.GetAnchors()[4], 3, 'down')
        board.PlaceWord(fattest, board.GetAnchors()[5], 5, 'down')
        results = board.IsWordLegal(ring, board.GetAnchors()[6], 2, 'across')
        
        # Assert 
        self.assertFalse(results[0])
        self.assertEqual(results[1], 'word creates an invalid word when placed')

    def test_IsWordLegal_IllegalWordBadPrefixAndSuffixOneLetterAnchorAcross_ReturnsFalse(self) :

        # Arrange
        board = Board()
        a = Tile('a', 1, 0.07633656680151722, 7)
        b = Tile('b', 3, 0.019012035570253775, 59)
        e = Tile('e', 1, 0.11533383402651991, 2)      
        f = Tile('f', 4, 0.0126414510845898, 67)
        i = Tile('i', 1, 0.0885545324304026, 5)
        g = Tile('g', 2, 0.02747732680328438, 47)
        k = Tile('k', 5, 0.009120399881348338, 73)
        l = Tile('l', 1, 0.05340397735520395, 23)
        n = Tile('n', 1, 0.06738530865210449, 13)
        o = Tile('o', 1, 0.0653196336945477, 19)
        r = Tile('r', 1, 0.07098146383333229, 11)
        s = Tile('s', 1, 0.09480520300163461, 3)
        t = Tile('t', 1, 0.06566549066880407, 17)

        linkers = Word([l, i, n, k, e, r, s])
        belies = Word([b, e, l, i, e, s])
        nose = Word([n, o, s, e])
        fattest = Word([f, a, t, t, e, s, t])
        sing = Word([s, i, n, g])
        

        # Act
        board.PlaceWord(linkers, board.GetAnchors()[0], 3, 'across')
        board.PlaceWord(belies, board.GetAnchors()[1], 3, 'down')
        board.PlaceWord(nose, board.GetAnchors()[3], 3, 'down')
        board.PlaceWord(fattest, board.GetAnchors()[4], 5, 'down')
        results = board.IsWordLegal(sing, board.GetAnchors()[12], 2, 'across')
        
        # Assert 
        self.assertFalse(results[0])
        self.assertEqual(results[1], 'word creates an invalid word when placed')

  
    def test_IsWordLegal_LegalWordAddPrefixOneLetterAnchorDown_ReturnsTrue(self) :

        # Arrange
        board = Board()
        a = Tile('a', 1, 0.07633656680151722, 7)
        b = Tile('b', 3, 0.019012035570253775, 59)
        c = Tile('c', 3, 0.04049934678472928, 29)
        e = Tile('e', 1, 0.11533383402651991, 2)      
        f = Tile('f', 4, 0.0126414510845898, 67)
        i = Tile('i', 1, 0.0885545324304026, 5)
        k = Tile('k', 5, 0.009120399881348338, 73)
        l = Tile('l', 1, 0.05340397735520395, 23)
        n = Tile('n', 1, 0.06738530865210449, 13)
        o = Tile('o', 1, 0.0653196336945477, 19)
        r = Tile('r', 1, 0.07098146383333229, 11)
        s = Tile('s', 1, 0.09480520300163461, 3)

        roller = Word([r, o, l, l, e, r])
        scarab = Word([s, c, a, r, a, b])
        flan = Word([f, l, a, n])
        link = Word([l, i, n, k])

        # Act
        board.PlaceWord(roller, board.GetAnchors()[0], 2, 'down')
        board.PlaceWord(scarab, board.GetAnchors()[0], 3, 'across')
        board.PlaceWord(flan, board.GetAnchors()[2], 1, 'across')
        results = board.IsWordLegal(link, board.GetAnchors()[15], 2, 'down')
        
        # Assert 
        # board.PrintBoard()
        self.assertTrue(results[0])

    def test_IsWordLegal_LegalWordAddSuffixOneLetterAnchorDown_ReturnsTrue(self) :

        # Arrange
        board = Board()
        a = Tile('a', 1, 0.07633656680151722, 7)
        c = Tile('c', 3, 0.04049934678472928, 29)
        e = Tile('e', 1, 0.11533383402651991, 2)      
        f = Tile('f', 4, 0.0126414510845898, 67)
        i = Tile('i', 1, 0.0885545324304026, 5)
        k = Tile('k', 5, 0.009120399881348338, 73)
        l = Tile('l', 1, 0.05340397735520395, 23)
        n = Tile('n', 1, 0.06738530865210449, 13)
        o = Tile('o', 1, 0.0653196336945477, 19)
        r = Tile('r', 1, 0.07098146383333229, 11)
        s = Tile('s', 1, 0.09480520300163461, 3)
        t = Tile('t', 1, 0.06566549066880407, 17)
        u = Tile('u', 1, 0.03288670659589642, 37)

        roller = Word([r, o, l, l, e, r])
        flan = Word([f, l, a, n])
        crust = Word([c, r, u, s, t])
        link = Word([l, i, n, k])

        # Act
        board.PlaceWord(roller, board.GetAnchors()[0], 2, 'down')
        board.PlaceWord(flan, board.GetAnchors()[3], 1, 'across')
        board.PlaceWord(crust, board.GetAnchors()[4], 1, 'across')
        results = board.IsWordLegal(link, board.GetAnchors()[8], 2, 'down')
        
        # Assert 
        # board.PrintBoard()
        self.assertTrue(results[0])

    def test_IsWordLegal_LegalWordAddPrefixAndSuffixOneLetterAnchorDown_ReturnsTrue(self) :

        # Arrange
        board = Board()
        a = Tile('a', 1, 0.07633656680151722, 7)
        b = Tile('b', 3, 0.019012035570253775, 59)
        c = Tile('c', 3, 0.04049934678472928, 29)
        e = Tile('e', 1, 0.11533383402651991, 2)      
        f = Tile('f', 4, 0.0126414510845898, 67)
        i = Tile('i', 1, 0.0885545324304026, 5)
        k = Tile('k', 5, 0.009120399881348338, 73)
        l = Tile('l', 1, 0.05340397735520395, 23)
        n = Tile('n', 1, 0.06738530865210449, 13)
        o = Tile('o', 1, 0.0653196336945477, 19)
        r = Tile('r', 1, 0.07098146383333229, 11)
        s = Tile('s', 1, 0.09480520300163461, 3)
        t = Tile('t', 1, 0.06566549066880407, 17)
        u = Tile('u', 1, 0.03288670659589642, 37)

        roller = Word([r, o, l, l, e, r])
        scarab = Word([s, c, a, r, a, b])
        flan = Word([f, l, a, n])
        crust = Word([c, r, u, s, t])
        link = Word([l, i, n, k])

        # Act
        board.PlaceWord(roller, board.GetAnchors()[0], 2, 'down')
        board.PlaceWord(scarab, board.GetAnchors()[0], 3, 'across')
        board.PlaceWord(flan, board.GetAnchors()[2], 1, 'across')
        board.PlaceWord(crust, board.GetAnchors()[3], 1, 'across')
        results = board.IsWordLegal(link, board.GetAnchors()[14], 2, 'down')
        
        # Assert 
        # board.PrintBoard()
        self.assertTrue(results[0])


    def test_IsWordLegal_IllegalWordBadPrefixOneLetterAnchorDown_ReturnsFalse(self) :

        # Arrange
        board = Board()
        a = Tile('a', 1, 0.07633656680151722, 7)
        b = Tile('b', 3, 0.019012035570253775, 59)
        c = Tile('c', 3, 0.04049934678472928, 29)
        e = Tile('e', 1, 0.11533383402651991, 2)      
        f = Tile('f', 4, 0.0126414510845898, 67)
        i = Tile('i', 1, 0.0885545324304026, 5)
        k = Tile('k', 5, 0.009120399881348338, 73)
        l = Tile('l', 1, 0.05340397735520395, 23)
        n = Tile('n', 1, 0.06738530865210449, 13)
        o = Tile('o', 1, 0.0653196336945477, 19)
        r = Tile('r', 1, 0.07098146383333229, 11)
        s = Tile('s', 1, 0.09480520300163461, 3)

        roller = Word([r, o, l, l, e, r])
        scarab = Word([s, c, a, r, a, b])
        flan = Word([f, l, a, n])
        sink = Word([s, i, n, k])

        # Act
        board.PlaceWord(roller, board.GetAnchors()[0], 2, 'down')
        board.PlaceWord(scarab, board.GetAnchors()[0], 3, 'across')
        board.PlaceWord(flan, board.GetAnchors()[2], 1, 'across')
        results = board.IsWordLegal(sink, board.GetAnchors()[15], 2, 'down')
        
        # Assert 
        self.assertFalse(results[0])
        self.assertEqual(results[1], 'word creates an invalid word when placed')

    def test_IsWordLegal_IllegalWordBadSuffixOneLetterAnchorDown_ReturnsFalse(self) :

        # Arrange
        board = Board()
        a = Tile('a', 1, 0.07633656680151722, 7)
        b = Tile('b', 3, 0.019012035570253775, 59)
        c = Tile('c', 3, 0.04049934678472928, 29)
        e = Tile('e', 1, 0.11533383402651991, 2)      
        f = Tile('f', 4, 0.0126414510845898, 67)
        i = Tile('i', 1, 0.0885545324304026, 5)
        k = Tile('k', 5, 0.009120399881348338, 73)
        l = Tile('l', 1, 0.05340397735520395, 23)
        m = Tile('m', 3, 0.02830915069392289, 43)
        n = Tile('n', 1, 0.06738530865210449, 13)
        o = Tile('o', 1, 0.0653196336945477, 19)
        r = Tile('r', 1, 0.07098146383333229, 11)
        u = Tile('u', 1, 0.03288670659589642, 37)

        roller = Word([r, o, l, l, e, r])
        flan = Word([f, l, a, n])
        crumb = Word([c, r, u, m, b])
        link = Word([l, i, n, k])

        # Act
        board.PlaceWord(roller, board.GetAnchors()[0], 2, 'down')
        board.PlaceWord(flan, board.GetAnchors()[3], 1, 'across')
        board.PlaceWord(crumb, board.GetAnchors()[4], 1, 'across')
        results = board.IsWordLegal(link, board.GetAnchors()[8], 2, 'down')
        
        # Assert 
        self.assertFalse(results[0])
        self.assertEqual(results[1], 'word creates an invalid word when placed')

    def test_IsWordLegal_IllegalWordBadPrefixAndSuffixOneLetterAnchorDown_ReturnsFalse(self) :

        # Arrange
        board = Board()
        a = Tile('a', 1, 0.07633656680151722, 7)
        b = Tile('b', 3, 0.019012035570253775, 59)
        c = Tile('c', 3, 0.04049934678472928, 29)
        e = Tile('e', 1, 0.11533383402651991, 2)      
        f = Tile('f', 4, 0.0126414510845898, 67)
        i = Tile('i', 1, 0.0885545324304026, 5)
        k = Tile('k', 5, 0.009120399881348338, 73)
        l = Tile('l', 1, 0.05340397735520395, 23)
        m = Tile('m', 3, 0.02830915069392289, 43)
        n = Tile('n', 1, 0.06738530865210449, 13)
        o = Tile('o', 1, 0.0653196336945477, 19)
        r = Tile('r', 1, 0.07098146383333229, 11)
        s = Tile('s', 1, 0.09480520300163461, 3)
        t = Tile('t', 1, 0.06566549066880407, 17)
        u = Tile('u', 1, 0.03288670659589642, 37)

        roller = Word([r, o, l, l, e, r])
        scarab = Word([s, c, a, r, a, b])
        flan = Word([f, l, a, n])
        crumb = Word([c, r, u, m, b])
        sink = Word([s, i, n, k])

        # Act
        board.PlaceWord(roller, board.GetAnchors()[0], 2, 'down')
        board.PlaceWord(scarab, board.GetAnchors()[0], 3, 'across')
        board.PlaceWord(flan, board.GetAnchors()[2], 1, 'across')
        board.PlaceWord(crumb, board.GetAnchors()[3], 1, 'across')
        results = board.IsWordLegal(sink, board.GetAnchors()[14], 2, 'down')
        
        # Assert 
        # board.PrintBoard()
        self.assertFalse(results[0])
        self.assertEqual(results[1], 'word creates an invalid word when placed')

    
    def test_IsWordLegal_LegalWordValidCollisionsOneLetterAnchorAcross_ReturnsTrue(self) :

        # Arrange
        board = Board()
        a = Tile('a', 1, 0.07633656680151722, 7)
        b = Tile('b', 3, 0.019012035570253775, 59)
        e = Tile('e', 1, 0.11533383402651991, 2)      
        f = Tile('f', 4, 0.0126414510845898, 67)
        i = Tile('i', 1, 0.0885545324304026, 5)
        g = Tile('g', 2, 0.02747732680328438, 47)
        k = Tile('k', 5, 0.009120399881348338, 73)
        l = Tile('l', 1, 0.05340397735520395, 23)
        n = Tile('n', 1, 0.06738530865210449, 13)
        o = Tile('o', 1, 0.0653196336945477, 19)
        r = Tile('r', 1, 0.07098146383333229, 11)
        s = Tile('s', 1, 0.09480520300163461, 3)
        t = Tile('t', 1, 0.06566549066880407, 17)

        linkers = Word([l, i, n, k, e, r, s])
        belies = Word([b, e, l, i, e, s])
        nose = Word([n, o, s, e])
        fastest = Word([f, a, s, t, e, s, t])
        ring = Word([r, i, n, g])
        
        # Act
        board.PlaceWord(linkers, board.GetAnchors()[0], 3, 'across')
        board.PlaceWord(belies, board.GetAnchors()[1], 3, 'down')
        board.PlaceWord(nose, board.GetAnchors()[3], 3, 'down')
        board.PlaceWord(ring, board.GetAnchors()[13], 2, 'across')
        results = board.IsWordLegal(fastest, board.GetAnchors()[4], 5, 'down')
        
        # Assert 
        self.assertTrue(results[0])

    def test_IsWordLegal_IllegalWordBadCollisionsOneLetterAnchorAcross_ReturnsFalse(self) :

        # Arrange
        board = Board()
        a = Tile('a', 1, 0.07633656680151722, 7)
        b = Tile('b', 3, 0.019012035570253775, 59)
        e = Tile('e', 1, 0.11533383402651991, 2)      
        f = Tile('f', 4, 0.0126414510845898, 67)
        i = Tile('i', 1, 0.0885545324304026, 5)
        g = Tile('g', 2, 0.02747732680328438, 47)
        k = Tile('k', 5, 0.009120399881348338, 73)
        l = Tile('l', 1, 0.05340397735520395, 23)
        n = Tile('n', 1, 0.06738530865210449, 13)
        o = Tile('o', 1, 0.0653196336945477, 19)
        r = Tile('r', 1, 0.07098146383333229, 11)
        s = Tile('s', 1, 0.09480520300163461, 3)
        t = Tile('t', 1, 0.06566549066880407, 17)

        linkers = Word([l, i, n, k, e, r, s])
        belies = Word([b, e, l, i, e, s])
        nose = Word([n, o, s, e])
        fattest = Word([f, a, t, t, e, s, t])
        sing = Word([s, i, n, g])
        
        # Act
        board.PlaceWord(linkers, board.GetAnchors()[0], 3, 'across')
        board.PlaceWord(belies, board.GetAnchors()[1], 3, 'down')
        board.PlaceWord(nose, board.GetAnchors()[3], 3, 'down')
        board.PlaceWord(sing, board.GetAnchors()[13], 2, 'across')
        results = board.IsWordLegal(fattest, board.GetAnchors()[4], 5, 'down')
        
        # Assert 
        self.assertFalse(results[0])
        self.assertEqual(results[1], 'word creates an invalid word when placed')
    
    def test_IsWordLegal_LegalWordValidCollisionsOneLetterAnchorDown_ReturnsTrue(self) :

        # Arrange
        board = Board()
        a = Tile('a', 1, 0.07633656680151722, 7)
        b = Tile('b', 3, 0.019012035570253775, 59)
        c = Tile('c', 3, 0.04049934678472928, 29)
        e = Tile('e', 1, 0.11533383402651991, 2)      
        f = Tile('f', 4, 0.0126414510845898, 67)
        i = Tile('i', 1, 0.0885545324304026, 5)
        k = Tile('k', 5, 0.009120399881348338, 73)
        l = Tile('l', 1, 0.05340397735520395, 23)
        n = Tile('n', 1, 0.06738530865210449, 13)
        o = Tile('o', 1, 0.0653196336945477, 19)
        r = Tile('r', 1, 0.07098146383333229, 11)
        s = Tile('s', 1, 0.09480520300163461, 3)
        t = Tile('t', 1, 0.06566549066880407, 17)
        u = Tile('u', 1, 0.03288670659589642, 37)

        roller = Word([r, o, l, l, e, r])
        scarab = Word([s, c, a, r, a, b])
        flan = Word([f, l, a, n])
        crust = Word([c, r, u, s, t])
        link = Word([l, i, n, k])

        # Act
        board.PlaceWord(roller, board.GetAnchors()[0], 2, 'down')
        board.PlaceWord(scarab, board.GetAnchors()[0], 3, 'across')
        board.PlaceWord(flan, board.GetAnchors()[2], 1, 'across')
        board.PlaceWord(link, board.GetAnchors()[15], 2, 'down')
        results = board.IsWordLegal(crust, board.GetAnchors()[3], 1, 'across')
        
        # Assert 
        self.assertTrue(results[0])

    def test_IsWordLegal_IllegalWordBadCollisionsOneLetterAnchorDown_ReturnsFalse(self) :

        # Arrange
        board = Board()
        a = Tile('a', 1, 0.07633656680151722, 7)
        b = Tile('b', 3, 0.019012035570253775, 59)
        c = Tile('c', 3, 0.04049934678472928, 29)
        e = Tile('e', 1, 0.11533383402651991, 2)      
        f = Tile('f', 4, 0.0126414510845898, 67)
        i = Tile('i', 1, 0.0885545324304026, 5)
        k = Tile('k', 5, 0.009120399881348338, 73)
        l = Tile('l', 1, 0.05340397735520395, 23)
        m = Tile('m', 3, 0.02830915069392289, 43)
        n = Tile('n', 1, 0.06738530865210449, 13)
        o = Tile('o', 1, 0.0653196336945477, 19)
        r = Tile('r', 1, 0.07098146383333229, 11)
        s = Tile('s', 1, 0.09480520300163461, 3)
        t = Tile('t', 1, 0.06566549066880407, 17)
        u = Tile('u', 1, 0.03288670659589642, 37)

        roller = Word([r, o, l, l, e, r])
        scarab = Word([s, c, a, r, a, b])
        flan = Word([f, l, a, n])
        crumb = Word([c, r, u, m, b])
        sink = Word([s, i, n, k])

        # Act
        board.PlaceWord(roller, board.GetAnchors()[0], 2, 'down')
        board.PlaceWord(scarab, board.GetAnchors()[0], 3, 'across')
        board.PlaceWord(flan, board.GetAnchors()[2], 1, 'across')
        board.PlaceWord(sink, board.GetAnchors()[14], 2, 'down')
        results = board.IsWordLegal(crumb, board.GetAnchors()[3], 1, 'across')
        
        # Assert 
        self.assertFalse(results[0])
        self.assertEqual(results[1], 'word creates an invalid word when placed')


    '''
    def visualTest_PlaceTile_PlaceRandomTiles(self) :

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



        # Assert
        testBoard.PrintBoard()
    '''


if __name__ == '__main__' :
    unittest.main()
