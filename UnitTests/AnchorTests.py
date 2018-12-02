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
            expectedLetter = ' '
            expectedXPos = 10
            expectedYPos = 10
            
            # Act
            testAnchor = Anchor()
            actualLetter = testAnchor.GetLetter()
            actualXPos = testAnchor.GetXPos()
            actualYPos = testAnchor.GetYPos()

            # Assert
            self.assertEqual(expectedLetter, actualLetter)
            self.assertEqual(expectedXPos, actualXPos)
            self.assertEqual(expectedYPos, actualYPos)

        def test_Constructor_CallWithTiles_AnchorSetCorrectly(self) :

            # Arrange
            c = Tile('C', 3, 0.04049934678472928, 29)
            expectedLetter = c.GetLetter()
            expectedXPos = 6
            expectedYPos = 2
            
            # Act
            testAnchor = Anchor(c, expectedXPos, expectedYPos)
            actualLetter = testAnchor.GetLetter()
            actualXPos = testAnchor.GetXPos()
            actualYPos = testAnchor.GetYPos()

            # Assert
            self.assertEqual(expectedLetter, actualLetter)
            self.assertEqual(expectedXPos, actualXPos)
            self.assertEqual(expectedYPos, actualYPos)


if __name__ == '__main__' :
    unittest.main()
