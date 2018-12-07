from Word import Word
from Words import Words
from Board import Board
from Tile import Tile
import random
import time

class BRI:
    def __init__(self, heuristic):
        self.heuristic = heuristic

    def FindBestMove(self, hand, board):
        #Return word, anchor, anchorindex, direction
        #Get words for each anchor, find best word, compare best words sequentially
        anchors = board.GetAnchors()
        random.shuffle(anchors)
        bestWord = Word()
        bestWord.SetScore(-99999)
        for anchor in anchors:
            # get list of possible words for each anchor
            # match words to hand
            words = self.MatchWords(hand, anchor, board)
            # set scores for words, find best word
            for word in words.keys():
                word.SetScore(self.heuristic.ScoreWord(word, hand))
                if word.GetScore() > bestWord.GetScore():
                    bestWord = word
                    bestAnchor = anchor
                    bestIndex = words[word][0]
                    bestDirection = words[word][1]
        # check for case no legal move is found
        if bestWord.GetScore() is -99999:
            print("BRI: No valid word options found!")
            return None
        return bestWord, bestAnchor, bestIndex, bestDirection

    def MatchWords(self, hand, anchor, board):
        # match available tiles in hand to possible words for a certain anchor
        anchorWords = anchor.GetPossibleWords()
        handTiles = hand.PeekHand()
        anchorTile = anchor.GetTile()
        if anchorTile.GetLetter is " ":
            handTiles.append(anchorTile)
        tiles = handTiles
        totalHand = Word(tiles)
        options = anchorWords.WordSearch(totalHand)
        optionsCleaned = dict()
        direction = anchor.GetDirection()
        timeStart = time.time()
        print(anchor.GetLetter(), anchor.GetDirection())
        for key, strWordList in options.GetDict().items():
            for strWord in strWordList:
                word = self.MakeItWord(strWord)
                if anchor.GetLetter() is " ":
                    indices = [int(len(strWord)/2)]
                else:
                    indices = [i for i, a in enumerate(word.GetString()) if a == anchor.GetLetter() ]
                for i in indices:
                    if board.IsWordLegal(word, anchor, i, direction):
                        optionsCleaned[word] = (i, direction)
            timeDiff = time.time() - timeStart
            if (timeDiff > 2):
                break
        return optionsCleaned

    def MakeItWord(self, word):
        tiles = []
        for i in range(len(word)):
            tiles.append(Tile(word[i]))
        return Word(tiles)

# tile1 = Tile('A', 1, 1, 1)
# word = Word(tile1)
# anchor = 

# FormWords(Anchor(Word(Tile())))
