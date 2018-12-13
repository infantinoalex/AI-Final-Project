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
import sys
import random

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
		for t in self.hand.PeekHand():
			print(t.GetLetter(), end=" ")
		print()
		while not self.IsEndState():
			try :
				word, anchor, anchorIndex, direction = self.bri.FindBestMove(self.hand, self.board)
				playedWords.append(word.GetString())
				
				self.board.PlaceWord(word, anchor, self.hand, anchorIndex, direction)
				self.concurrentExceptions = 0
				self.board.PrintBoard()

				print()
				print(playedWords)
				print()
				print("Hand Score: ", self.hand.GetScore())
				print("Bunch Score: ", self.bunch.ScoreBunch())
				print("Total Score: ", self.hand.GetScore() + self.bunch.ScoreBunch())
				print("Items left in bunch: ", len(self.bunch.GetBunch()))

			except Exception as ex:
				#print("\t Error trying to get best move")
				print("\t", ex)
				self.concurrentExceptions += 1

			self.hand.AddTilesToHand(self.bunch.Peel())
			for t in self.hand.PeekHand():
				print(t.GetLetter(), end=" ")
			print()

			timeDiff = time.time() - timeStart
			#print("Time:", timeDiff)
			self.timer = self.time - timeDiff

		if self.IsGoalState():
			print("Goal achieved! BRI is the winner!")

		if self.IsTimeOut():
			print("Game timed out! Sorry, try harder next time")

		handScore = self.hand.GetScore()
		bunchScore = self.bunch.ScoreBunch()
		print("Hand score: ", handScore)
		print("Bunch score: ", bunchScore)
		print("Total score: ", handScore + bunchScore)
		if self.concurrentExceptions > 5 :
			print("Too many exceptions thrown")

		print("Words played were:", playedWords)

		results = []
		for t in self.hand.PeekHand():
			results.append(t.GetLetter())

		return [handScore + bunchScore, results]


def main() :
	#longestWordScale = sys.argv[1]
	#uncommonLetterScale = sys.argv[2]
	#ratioScale = sys.argv[3]
	#scoreWordScale = sys.argv[4]

	#longestWordScale, uncommonLetterScale, ratioScale, scoreWordScale, playableWordsCheck
	
	size1 = 10
	size2 = 3

	a = 1.0
	b = 1.0
	c = 1.0
	d = 1.0
	e = 1.0
	lrate_a = 1
	lrate_b = 1
	lrate_c = 1
	lrate_d = 1
	lrate_e = 1

	heuristic = CalculateHeuristic(a, b, c, d, e)
	game = Game(heuristic)
	best_results = 100000
	results = []

	for i in range(size1) :

		heuristic = CalculateHeuristic(a * lrate_a, b * lrate_b, c * lrate_c, d * lrate_d, e * lrate_e)

		for j in range(size2) :
			game = Game(heuristic)
			results.append(game.Play()[0])

		print("==================================================================")
		print(results)
		new_results = sum(results) / len(results)
		print(new_results)

		if new_results < best_results :
			best_results = new_results
			results = []
			lrate_a = a * lrate_a
			lrate_b = b * lrate_b
			lrate_c = c * lrate_c
			lrate_d = d * lrate_d
			lrate_e = e * lrate_e
		
		print("new a:", lrate_a)
		print("new b:", lrate_b)
		print("new c:", lrate_c)
		print("new d:", lrate_d)
		print("new e:", lrate_e)	
		
		lrate_a = random.uniform(0.0, 2.0)
		lrate_b = random.uniform(0.0, 2.0)
		lrate_c = random.uniform(0.0, 2.0)
		lrate_d = random.uniform(0.0, 2.0)
		lrate_e = random.uniform(0.0, 2.0)

		print("==================================================================")

	#for i in range(size) :
	#	print(scoreResults[i], ":", remainingLetterResults[i])

if __name__ == '__main__' :
	main()