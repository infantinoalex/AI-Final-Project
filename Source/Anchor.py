"""

Contains the Anchor class
An Anchor is a place where a word can be played

"""

from Words import Words

class Anchor :

    def __init__(self, data=' ', words = Words(), x=10, y=10) :
        self.data = data
        self.possibleWords = words
        self.xPos = x
        self.yPos = y

    def GetData(self) :
        return self.data

    def GetPossibleWords(self) :
        return self.possibleWords.GetDict()

    def GetXPos(self) :
        return self.xPos

    def GetYPos(self) :
        return self.yPos
