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
        self.assertEqual(board.GetBoard()[7, 10], t.GetLetter())
        self.assertEqual(board.GetBoard()[8, 10], e.GetLetter())
        self.assertEqual(board.GetBoard()[9, 10], s.GetLetter())
        self.assertEqual(board.GetBoard()[10, 10], t.GetLetter())
        self.assertEqual(board.GetBoard()[11, 10], i.GetLetter())
        self.assertEqual(board.GetBoard()[12, 10], n.GetLetter())
        self.assertEqual(board.GetBoard()[13, 10], g.GetLetter())

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
        self.assertEqual(board.GetBoard()[10, 7], t.GetLetter())
        self.assertEqual(board.GetBoard()[10, 8], e.GetLetter())
        self.assertEqual(board.GetBoard()[10, 9], s.GetLetter())
        self.assertEqual(board.GetBoard()[10, 10], t.GetLetter())
        self.assertEqual(board.GetBoard()[10, 11], i.GetLetter())
        self.assertEqual(board.GetBoard()[10, 12], n.GetLetter())
        self.assertEqual(board.GetBoard()[10, 13], g.GetLetter())

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
        self.assertEqual(board.GetBoard()[10, 10], t.GetLetter())
        self.assertEqual(board.GetBoard()[11, 10], e.GetLetter())
        self.assertEqual(board.GetBoard()[12, 10], s.GetLetter())
        self.assertEqual(board.GetBoard()[13, 10], t.GetLetter())
        self.assertEqual(board.GetBoard()[14, 10], i.GetLetter())
        self.assertEqual(board.GetBoard()[15, 10], n.GetLetter())
        self.assertEqual(board.GetBoard()[16, 10], g.GetLetter())

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
        self.assertEqual(board.GetBoard()[10, 10], t.GetLetter())
        self.assertEqual(board.GetBoard()[10, 11], e.GetLetter())
        self.assertEqual(board.GetBoard()[10, 12], s.GetLetter())
        self.assertEqual(board.GetBoard()[10, 13], t.GetLetter())
        self.assertEqual(board.GetBoard()[10, 14], i.GetLetter())
        self.assertEqual(board.GetBoard()[10, 15], n.GetLetter())
        self.assertEqual(board.GetBoard()[10, 16], g.GetLetter())

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
        # print(results[1])
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
        # print(results[1])
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
        # print(results[1])
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
        # print(results[1])
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
        board.PlaceWord(word1, board.GetAnchors()[0], 3, 'across')
        results = board.IsWordLegal(word2, board.GetAnchors()[3], 0, 'down')

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
        a = Tile('a', -1, -1.0, -1)
        c = Tile('c', -1, -1.0, -1)
        d = Tile('d', -1, -1.0, -1)
        e = Tile('e', -1, -1.0, -1)
        g = Tile('g', -1, -1.0, -1)
        i = Tile('i', -1, -1.0, -1)
        k = Tile('k', -1, -1.0, -1)
        n = Tile('n', -1, -1.0, -1)
        r = Tile('r', -1, -1.0, -1)
        v = Tile('v', -1, -1.0, -1)
        w = Tile('w', -1, -1.0, -1)
        y = Tile('y', -1, -1.0, -1)
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

    '''
    def test_IsWordLegal_LegalWordWithOverlapOneLetterAnchorDown_ReturnsTrue(self) :

        # Arrange
        board = Board()
        a = Tile('a', -1, -1.0, -1)
        c = Tile('c', -1, -1.0, -1)
        d = Tile('d', -1, -1.0, -1)
        e = Tile('e', -1, -1.0, -1)
        g = Tile('g', -1, -1.0, -1)
        i = Tile('i', -1, -1.0, -1)
        k = Tile('k', -1, -1.0, -1)
        n = Tile('n', -1, -1.0, -1)
        r = Tile('r', -1, -1.0, -1)
        v = Tile('v', -1, -1.0, -1)
        w = Tile('w', -1, -1.0, -1)
        y = Tile('y', -1, -1.0, -1)
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
        # board.PrintBoard()
        self.assertTrue(results[0])
    '''

    def test_IsWordLegal_IllegalWordWithOverlapOneLetterAnchorAcross_ReturnsFalseWordFit(self) :

        # Arrange
        board = Board()
        a = Tile('a', -1, -1.0, -1)
        d = Tile('d', -1, -1.0, -1)
        e = Tile('e', -1, -1.0, -1)
        g = Tile('g', -1, -1.0, -1)
        i = Tile('i', -1, -1.0, -1)
        k = Tile('k', -1, -1.0, -1)
        n = Tile('n', -1, -1.0, -1)
        r = Tile('r', -1, -1.0, -1)
        v = Tile('v', -1, -1.0, -1)
        w = Tile('w', -1, -1.0, -1)
        y = Tile('y', -1, -1.0, -1)
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
        a = Tile('a', -1, -1.0, -1)
        d = Tile('d', -1, -1.0, -1)
        e = Tile('e', -1, -1.0, -1)
        g = Tile('g', -1, -1.0, -1)
        i = Tile('i', -1, -1.0, -1)
        k = Tile('k', -1, -1.0, -1)
        n = Tile('n', -1, -1.0, -1)
        r = Tile('r', -1, -1.0, -1)
        v = Tile('v', -1, -1.0, -1)
        w = Tile('w', -1, -1.0, -1)
        y = Tile('y', -1, -1.0, -1)
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
