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
                if word[1] in self.dict : self.dict[word[1]].append(word[0])
                else : self.dict[word[1]] = [word[0]]

    def GetDict(self) :
        return self.dict

    # returns words that contain a certain tile
    def TileSearch(self, tile) :
        possibleWords = {}
        a = tile.GetPrime()
        for key, wordList in self.dict.items() :
            if (int(key) % int(a) == 0) :
                if key in possibleWords : 
                    for element in wordList : 
                        possibleWords[key].append(element)
                else : possibleWords[key] = wordList    
        return Words(possibleWords)

    # returns words that contain a set of tiles
    # the set of tiles can be in any order
    def WordSearch(self, word) :
        possibleWords = {}
        a = word.GetPrime()
        for key, wordList in self.dict.items() :
            if (int(a) % int(key) == 0) :
                if key in possibleWords : 
                    for element in wordList : 
                        possibleWords[key].append(element)
                else : possibleWords[key] = wordList    
        return Words(possibleWords)

    # returns words that contain a set of tiles
    # the set of tiles must be in the same order as passed
    def FixedWordSearch(self, word) :
        jumbledWords = {}
        possibleWords = {}
        for tile in word.GetTiles() :
            jumbledWords = self.TileSearch(tile)
        for key, wordList in jumbledWords.GetDict().items() :
            for element in wordList : 
                if (word.GetString() in element) :
                    if key in possibleWords : possibleWords[key].append(element)
                    else : possibleWords[key] = [element]
        return Words(possibleWords)

    # returns words that contain a set of tiles
    # the set of tiles must be in the same order as passed
    def ExactWordSearch(self, word) :
        key = str(word.GetPrime())
        value = word.GetString()
        possibleWords = self.GetDict().get(key)
        if possibleWords is None :
            return False
        elif value.upper() in possibleWords :
                return True
        else : 
            return False

    def AnchorSearch(self, word) :
        if len(word.GetTiles()) == 1 :
            return self.TileSearch(word.GetTiles()[0])
        else :
            return self.FixedWordSearch(word)