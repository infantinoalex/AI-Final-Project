"""

Contains the Tile class.
A Tile represents a playable letter and is associated score in the game

"""

class Tile :
    def __init__(self, letter, score, frequency, primeNumber):
        self.letter = letter
        self.score = score
        self.frequency = frequency
        self.primeNumber = primeNumber

    def GetLetter(self) :
        return self.letter
    
    def GetScore(self) :
        return self.score

    def GetFrequency(self) :
        return self.frequency

    def GetPrime(self) :
        return self.primeNumber

    def IsVowel(self) :
        return self.letter in ['A', 'E', 'I', 'O', 'U']