import time
from Bunch import Bunch
from Hand import Hand
import Tile

class Game:
	def __init__(self, heuristic=None):
		self.bunch = Bunch()
		self.hand = Hand("BRI")
		tiles = self.bunch.DealFromBunch(15)
		self.hand.AddTilesToHand(tiles)
		self.bunch.DealFromBunch(15)
		# self.bri = BRI
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

	def Play(self):
		timeStart = time.time()
		while not self.IsEndState():

			timeDiff = time.time() - timeStart
			self.timer = self.time - timeDiff

		#if IsGoalState():
			# do something

		if self.IsTimeOut():
			print("Game timed out")


game = Game()
game.Play()
