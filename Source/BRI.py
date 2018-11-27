from Word import Word
from Words import Words
from Board import Board

class BRI:
    def __init__(self, heuristic):
        self.heuristic = heuristic

    def FormWords(self, hand, board):
        #Return word, anchor, anchorindex, direction
        #Get words for each anchor, find best word, compare best words sequentially
        anchors = board.GetAnchors()
        for anchor in anchors:
            # get list of possible words for each anchor
            # match words to hand
            words = self.MatchWords(hand, anchor, board)
            # set scores for words, find best word
            for word in words:
                word.SetScore(self.heuristic.ScoreWord(word, hand))
                if word.GetScore() > bestWord.GetScore():
                    # indices where anchor exists in word aka anchorIndex
                    indices = [i for i, a in enumerate(word.GetString()) if a == anchor.GetData().GetString()]
                    for i in indices:
                        # anchorDirections
                        for d in ['across', 'down']:
                            if Board.IsWordLegal(word, anchor, i, d):
                                bestWord = word
                                bestAnchor = anchor
                                bestIndex = i
                                bestDirection = d
        # check for case no legal move is found
        return bestWord, bestAnchor, bestIndex, bestDirection

    def MatchWords(self, hand, anchor, board):
        # match available tiles in hand to possible words for a certain anchor
        anchorWords = anchor.GetPossibleWords()
        tiles = hand.PeekHand().append(anchor.GetData().GetTiles())
        totalHand = Word(tiles)
        options = anchorWords.WordSearch(totalHand)
        optionsCleaned = [word for word in options if board.IsWordLegal(word, anchor, word.GetString().index(anchor.GetData().GetString()))]
        return optionsCleaned

# tile1 = Tile('A', 1, 1, 1)
# word = Word(tile1)
# anchor = 

# FormWords(Anchor(Word(Tile())))