"""

Contains the Anchor class
An Anchor is a place where a word can be played

"""

from Tile import Tile
from Words import Words

class Anchor :

    def __init__(self, tile=Tile(), x=10, y=10, dir="down") :
        self.data = tile
        self.xPos = x # position of the tile on the board
        self.yPos = y # position of the tile on the board
        self.dir = dir
        self.possibleWords = Words()
        if self.data.GetLetter() is not ' ' : 
            self.possibleWords = self.possibleWords.TileSearch(self.data)

    def GetTile(self) :
        return self.data

    def GetLetter(self) :
        return self.data.GetLetter()

    def GetPossibleWords(self) :
        return self.possibleWords

    def GetXPos(self) :
        return self.xPos

    def GetYPos(self) :
        return self.yPos

    def GetDirection(self):
        return self.dir
