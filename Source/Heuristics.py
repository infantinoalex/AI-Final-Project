from ReadInFiles import ReadInTilesFromFile
from math import e

def CalculateHeuristic(longestWordScale, uncommonLetterScale, ratioScale, scoreWordScale) :
    heuristics = []
    longestWordHeuristic = LongestWordHeuristic(longestWordScale)
    uncommonLetterHeuristic = UncommonLettersHeuristic(uncommonLetterScale)
    ratioHeuristic = ConsonantVowelHeuristic(ratioScale)
    scoreWordHeuristic = LetterScoringHeuristic(scoreWordScale)

    heuristics.append(longestWordHeuristic)
    heuristics.append(uncommonLetterHeuristic)
    heuristics.append(ratioHeuristic)
    heuristics.append(scoreWordHeuristic)

    return Heuristic(heuristics)

class Heuristic :
    def __init__(self, hueristics=[]) :
        self.heuristcs = hueristics

    def ScoreWord(self, wordToPlay, hand) :
        score = 0
        for hueristicToCheck in self.heuristcs :
            result = hueristicToCheck.ScoreWord(wordToPlay, hand)
            result *= hueristicToCheck.Scale()
            score += result

        return score

    def Scale(self) :
        return 1

class NullHeuristic :
    def __init__(self, scale) :
        self.scale = scale

    def ScoreWord(self, wordToPlay, hand) :
        return 0

    def Scale(self) :
        return self.scale

class LongestWordHeuristic :
    def __init__(self, scale) :
        self.scale = scale

    def ScoreWord(self, wordToPlay, hand) :
        count = len(wordToPlay.GetTiles())

        return count

    def Scale(self) :
        return self.scale

class UncommonLettersHeuristic :
    def __init__(self, scale) :
        self.letterScoreDictionary = {}
        tiles = ReadInTilesFromFile("..\\Data\\processed_letters.txt")
        for tile in tiles :
            letter = tile.GetLetter()
            score = tile.GetScore()
            if letter not in self.letterScoreDictionary  :
                self.letterScoreDictionary[letter] = score

        self.scale = scale

    def ScoreWord(self, wordToPlay, hand) :
        score = 0
        for tile in wordToPlay.GetTiles() :
            letterScore = self.letterScoreDictionary[tile.GetLetter()]
            score += e ** (letterScore / 3)
                
        return score

    def Scale(self) :
        return self.scale

class ConsonantVowelHeuristic :
    def __init__(self, scale) :
        self.letterScoreDictionary = {}
        tiles = ReadInTilesFromFile("..\\Data\\processed_letters.txt")
        for tile in tiles :
            letter = tile.GetLetter()
            if letter not in self.letterScoreDictionary  :
                self.letterScoreDictionary[letter] = tile
        
        self.scale = scale

    def ScoreWord(self, wordToPlay, hand) :
        numberOfConsonants = 0
        numberOfVowels = 0

        handTiles = hand.PeekHand()
        handTilesLetters = []

        for tile in handTiles :
            handTilesLetters.append(tile.GetLetter())

        for tile in wordToPlay.GetTiles() :
            foundTile = self.letterScoreDictionary[tile.GetLetter()]

            handTilesLetters.remove(foundTile.GetLetter())

        for tile in hand.PeekHand() :
            if (tile.IsVowel) :
                numberOfVowels += 1
            else :
                numberOfConsonants += 1

        ratio = float(numberOfConsonants) / float(numberOfVowels)

        #return (-(ratio - 1.3)) * (ratio - 2.5) 
        return (-10.0 * (ratio - 1.7)) * (ratio - 2.7) 

    def Scale(self) :
        return self.scale

class LetterScoringHeuristic :
    def __init__(self, scale) :
        self.letterScoreDictionary = {}
        tiles = ReadInTilesFromFile("..\Data\processed_letters.txt")
        for tile in tiles :
            letter = tile.GetLetter()
            score = tile.GetScore()
            if letter not in self.letterScoreDictionary  :
                self.letterScoreDictionary[letter] = score

        self.scale = scale


    def ScoreWord(self, wordToPlay, hand) :
        score = 0
        for tile in wordToPlay.GetTiles() :
            score += self.letterScoreDictionary[tile.GetLetter()]

        return score

    def Scale(self) :
        return self.scale
