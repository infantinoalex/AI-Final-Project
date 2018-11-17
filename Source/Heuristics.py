from ReadInFiles import ReadInTilesFromFile

class Heuristic :
    def ScoreWord(self, wordToPlay, hand) :
        return 0

class LongestWordHeuristic(Heuristic) :
    def ScoreWord(self, wordToPlay, hand) :
        count = len(wordToPlay)
        return count

class LetterScoringHeuristic(Heuristic) :
    def __init__(self) :
        self.letterScoreDictionary = {}
        tiles = ReadInTilesFromFile("..\Data\processed_letters.txt")
        for tile in tiles :
            letter = tile.GetLetter()
            score = tile.GetScore()
            if letter not in self.letterScoreDictionary  :
                self.letterScoreDictionary[letter] = score


    def ScoreWord(self, wordToPlay, hand) :
        score = 0
        for letter in wordToPlay :
            score += self.letterScoreDictionary[letter]
        return score