"""
	Game class
	Main driver for the game of Bananagrams
"""

import time
from Board import Board
from Bunch import Bunch
from Hand import Hand
from BRI import BRI
from Heuristics import *
from ReadInFiles import ReadInTilesFromFile
import Tile
from sys import argv

class Game:
	def __init__(self, heuristic):
		self.bunch = Bunch()
		handTiles = self.bunch.DealFromBunch(15)
		self.hand = Hand("BRI", handTiles)
		self.bunch.DealFromBunch(15)
		self.board = Board()
		self.board.PrintBoard()

		self.concurrentExceptions = 0
		self.bri = BRI(heuristic)
		self.time = 1000
		self.timer = self.time #nanoseconds

	def IsGoalState(self):
		#print("Goal State:", self.bunch.IsBunchEmpty(), self.hand.IsHandEmpty())
		return self.bunch.IsBunchEmpty() and self.hand.IsHandEmpty()

	def IsTimeOut(self):
		#print("Time out:", self.timer)
		return self.timer <= 0

	def IsEndState(self):
		return self.IsGoalState() or self.IsTimeOut()  or self.concurrentExceptions > 5

	# also should consider timer for BRI i.e. cap time spent calculating a move
	# though maybe we won't need that actually
	def Play(self):
		timeStart = time.time()
		playedWords = []
		while not self.IsEndState():
			try :
				word, anchor, anchorIndex, direction = self.bri.FindBestMove(self.hand, self.board)
				playedWords.append(word.GetString())
				print(playedWords)
				self.board.PlaceWord(word, anchor, self.hand, anchorIndex, direction)
				self.board.PrintBoard()
			except:
				print("Error trying to get best move")
				self.concurrentExceptions += 1

			self.hand.AddTilesToHand(self.bunch.Peel())
			print(playedWords)
			for t in self.hand.PeekHand():
				print(t.GetLetter(), end=" ")
			print()
			handScore = self.hand.GetScore()
			bunchScore = self.bunch.ScoreBunch()
			print("Hand Score: ", handScore)
			print("Bunch Score: ", bunchScore)
			bunchList = self.bunch.GetBunch()
			bunchLength = len(bunchList)
			print("Items left in bunch: ", bunchLength)
			timeDiff = time.time() - timeStart
			print("Time:", timeDiff)
			self.timer = self.time - timeDiff

		if self.IsGoalState():
			print("Goal achieved! BRI is the winner!")

		if self.IsTimeOut():
			print("Game timed out! Sorry, try harder next time")

		handScore = self.hand.GetScore()
		bunchScore = self.bunch.ScoreBunch()
		print("Hand score: ", handScore)
		print("Bunch score: ", bunchScore)
		if self.concurrentExceptions > 5 :
			print("Too many exceptions thrown")

		print("Words played were:", playedWords)


if __name__ == '__main__' :
	main()

def main() :
	longestWordScale = sys.argv[1]
	uncommonLetterScale = sys.argv[2]
	ratioScale = sys.argv[3]
	scoreWordScale = sys.argv[4]

	heuristic = CalculateHeuristic(0, 0, 0, 0)

	game = Game(heuristic)
	game.Play()