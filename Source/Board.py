"""

Contains the Board class
The Board is the place where all the tiles are played; it starts off empty, and 
then holds every word which gets played throughout the game

"""

import numpy as np
from Tile import Tile
from Anchor import Anchor
from Word import Word
from Words import Words

class Board :

    def __init__(self) :
        self.size = 21
        self.board = np.empty([self.size, self.size], dtype=Tile)
        self.anchors = [Anchor()]

        for i in range(self.size) :
            for j in range(self.size) :
                self.board[i, j] = Tile()

    def GetBoard(self) :
        return self.board

    def GetAnchors(self) :
        return self.anchors

    def PlaceTile(self, tile, xPos, yPos) :
        self.board[xPos, yPos] = tile
        self.anchors.append(Anchor(tile, xPos, yPos))

    def PlaceWord(self, word, anchor, anchorIndex, playDirection) :
        relativeXPos = anchor.GetXPos()
        relativeYPos = anchor.GetYPos()
        if playDirection == 'across' :
            relativeXPos-= anchorIndex
            for tile in word.GetTiles() :
                self.PlaceTile(tile, relativeXPos, relativeYPos)
                self.anchors.append(Anchor(tile, relativeXPos, relativeYPos, 'down'))
                relativeXPos+= 1
        if playDirection == 'down' :
            relativeYPos-= anchorIndex
            for tile in word.GetTiles() :
                self.PlaceTile(tile, relativeXPos, relativeYPos)
                self.anchors.append(Anchor(tile, relativeXPos, relativeYPos, 'across'))
                relativeYPos+= 1
        self.anchors.remove(anchor)

    def IsWordLegal(self, word, anchor, anchorIndex, playDirection) :

        # word must have at least 2 letters
        if not self.BigEnough(word) : 
            return [False, 'word not big enough']

        # word must not go off the board
        elif self.OffBoard(word, anchor, anchorIndex, playDirection) : 
            return [False, 'word goes off the board']

        # at this point, if the anchor is the default anchor, 
        # we can stop checking and confirm that the word is legal
        elif anchor.GetLetter() is ' ' :
            return [True, 'word with default anchor is legal :)']

        # otherwise we have more checks to make
        else :

            # anchor must mach the letter at the anchor index
            if not self.AnchorIndexCorrect(word, anchor, anchorIndex) :
                return [False, 'anchorIndex is invalid']

            # the word must fit on the board correctly, aka spaces where word will go
            # must either be blank or equal to the letter that will be placed there
            elif not self.WordFits(word, anchor, anchorIndex, playDirection) :
                return [False, 'word does not fit in the board correctly']
        
            # the word must not create any illegal words, aka the spaces surrounding the
            # word must be clear or if there are any collisions they must form words
            elif self.WordCreatesInvalidWord(word, anchor, anchorIndex, playDirection) :
                return [False, 'word creates an invalid word when placed']

            else : return [True, 'word is legal :)']

    def PrintBoard(self) :
        for i in range(21) :
            if (i == 0) :
                print(end=" ")
                for j in range(21) :
                    print('+---', end="")
                print('+')
            for j in range(21) :
                print(' |', self.board[j][i].GetLetter(), end="")
            print(' |')
            print(end=" ")
            for j in range(21) :
                print('+---', end="")
            print('+')


    def BigEnough(self, word) :
        if not word.GetTiles() : 
            return False
        elif len(word.GetTiles()) < 2 : 
            return False 
        else : 
            return True

    def OutOfBounds(self, bound) :
        if bound < 0 or bound > self.size : 
            return True
        else : 
            return False

    def OffBoard(self, word, anchor, anchorIndex, playDirection) : 
        relativeXPos = anchor.GetXPos()
        relativeYPos = anchor.GetYPos()
        if playDirection == 'across' :
            upperBound = relativeXPos - anchorIndex
            lowerBound = relativeXPos + (len(word.GetTiles()) - anchorIndex - 1)
        if playDirection == 'down' :
            upperBound = relativeYPos - anchorIndex
            lowerBound = relativeYPos + (len(word.GetTiles()) - anchorIndex - 1)
        if self.OutOfBounds(upperBound) or self.OutOfBounds(lowerBound) :
            return True
        else : 
            return False
    
    def AnchorIndexCorrect(self, word, anchor, anchorIndex) :
        expectedAnchorLetter = anchor.GetLetter()
        actualAnchorLetter = word.GetTiles()[anchorIndex].GetLetter()
        if expectedAnchorLetter is actualAnchorLetter :
            return True
        else :
            print(expectedAnchorLetter, "!=", actualAnchorLetter)
            return False

    def TileFits(self, tile, xPos, yPos) :
        if self.board[xPos, yPos].GetLetter() == ' ' :
            return True
        elif self.board[xPos, yPos].GetLetter() == tile.GetLetter() :
            return True
        else :
            return False 

    def WordFits(self, word, anchor, anchorIndex, playDirection) :
        relativeXPos = anchor.GetXPos()
        relativeYPos = anchor.GetYPos()
        if playDirection == 'across' :
            upperBound = relativeXPos - anchorIndex
            lowerBound = relativeXPos + (len(word.GetTiles()) - anchorIndex - 1)
            for i in range(upperBound, lowerBound + 1) :
                if not self.TileFits(word.GetTiles()[i - upperBound], i, relativeYPos) :
                    return False
        if playDirection == 'down' :
            upperBound = relativeYPos - anchorIndex
            lowerBound = relativeYPos + (len(word.GetTiles()) - anchorIndex - 1)
            for i in range(upperBound, lowerBound + 1) :
                if not self.TileFits(word.GetTiles()[i - upperBound], relativeXPos, i) :
                    return False
        return True

    def PrefixAndSuffixClear(self, word, anchor, anchorIndex, playDirection) :

        # look at the word you played in addition to any direct prefex and suffix tiles
        # if this new word is valid, return true, otherwise return false 

        relativeXPos = anchor.GetXPos()
        relativeYPos = anchor.GetYPos()
        if playDirection == 'across' :
            upperBound = relativeXPos - anchorIndex
            prefixUpperBound = upperBound - 1
            upperOutOfBounds = self.OutOfBounds(prefixUpperBound)
            upperEqualsSpace = self.board[prefixUpperBound, relativeYPos].GetLetter() == ' '
            lowerBound = relativeXPos + (len(word.GetTiles()) - anchorIndex - 1)
            suffixLowerBound = lowerBound + 1
            lowerOutOfBounds = self.OutOfBounds(suffixLowerBound)
            lowerEqualsSpace = self.board[suffixLowerBound, relativeYPos].GetLetter() == ' '
            if not upperOutOfBounds and upperEqualsSpace and not lowerOutOfBounds and lowerEqualsSpace :
                return True
            while not upperOutOfBounds and not upperEqualsSpace :
                prefixUpperBound-= 1
                upperOutOfBounds = self.OutOfBounds(prefixUpperBound)
                upperEqualsSpace = self.board[prefixUpperBound, relativeYPos].GetLetter() == ' '
            while not lowerOutOfBounds and not lowerEqualsSpace :
                suffixLowerBound+= 1
                lowerOutOfBounds = self.OutOfBounds(suffixLowerBound)
                lowerEqualsSpace = self.board[suffixLowerBound, relativeYPos].GetLetter() == ' '
            fullWord = []
            for i in range(prefixUpperBound + 1, upperBound) :
                fullWord.append(self.board[i, relativeYPos])
            fullWord+= word.GetTiles()
            for i in range(lowerBound + 1, suffixLowerBound) :
                fullWord.append(self.board[i, relativeYPos])
            return Words().ExactWordSearch(Word(fullWord))
        if playDirection == 'down' :
            upperBound = relativeYPos - anchorIndex
            prefixUpperBound = upperBound - 1
            upperOutOfBounds = self.OutOfBounds(prefixUpperBound)
            upperEqualsSpace = self.board[relativeXPos, prefixUpperBound].GetLetter() == ' '
            lowerBound = relativeYPos + (len(word.GetTiles()) - anchorIndex - 1)
            suffixLowerBound = lowerBound + 1
            lowerOutOfBounds = self.OutOfBounds(suffixLowerBound)
            lowerEqualsSpace = self.board[relativeXPos, suffixLowerBound].GetLetter() == ' '
            if not upperOutOfBounds and upperEqualsSpace and not lowerOutOfBounds and lowerEqualsSpace :
                return True
            while not upperOutOfBounds and not upperEqualsSpace :
                prefixUpperBound-= 1
                upperOutOfBounds = self.OutOfBounds(prefixUpperBound)
                upperEqualsSpace = self.board[relativeXPos, prefixUpperBound].GetLetter() == ' '
            while not lowerOutOfBounds and not lowerEqualsSpace :
                suffixLowerBound+= 1
                lowerOutOfBounds = self.OutOfBounds(suffixLowerBound)
                lowerEqualsSpace = self.board[relativeXPos, suffixLowerBound].GetLetter() == ' '
            fullWord = []
            for i in range(prefixUpperBound + 1, upperBound) :
                fullWord.append(self.board[relativeXPos, i])
            fullWord+= word.GetTiles()
            for i in range(lowerBound + 1, suffixLowerBound) :
                fullWord.append(self.board[relativeXPos, i])
            return Words().ExactWordSearch(Word(fullWord))

    def WordCreatesInvalidWord(self, word, anchor, anchorIndex, playDirection) :
        invalidWord = False
        if not self.PrefixAndSuffixClear(word, anchor, anchorIndex, playDirection) : 
            invalidWord = True
        for i in range(len(word.GetTiles())) :
            tile = word.GetTiles()[i]
            temp = Word([tile])
            if i is not anchorIndex and playDirection is 'across':
                x = anchor.GetXPos() - anchorIndex + i
                y = anchor.GetYPos()
                if not self.PrefixAndSuffixClear(temp, Anchor(tile, x, y), 0, 'down') : 
                    invalidWord = True
            if i is not anchorIndex and playDirection is 'down':
                x = anchor.GetXPos()
                y = anchor.GetYPos() - anchorIndex + i
                if not self.PrefixAndSuffixClear(temp, Anchor(tile, x, y), 0, 'across') : 
                    invalidWord = True
        return invalidWord

