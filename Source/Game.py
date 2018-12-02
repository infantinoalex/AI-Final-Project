"""
	Game class
	Main driver for the game of Bananagrams
"""

import time
from Board import Board
from Bunch import Bunch
from Hand import Hand
from BRI import BRI
from Heuristics import LongestWordHeuristic
from ReadInFiles import ReadInTilesFromFile
import Tile

class Game:
	def __init__(self, heuristic=LongestWordHeuristic()):
		self.bunch = Bunch()
		handTiles = self.bunch.DealFromBunch(15)
		self.hand = Hand("BRI", handTiles)
		self.bunch.DealFromBunch(15)
		self.board = Board()
		self.board.PrintBoard()
		self.bri = BRI(heuristic)
		self.time = 1
		self.timer = self.time #nanoseconds

	def IsGoalState(self):
		#print("Goal State:", self.bunch.IsBunchEmpty(), self.hand.IsHandEmpty())
		return self.bunch.IsBunchEmpty() and self.hand.IsHandEmpty()

	def IsTimeOut(self):
		#print("Time out:", self.timer)
		return self.timer <= 0

	def IsEndState(self):
		return self.IsGoalState() or self.IsTimeOut()

	# also should consider timer for BRI i.e. cap time spent calculating a move
	# though maybe we won't need that actually
	def Play(self):
		timeStart = time.time()
		while not self.IsEndState():
			anchors = self.board.GetAnchors()

			word, anchor, anchorIndex, direction = self.bri.FormWords(self.hand, self.board)
			self.board.PlaceWord(word, anchor, anchorIndex, direction)
			self.board.PrintBoard()

			timeDiff = time.time() - timeStart
			self.timer = self.time - timeDiff

		#if IsGoalState():
			# do something

		if self.IsTimeOut():
			print("Game timed out")


game = Game()
game.Play()
