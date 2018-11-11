"""

Contains function to read in Tiles from a text file

"""

from Tile import Tile
import re
import os

def ReadInTilesFromFile(fileName) :
    tiles = []
    pythonDir = os.path.dirname(__file__)
    absFilePath = os.path.join(pythonDir, fileName)
    with open(absFilePath, "r") as filePointer :
        line = filePointer.readline()

        regexString = "(\w),(\d),(\d),(\d)"
        regex = re.compile(regexString)
        while line :
            if regex.match(line) :
                result = regex.findall(line)
                letter = str(result[0][0])
                value = int(result[0][1])
                frequency = int(result[0][2])
                primeNumber = int(result[0][3])
                tile = Tile(letter, value, frequency, primeNumber)
                tiles.append(tile)
                line = filePointer.readline()

            else :
                raise IOError("Could not find any match with line {}. Check to make sure it is in correct format".format(line))


    if not tiles :
        raise IOError("Could not properly read file {}".format(fileName))

    return tiles