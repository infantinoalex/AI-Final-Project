"""

Contains the Word class.
A Word represents a playable letter and is associated score in the game

"""

class Word :
    
    def __init__(self, tiles):
        self.tiles = tiles
        self.string = ""
        self.score = 0
        self.primeNumber = 1

        for tile in tiles :
            self.string+= tile.GetLetter()
            self.score+= tile.GetScore()
            self.primeNumber*= tile.GetPrime()

    def GetTiles(self) :
        return self.tiles

    def GetString(self) :
        return self.string
    
    def GetScore(self) :
        return self.score

    def GetPrime(self) :
        return self.primeNumber