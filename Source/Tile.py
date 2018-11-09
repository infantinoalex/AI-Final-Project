"""

Contains the Tile class.
A Tile represents a playable letter and is associated score in the game

"""

class Tile :
    def __init__(self, letter, score):
        self.letter = letter
        self.score = score

    def GetLetter(self) :
        return self.letter
    
    def GetScore(self) :
        return self.score

    def IsVowel(self) :
        return self.letter in ['A', 'E', 'I', 'O', 'U']