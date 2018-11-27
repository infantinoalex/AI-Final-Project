from Word import Word

class BRI:
    def __init__(self, heuristic):
        self.heuristic = heuristic

    def FormWords(self, anchors, hand):
        #Return word, anchor
        # How will we represent direction of the word? Should return that as well
        #Get words for each anchor, find best word, compare best words sequentially
        bestWord = Word() # initialize to empty word
        for anchor in anchors:
            # get list of possible words for each anchor
            anchorWords = anchor.GetPossibleWords()
            # match words to hand
            words, anchor = MatchWords(hand, anchorWords)
            # set scores for words, find best word
            for word in words:
                word.SetScore(self.heuristic.ScoreWord(word, hand))
                if word.GetScore() > bestWord.GetScore():
                    bestWord = word
                    bestAnchor = anchor
        return bestWord, bestAnchor

    def MatchWords(self, hand, wordList):
        # match available tiles in hand to possible words
        # return word, anchor

