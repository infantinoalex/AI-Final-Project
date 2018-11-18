import os
import sys 
unitTestPath = os.path.dirname(__file__) + "/../Source"
sys.path.append(unitTestPath)

import unittest
from Anchor import Anchor
from Tile import Tile
from Word import Word 

class TestAnchorClass(unittest.TestCase) :

        def test_Constructor_CallWithDefaultParameters_AnchorSetCorrectly(self) :

            # Arrange
            expectedData = ''
            expectedSize = 0
            expectedXPos = 10
            expectedYPos = 10
            
            # Act
            testAnchor = Anchor()
            actualData = testAnchor.GetData().GetString()
            actualSize = testAnchor.GetSize()
            actualXPos = testAnchor.GetXPos()
            actualYPos = testAnchor.GetYPos()

            # Assert
            self.assertEqual(expectedData, actualData)
            self.assertEqual(expectedSize, actualSize)
            self.assertEqual(expectedXPos, actualXPos)
            self.assertEqual(expectedYPos, actualYPos)

        def test_Constructor_CallWithTiles_AnchorSetCorrectly(self) :

            # Arrange
            c = Tile('C', 3, 0.04049934678472928, 29)
            a = Tile('A', 1, 0.07633656680151722, 7)
            t = Tile('T', 1, 0.06566549066880407, 17)          
            expectedData = [c, a, t]
            expectedSize = len(expectedData)
            expectedXPos = 6
            expectedYPos = 2
            
            # Act
            testAnchor = Anchor(Word(expectedData), expectedXPos, expectedYPos)
            actualData = testAnchor.GetData().GetTiles()
            actualSize = testAnchor.GetSize()
            actualXPos = testAnchor.GetXPos()
            actualYPos = testAnchor.GetYPos()

            # Assert
            self.assertEqual(expectedData, actualData)
            self.assertEqual(expectedSize, actualSize)
            self.assertEqual(expectedXPos, actualXPos)
            self.assertEqual(expectedYPos, actualYPos)


if __name__ == '__main__' :
    unittest.main()
