import coordinate
import random

class Animal:
	def __init__(self, _pos):
		self.position = _pos
	def Move(self):
		self.position.MoveTo(self.__step)
	def Breed(self):
		
	def __state(self):
		x_limit = 1
		y_limit = 1
		if self.position.x == 0 || \
		self.position.y 
	def __step(self):
		direction = random.choice(self.position.MoveableDirections())
		if direction == "up":
			return (1,0)
		elif direction == "down":
			return (0,-1)
		elif direction == "left":
			return (-1,0)
		elif direction == "right":
			return (0,1)

