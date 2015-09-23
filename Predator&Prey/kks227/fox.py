from constant import *

# Fox class
class Fox:
	# member variables
	# x: x position
	# y: y position
	# breedTime: timing counter to breed
	# starveTime: timing counter to starve
	# didHunt: did the fox hunt this time?

	# constructor
	def __init__(self, x1=0, y1=0):
		self.x = x1
		self.y = y1
		self.breedTime = 0
		self.starveTime = 0
		self.didHunt = False

	# member functions
	def move(self, dir):
		if self.didHunt:
			self.didHunt = False
			return False
		self.x += XOFF[dir]
		self.y += YOFF[dir]
		return True

	def isTimeToBreed(self):
		self.breedTime += 1
		if self.breedTime == FOX_BREED:
			self.breedTime = 0
			return True
		return False

	def isTimeToStarve(self):
		self.starveTime += 1
		if self.starveTime == FOX_STARVE:
			return True
		return False

	def hunt(self, dir):
		self.starveTime = -1
		self.didHunt = True
		self.x += XOFF[dir]
		self.y += YOFF[dir]