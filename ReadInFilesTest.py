import unittest
import ReadInFiles
from Tile import Tile

class TestTilesClass(unittest.TestCase) :

    def test_ReadInTilesFromFile_FileNotFound_IOErrorRaised(self) :
        # Arrange
        fileName = "Does Not Exist"

        # Act & Asssert
        self.assertRaises(IOError, ReadInFiles.ReadInTilesFromFile, fileName)

    def test_ReadInTilesFromFile_InvalidFileFormat_IOErrorRaised(self) :
        # Arrange
        fileName = "ReadInFilesTestFiles\WrongFileFormat.txt"

        # Act & Asssert
        self.assertRaises(IOError, ReadInFiles.ReadInTilesFromFile, fileName)

    def test_ReadInTilesFromFile_ValidFileFormat_ExpectedTilesReturned(self) :
        # Arrange
        tiles = []

        letterA = 'A'
        valueA = 1
        frequencyA = 1
        primeNumberA = 1
        tileA = Tile(letterA, valueA, frequencyA, primeNumberA)
        tiles.append(tileA)

        letterB = 'B'
        valueB = 3
        frequencyB = 3
        primeNumberB = 3
        tileB = Tile(letterB, valueB, frequencyB, primeNumberB)
        tiles.append(tileB)
        tiles.append(tileB)
        tiles.append(tileB)

        fileName = "ReadInFilesTestFiles\TestFile.txt"

        # Act
        result = ReadInFiles.ReadInTilesFromFile(fileName)

        # Assert
        lengthResult = len(result)
        lengthExpected = len(tiles)
        self.assertEqual(lengthResult, lengthExpected)

        for count in range(lengthResult) :
            resultTile = result[count]
            expectedTile = tiles[count]
            self.assertEqual(resultTile.GetLetter(), expectedTile.GetLetter())
            self.assertEqual(resultTile.GetScore(), expectedTile.GetScore())
            self.assertEqual(resultTile.GetFrequency(), expectedTile.GetFrequency())
            self.assertEqual(resultTile.GetPrime(), expectedTile.GetPrime())


if __name__ == '__main__' :
    unittest.main()