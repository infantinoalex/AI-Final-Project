"""

Contains the Board class
The Board is the place where all the tiles are played; it starts off empty, and 
then holds every word which gets played throughout the game

"""

import numpy as np
from Tile import Tile
from Anchor import Anchor
from Word import Word

class Board :

    def __init__(self) :
        self.size = 21
        self.board = np.empty([self.size, self.size], dtype=str)
        self.anchors = [Anchor()]

        for i in range(self.size) :
            for j in range(self.size) :
                self.board[i, j] = ' '

    def GetAnchors(self) :
        return self.anchors

    def PlaceTile(self, tile, xPos, yPos) :
        self.board[xPos, yPos] = tile.GetLetter()

    def PlaceWord(self, word, anchor, anchorIndex, playDirection) :
        relXPos = anchor.GetXPos()
        relYPos = anchor.GetYPos()
        if playDirection == 'across' :
            relXPos-= anchorIndex
            for tile in word.GetTiles() :
                self.PlaceTile(tile, relXPos, relYPos)
                relXPos+= 1
                np.append(self.anchors, Anchor([tile], relXPos, relYPos))
        if playDirection == 'down' :
            relYPos-= anchorIndex
            for tile in word.GetTiles() :
                self.PlaceTile(tile, relXPos, relYPos)
                relYPos+= 1
                np.append(self.anchors, Anchor([tile], relXPos, relYPos))
        np.append(self.anchors, Anchor(word.GetTiles(), relXPos, relYPos))
        np.delete(self.anchors, anchor, 0)

    def IsWordLegal(self, word, anchor, anchorIndex, playDirection) :

        # word must have at least 2 letters
        if not self.BigEnough(word) : 
            return False 

        # word must not go off the board
        elif self.OffBoard(word, anchor, anchorIndex, playDirection) : 
            return False

        # at this point, if the anchor is the default anchor, 
        # we can stop checking and confirm that the word is legal
        elif anchor.GetSize() is 0 :
            return True

        # otherwise we have more checks to make
        else :

            # cover the case where an anchor is only one tile            
            if anchor.GetSize() is 1 :

                # anchor must mach the letter at the anchor index
                if self.AnchorIndexIncorrect(word, anchor, anchorIndex) :
                    return False

                # the word must fit on the board correctly, aka spaces where word will go
                # must either be blank or equal to the letter that will be placed there
                if not self.WordFits(word, anchor, anchorIndex) :
                    return False
            
                # the word must not create any illegal words, aka the spaces surrounding the
                # word must be clear or if there are any collisions they must form words
                if self.WordCreatesInvalidWord(self, word, anchor, anchorIndex) :
                    return False

            # cover the case where an anchor is many tiles
            else :
                print("haven't gotten here yet lol")



    def PrintBoard(self) :
        for i in range(21) :
            if (i == 0) :
                print(end=" ")
                for j in range(21) :
                    print('+---', end="")
                print('+')
            for j in range(21) :
                print(' |', self.board[j][i], end="")
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
        if playDirection = 'across' :
            upperBound = relativeXPos - anchorIndex
            lowerBound = relativeXPos + (len(word.GetTiles()) - anchorIndex - 1)
        if playDirection = 'down' :
            upperBound = relativeYPos - anchorIndex
            lowerBound = relativeYPos + (len(word.GetTiles()) - anchorIndex - 1)
        if OutOfBounds(upperBound) or OutOfBounds(lowerBound) :
            return False
        else : 
            return True
    
    def AnchorIndexIncorrect(self, word, anchor, anchorIndex) :
        expectedAnchorIndex = anchor.GetTiles()[0].GetLetter()
        actualAnchorIndex = word.GetTiles()[anchorIndex].GetLetter()
        if expectedAnchorIndex is actualAnchorIndex :
            return True
        else :
            return False

    def TileFits(self, tile, xPos, yPos) :
        if self.board[xPos, yPos] == ' ' :
            return True
        elif self.board[xPos, yPos] == tile.GetLetter() :
            return True
        else :
            return False 

    def WordFits(self, word, anchor, anchorIndex) :
        relativeXPos = anchor.GetXPos()
        relativeYPos = anchor.GetYPos()
        if playDirection = 'across' :
            upperBound = relativeXPos - anchorIndex
            lowerBound = relativeXPos + (len(word.GetTiles()) - anchorIndex - 1)
            for i in range(upperBound, lowerBound + 1) :
                if not self.TileFits(word.GetTiles()[i - upperBound], i, relativeYPos) :
                    return False
        if playDirection = 'down' :
            upperBound = relativeYPos - anchorIndex
            lowerBound = relativeYPos + (len(word.GetTiles()) - anchorIndex - 1)
            for i in range(upperBound, lowerBound + 1) :
                if not self.ValidSpace(word.GetTiles()[i - upperBound], relativeXPos, i) :
                    return False
        return True

    def PrefixAndSuffixClear(self, word, anchor, anchorIndex) :

        # look at the word you played in addition to any direct prefex and suffix tiles
        # if this new word is valid, return true, otherwise return false 

        relativeXPos = anchor.GetXPos()
        relativeYPos = anchor.GetYPos()
        if playDirection = 'across' :
            upperBound = relativeXPos - anchorIndex
            lowerBound = relativeXPos + (len(word.GetTiles()) - anchorIndex - 1)
            while not self.OutOfBounds(upperBound - 1) and self.board[upperBound - 1, relativeYPos] == ' ' :
                upperBound-= 1
            while not self.OutOfBounds(lowerBound + 1) and self.board[lowerBound + 1, relativeYPos] == ' ' :
                lowerBound+= 1
            fullWord = ''
            for i in range(upperBound, lowerBound + 1) :
                fullWord+= self.board[i, relativeYPos]
            return Words().ExactWordSearch(fullWord)
        if playDirection = 'down' :
            upperBound = relativeYPos - anchorIndex
            lowerBound = relativeYPos + (len(word.GetTiles()) - anchorIndex - 1)
            while not self.OutOfBounds(upperBound - 1) and self.board[relativeXPos, upperBound - 1] == ' ' :
                upperBound-= 1
            while not self.OutOfBounds(lowerBound + 1) and self.board[relativeXPos, upperBound - 1] == ' ' :
                lowerBound+= 1
            fullWord = ''
            for i in range(upperBound, lowerBound + 1) :
                fullWord+= self.board[i, relativeYPos]
            return Words().ExactWordSearch(fullWord)

    def WordCreatesInvalidWord(self, word, anchor, anchorIndex) :
        relativeXPos = anchor.GetXPos()
        relativeYPos = anchor.GetYPos()
        invalidWord = False
        if playDirection = 'across' :
            upperBound = relativeXPos - anchorIndex
            lowerBound = relativeXPos + (len(word.GetTiles()) - anchorIndex - 1)
            if not self.PrefixAndSuffixClear(word, anchor, anchorIndex) : 
                invalidWord = True
            for i in range(len(word.GetTiles())) :
                tile = word.GetTiles()[i]
                if i is not anchorIndex :
                    if not self.PrefixAndSuffixClear(Word([tile]), anchor, anchorIndex) : 
                        invalidWord = True
        if playDirection = 'down' :
            upperBound = relativeYPos - anchorIndex
            lowerBound = relativeYPos + (len(word.GetTiles()) - anchorIndex - 1)
            if not self.PrefixAndSuffixClear() : invalidWord = True
            for i in range(len(word.GetTiles())) :
                tile = word.GetTiles()[i]
                if i is not anchorIndex :
                    if not self.PrefixAndSuffixClear(Word([tile]), anchor, anchorIndex) : 
                        invalidWord = True
        return invalidWord

