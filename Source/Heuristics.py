from ReadInFiles import ReadInTilesFromFile

class Heuristic :
    def ScoreWord(self, wordToPlay, hand) :
        return 0

class LongestWordHeuristic(Heuristic) :
    def ScoreWord(self, wordToPlay, hand) :
        count = len(wordToPlay)

        # First Ranked Heuristic
        count *= 100

        return count

class UncommonLettersHeuristic(Heuristic) :
    def __init__(self) :
        self.letterScoreDictionary = {}
        tiles = ReadInTilesFromFile("..\\Data\\processed_letters.txt")
        for tile in tiles :
            letter = tile.GetLetter()
            score = tile.GetScore()
            if letter not in self.letterScoreDictionary  :
                self.letterScoreDictionary[letter] = score

    def ScoreWord(self, wordToPlay, hand) :
        score = 0
        for letter in wordToPlay :
            score = self.letterScoreDictionary[letter]
            if score > 5 :
                score += 10

        # Second Ranked Heuristic
        score *= 50
        return score

class ConsonantVowelHeuristic(Heuristic) :
    def __init__(self) :
        self.letterScoreDictionary = {}
        tiles = ReadInTilesFromFile("..\\Data\\processed_letters.txt")
        for tile in tiles :
            letter = tile.GetLetter()
            score = tile.GetScore()
            if letter not in self.letterScoreDictionary  :
                self.letterScoreDictionary[letter] = tile

    def ScoreWord(self, wordToPlay, hand) :
        numberOfConsonants = 0
        numberOfVowels = 0

        score = 0
        for letter in wordToPlay :
            foundTile = self.letterScoreDictionary[letter]

            hand.RemoveTileFromHand(foundTile)

        for tile in hand :
            if (tile.IsVowel) :
                numberOfVowels += 1
            else :
                numberOfConsonants += 1

        ratio = (float)numberOfConsonants / (float)numberOfVowels

        if ratio <= 2.5 and ratio >= 1.3 :
            score += 25
        
        else :
            ratio += 5

        # Third Ranked Heuristic
        score *= 25

        return score

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

        # Fourth Scoring Heuristic
        score *= 10

        return score