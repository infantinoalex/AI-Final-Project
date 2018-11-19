import os
import sys 
unitTestPath = os.path.dirname(__file__) + "/../Source"
sys.path.append(unitTestPath)

import unittest
from Tile import Tile
from Word import Word
from Words import Words

class TestWordsClass(unittest.TestCase) :

    def test_Constructor_DefaultConstructor_ContainsFullDictionary(self) :

        # Arrange 
        expectedWordCount = 178603
        
        # Act
        words = Words()
        actualWordCount = 0
        for key in words.GetDict() :
            actualWordCount+= len(words.GetDict().get(key))

        # Assert
        self.assertEqual(expectedWordCount, actualWordCount)
      
    def test_Constructor_PassedDictionary_ContainsPassedDictionary(self) :
        
        # Arrange 
        expected = {1111:'THIS', 2222:'IS', 3333:'A', 4444:'TEST'}
        
        # Act
        words = Words(expected)
        actual = words.GetDict()

        # Assert
        self.assertEqual(expected, actual)

    def test_TileSearch_FindingWordsWithQ_ReturnsCorrectWords(self) :

        # Arrange
        words = Words()
        qKeys = []
        q = Tile('Q', 10, 0.0016308292362745903, 101)
        allQs = True
        noQs = True

        # Act
        qWords = words.TileSearch(q)
        for key in qWords.GetDict() :
            qKeys.append(key)
            for element in qWords.GetDict().get(key) :
                if q.GetLetter() not in element :
                    allQs = False
                    print(qWords.GetDict().get(key), "has no Qs!")
        for key in words.GetDict() :
            if key not in qKeys : 
                for element in words.GetDict().get(key) :
                    if q.GetLetter() in element :
                        noQs = False
                        print(words.GetDict().get(key), "has Qs!")

        # Assert
        self.assertTrue(allQs)
        self.assertTrue(noQs)

    def test_WordSearch_FindingWordsWithScript_ReturnsCorrectWords(self) :

        # Arrange
        words = Words()
        selectedKeys = []
        s = Tile('S', 1, 0.09480520300163461, 3)
        c = Tile('C', 3, 0.04049934678472928, 29)
        r = Tile('R', 1, 0.07098146383333229, 11)
        i = Tile('I', 1, 0.0885545324304026, 5)
        p = Tile('P', 3, 0.029410465329100584, 41)
        t = Tile('T', 1, 0.06566549066880407, 17)
        word = Word([s, c, r, i, p, t])
        allWordsContainLetters = True
        noWordsContainLetters = True

        # Act
        selectedWords = words.WordSearch(word)
        for key in selectedWords.GetDict() :
            selectedKeys.append(key)
            for element in selectedWords.GetDict().get(key) :
                validLetters = [tile.GetLetter() for tile in word.GetTiles()]
                actualLetters = [letter for i, letter in enumerate(element)]
                for letter in actualLetters :
                    if letter in validLetters : validLetters.remove(letter)
                    else : allWordsContainLetters = False
        for key in words.GetDict() :
            if key not in selectedKeys : 
                for element in words.GetDict().get(key) :
                    validLetters = [tile.GetLetter() for tile in word.GetTiles()]
                    actualLetters = [letter for i, letter in enumerate(element)]
                    for i, letter in enumerate(element) :
                        if letter in validLetters : 
                            validLetters.remove(letter)
                            actualLetters.remove(letter)
                    if not validLetters and not actualLetters: 
                        noWordsContainLetters = False                    

        # Assert
        self.assertTrue(allWordsContainLetters)
        self.assertTrue(noWordsContainLetters)

    def test_FixedWordSearch_FindingWordsWithScript_ReturnsCorrectWords(self) :

        # Arrange
        words = Words()
        selectedKeys = []
        s = Tile('S', 1, 0.09480520300163461, 3)
        c = Tile('C', 3, 0.04049934678472928, 29)
        r = Tile('R', 1, 0.07098146383333229, 11)
        i = Tile('I', 1, 0.0885545324304026, 5)
        p = Tile('P', 3, 0.029410465329100584, 41)
        t = Tile('T', 1, 0.06566549066880407, 17)
        word = Word([s, c, r, i, p, t])
        allWordsContainWord = True
        noWordsContainWord = True

        # Act
        selectedWords = words.FixedWordSearch(word)
        for key in selectedWords.GetDict() :
            selectedKeys.append(key)
            for element in selectedWords.GetDict().get(key) :
                if word.GetString() not in element :
                    allWordsContainWord = False
        for key in words.GetDict() :
            if key not in selectedKeys : 
                for element in words.GetDict().get(key) :
                    if word.GetString() in element :
                        noWordsContainWord = False
                        print(element, "contains the word", word.GetString())

        # Assert
        self.assertTrue(allWordsContainWord)
        self.assertTrue(noWordsContainWord)
 
    def test_AnchorSearch_FindingWordsWithQ_ReturnsCorrectWords(self) :

        # Arrange
        words = Words()
        qKeys = []
        q = Tile('Q', 10, 0.0016308292362745903, 101)
        word = Word([q])
        allQs = True
        noQs = True

        # Act
        qWords = words.AnchorSearch(word)
        for key in qWords.GetDict() :
            qKeys.append(key)
            for element in qWords.GetDict().get(key) :
                if q.GetLetter() not in element :
                    allQs = False
                    print(qWords.GetDict().get(key), "has no Qs!")
        for key in words.GetDict() :
            if key not in qKeys : 
                for element in words.GetDict().get(key) :
                    if q.GetLetter() in element :
                        noQs = False
                        print(words.GetDict().get(key), "has Qs!")

        # Assert
        self.assertTrue(allQs)
        self.assertTrue(noQs)
    
    def test_AnchorSearch_FindingWordsWithScript_ReturnsCorrectWords(self) :

        # Arrange
        words = Words()
        selectedKeys = []
        s = Tile('S', 1, 0.09480520300163461, 3)
        c = Tile('C', 3, 0.04049934678472928, 29)
        r = Tile('R', 1, 0.07098146383333229, 11)
        i = Tile('I', 1, 0.0885545324304026, 5)
        p = Tile('P', 3, 0.029410465329100584, 41)
        t = Tile('T', 1, 0.06566549066880407, 17)
        word = Word([s, c, r, i, p, t])
        allWordsContainWord = True
        noWordsContainWord = True

        # Act
        selectedWords = words.AnchorSearch(word)
        for key in selectedWords.GetDict() :
            selectedKeys.append(key)
            for element in selectedWords.GetDict().get(key) :
                if word.GetString() not in element :
                    allWordsContainWord = False
        for key in words.GetDict() :
            if key not in selectedKeys : 
                for element in words.GetDict().get(key) :
                    if word.GetString() in element :
                        noWordsContainWord = False
                        print(element, "contains the word", word.GetString())

        # Assert
        self.assertTrue(allWordsContainWord)
        self.assertTrue(noWordsContainWord)

    def test_ExactWordSearch_WordExists_ReturnsTrue(self) :

        # Arrange
        words = Words()
        c = Tile('C', 3, 0.04049934678472928, 29)
        a = Tile('A', 1, 0.07633656680151722, 7) 
        t = Tile('T', 1, 0.06566549066880407, 17)
        word = Word([c, a, t])

        # Act
        results = words.ExactWordSearch(word)

        # Assert
        self.assertTrue(results)

    def test_ExactWordSearch_WordDoesNotExist_ReturnsFalse(self) :

        # Arrange
        words = Words()
        c = Tile('C', 3, 0.04049934678472928, 29)
        q = Tile('Q', 10, 0.0016308292362745903, 101)
        t = Tile('T', 1, 0.06566549066880407, 17)
        word = Word([c, q, t])

        # Act
        results = words.ExactWordSearch(word)

        # Assert
        self.assertFalse(results)
    

if __name__ == '__main__' :
    unittest.main()