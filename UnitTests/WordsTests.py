import os
import sys 
unitTestPath = os.path.dirname(__file__) + "/../Source"
sys.path.append(unitTestPath)

import unittest
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



if __name__ == '__main__' :
    unittest.main()