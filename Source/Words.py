"""

Contains the Words class
Holds the dictionary for all of the possible words

"""

import os
import pandas as pd

from Tile import Tile
from Word import Word


class Words :

    def __init__(self, words={}) :
        self.dict = words
        if not len(words) :
            directory = os.path.dirname(__file__)
            words_df = pd.read_csv(directory + "/../Data/processed_words.txt")
            words = words_df.values[:, 0:2]
            for word in words :
                if word[1] in self.dict :
                    self.dict[word[1]].append(word[0])
                else :
                    self.dict[word[1]] = [word[0]]

    def GetDict(self) :
        return self.dict

    # returns words that contain a certain tile
    def TileSearch(self, tile) :
        possibleWords = {}
        a = tile.GetPrime()
        for key in self.dict :
            if (int(key) % int(a) == 0) :
                possibleWords[key] = self.dict.get(key)        
        return Words(possibleWords)

    # returns words that contain a set of tiles
    # the set of tiles can be in any order
    def WordSearch(self, word) :
        possibleWords = {}
        a = word.GetPrime()
        for key in self.dict :
            if (int(a) % int(key) == 0) :
                possibleWords[key] = self.dict.get(key) 
        return Words(possibleWords)

    # returns words that contain a set of tiles
    # the set of tiles must be in the same order as passed
    def FixedWordSearch(self, word) :
        jumbledWords = self.WordSearch(word)
        possibleWords = {}
        for key in jumbledWords.GetDict() :
            w = jumbledWords.GetDict().get(key)
            if (w.Contains(word.GetString())) :
                possibleWords[key] = w 
        return Words(possibleWords)

    def AnchorSearch(self, word) :
        if len(word) == 1 :
            return self.TileSearch(word[0])
        else :
            return self.FixedWordSearch(word)