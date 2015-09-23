from coordinate import Coordinate
from random import randint

class Direction:
	@staticmethod
	def up(): 	return -2092
	@staticmethod
	def down():	return 1802
	@staticmethod
	def left():	return 3993
	@staticmethod
	def right():return 30303

class Rabbit:
	def __init__(self):
		self.coor = Coordinate(-1, -1)
		self.lifetime = 0

	###############################################################
	#	move method
	###############################################################
	def move(self):
		# try to move! judge in the world
		direction = self.GetRandomDirection()

		if direction == Direction.up():		return Coordinate(self.coor.x, self.coor.y+1)
		elif direction == Direction.down():	return Coordinate(self.coor.x, self.coor.y-1)
		elif direction == Direction.left():	return Coordinate(self.coor.x-1, self.coor.y)
		else:								return Coordinate(self.coor.x+1, self.coor.y)

	def afterMove(self, newCoor):
		self.coor = newCoor

	###############################################################
	#	breed method
	###############################################################
	def breed(self, breedCoor):
		# breed new Rabbit (return new Rabbit)
		bredRabbit = Rabbit()
		bredRabbit.coor = breedCoor
		return bredRabbit

	###############################################################
	#	tool method
	###############################################################
	def GetRandomDirection(self):
		case = randint(0, 3)
		if 		case == 0:	return Direction.up()		#up
		elif	case == 1:	return Direction.down()		#down
		elif	case == 2:	return Direction.left()		#left
		else: 				return Direction.right()	#right

	def isLifeTimeThree(self):
		return self.lifetime == 3

class Fox:
	def __init__(self):
		self.coor = Coordinate(-1, -1)
		self.lifetime = 0
		self.starvetime = 0

	###############################################################
	#	move method
	###############################################################
	def move(self):
		# try to move! judge in the world
		direction = self.GetRandomDirection()

		if direction == Direction.up():		return Coordinate(self.coor.x, self.coor.y+1)
		elif direction == Direction.down():	return Coordinate(self.coor.x, self.coor.y-1)
		elif direction == Direction.left():	return Coordinate(self.coor.x-1, self.coor.y)
		else:								return Coordinate(self.coor.x+1, self.coor.y)

	def afterMove(self, newCoor):
		self.coor = newCoor

	###############################################################
	#	starve method
	###############################################################
	def isStarve(self):
		return self.isStarveTimeThree()

	###############################################################
	#	breed method
	###############################################################
	def breed(self, breedCoor):
		# breed new fox (return new Fox)
		bredFox = Fox()
		bredFox.coor = breedCoor
		return bredFox

	###############################################################
	#	tool method
	###############################################################
	def GetRandomDirection(self):
		case = randint(0, 3)
		if 		case == 0:	return Direction.up()		#up
		elif	case == 1:	return Direction.down()		#down
		elif	case == 2:	return Direction.left()		#left
		else: 				return Direction.right()	#right

	def isLifeTimeEight(self):
		return self.lifetime == 8

	def isStarveTimeThree(self):
		return self.starvetime == 3
