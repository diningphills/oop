from constant import *

# Rabbit class
class Rabbit:
	# member variables
	# x: x position
	# y: y position
	# breedTime: timing counter to breed

	# constructor
	def __init__(self, x1=0, y1=0):
		self.x = x1
		self.y = y1
		self.breedTime = 0

	# member functions
	def move(self, dir):
		self.x += XOFF[dir]
		self.y += YOFF[dir]
		return True

	def isTimeToBreed(self):
		self.breedTime += 1
		if self.breedTime == RABBIT_BREED:
			self.breedTime = 0
			return True
		return False