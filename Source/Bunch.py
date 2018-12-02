"""

Contains the Bunch class
A Bunch represents the list of tiles that are not in the players hand
or have not been played yet

"""

from Tile import Tile
from ReadInFiles import ReadInTilesFromFile
from random import shuffle
from random import randint

class Bunch :

    def __init__(self, tiles = []) :
        if (not tiles) :
            self.bunch = ReadInTilesFromFile("..\\Data\\processed_letters.txt")
        else :
            self.bunch = tiles

        for x in range(10) :
            shuffle(self.bunch)

    def GetBunch(self) :
        return self.bunch

    def Peel(self) :
        randomInt = randint(1, 5)
        return self.DealFromBunch(randomInt)

    def ScoreBunch(self) :
        score = 0

        for tile in self.bunch :
            score += tile.GetScore()

        return score

    def IsBunchEmpty(self) :
        return not self.bunch

    def DealFromBunch(self, numberOfTiles) :
        if len(self.bunch) < numberOfTiles :
            numberOfTiles = len(self.bunch)

        dealtTiles = []

        for x in range(numberOfTiles) :
            dealtTiles.append(self.bunch.pop())

        return dealtTiles
        
