"""

Contains the Anchor class
An Anchor is a place where a word can be played

"""

from Word import Word
from Words import Words

class Anchor :

    def __init__(self, word=Word(), x=10, y=10) :
        self.data = word
        self.size = len(word)
        self.xPos = x # position of first letter in anchor
        self.yPos = y # position of first letter in anchor
        self.possibleWords = Words().AnchorSearch(word)

    def GetData(self) :
        return self.data

    def GetPossibleWords(self) :
        return self.possibleWords.GetDict()

    def GetXPos(self) :
        return self.xPos

    def GetYPos(self) :
        return self.yPos
