import critter

from random import randint
from coordinate import Coordinate

class Cell:
	def __init__(self):
		self.critter = None	# empty status

	def isEmpty(self):
		if self.critter is None:	return True
		else:						return False

	def SetEmpty(self):
		self.critter = None

	def SetCritter(self, critter):
		self.critter = critter


class World:
	###############################################################
	#	initial method
	###############################################################
	def __init__(self, numberOfRabbit, numberOfFox):
		self.maxX = 20
		self.maxY = 20
		self.cells = [[Cell() for _ in range(self.maxX)] for _ in range(self.maxY)]
		self.totalTimeStep = 0

		# initWorld
		self.initWorld(numberOfRabbit, numberOfFox)

	def initWorld(self, numberOfRabbit, numberOfFox):	#number of foxes need added
		self.initRabbits(numberOfRabbit)
		self.initFoxes(numberOfFox)

	def initRabbits(self, numberOfRabbit):
		for i in range(numberOfRabbit):
			while True:
				randomCoor = self.GetRandomCoor()
				if self.isCellEmpty(randomCoor):
					newRabbit = critter.Rabbit()
					newRabbit.coor = randomCoor
					self.SetCell(randomCoor, newRabbit)
					break
				else:	continue

	def initFoxes(self, numberOfFox):
		for i in range(numberOfFox):
			while True:
				randomCoor = self.GetRandomCoor()
				if self.isCellEmpty(randomCoor):
					newFox = critter.Fox()
					newFox.coor = randomCoor
					self.SetCell(randomCoor, newFox)
					break
				else:	continue


	###############################################################
	#	world's time flow method
	###############################################################
	def timeStep(self):
		self.triggerMoveEvents()
		self.triggerStarveEvents()
		self.triggerBreedEvents()
		self.triggerLifeTimeEvents()
		self.triggerStarveTimeEvents()
		self.totalTimeStep += 1

	###############################################################
	#	move trigger method
	###############################################################
	def triggerMoveEvents(self):
		self.triggerFoxMoveEvent()
		self.triggerRabbitMoveEvent()

	def triggerRabbitMoveEvent(self):
		rabbits = self.GetRabbits()

		for rabbit in rabbits:
			newCoor = rabbit.move()
			if self.isCanMove(newCoor):
				self.SetCell(rabbit.coor, None)
				rabbit.afterMove(newCoor)
				self.SetCell(newCoor, rabbit)
			else: pass

	def triggerFoxMoveEvent(self):
		foxes = self.GetFoxes()

		for fox in foxes:
			if self.isRabbitInAdjacentCoor(fox.coor):
				self.eatRabbit(fox)
			else:
				newCoor = fox.move()
				if self.isCanMove(newCoor):
					self.SetCell(fox.coor, None)
					fox.afterMove(newCoor)
					self.SetCell(newCoor, fox)
				else: pass

	###############################################################
	#	eat rabbit method
	###############################################################
	def eatRabbit(self, fox):
		self.SetCell(fox.coor, None)
		targetRabbitCoor = self.GetRabbitInAdjacentCoor(fox.coor)
		fox.coor = targetRabbitCoor
		fox.starvetime = 0
		self.SetCell(targetRabbitCoor, fox)

	###############################################################
	#	breed trigger method
	###############################################################
	def triggerBreedEvents(self):
		self.triggerRabbitBreedEvent()
		self.triggerFoxBreedEvent()

	def triggerRabbitBreedEvent(self):
		rabbits = self.GetRabbits()

		for rabbit in rabbits:
			if rabbit.isLifeTimeThree():
				rabbit.lifetime = 0
				if self.isNoEmptySurround(rabbit.coor): pass
				else:
					breedCoor = self.GetRandomAdjacentCoor(rabbit.coor)
					bredRabbit = rabbit.breed(breedCoor)
					self.SetCell(breedCoor, bredRabbit)

			else: pass

	def triggerFoxBreedEvent(self):
		foxes = self.GetFoxes()

		for fox in foxes:
			if fox.isLifeTimeEight():
				fox.lifetime = 0
				if self.isNoEmptySurround(fox.coor): pass
				else:
					breedCoor = self.GetRandomAdjacentCoor(fox.coor)
					bredFox = fox.breed(breedCoor)
					self.SetCell(breedCoor, bredFox)

			else: pass

	###############################################################
	#	life time, starve time trigger method
	###############################################################
	def triggerLifeTimeEvents(self):
		self.triggerRabbitLifeTimeEvent()
		self.triggerFoxLifeTimeEvent()

	def triggerRabbitLifeTimeEvent(self):
		rabbits = self.GetRabbits()

		for rabbit in rabbits:
			rabbit.lifetime += 1

	def triggerFoxLifeTimeEvent(self):
		foxes = self.GetFoxes()

		for fox in foxes:
			fox.lifetime += 1

	def triggerStarveTimeEvents(self):
		self.triggerFoxStarveTimeEvent()

	def triggerFoxStarveTimeEvent(self):
		foxes = self.GetFoxes()

		for fox in foxes:
			fox.starvetime += 1

	###############################################################
	#	starve trigger method
	###############################################################
	def triggerStarveEvents(self):
		self.triggerFoxStarveEvent()

	def triggerFoxStarveEvent(self):
		foxes = self.GetFoxes()

		for fox in foxes:
			if fox.isStarve():
				self.foxStarve(fox)

	def foxStarve(self, fox):
		self.SetCell(fox.coor, None)
	###############################################################
	#	Getter method
	###############################################################
	def GetRabbits(self):
		rabbits = []
		for cellblock in self.cells:
			for cell in cellblock:
				if isinstance(cell.critter, critter.Rabbit):
					rabbits.append(cell.critter)
				else:	pass
		return rabbits

	def GetFoxes(self):
		foxes = []
		for cellblock in self.cells:	# x block
			for cell in cellblock:		# same x block, y cells
				if isinstance(cell.critter, critter.Fox):	foxes.append(cell.critter)
				else:	pass
		return foxes

	###############################################################
	#	print method
	###############################################################
	def printWorld(self):
		print("time_step: " + str(self.totalTimeStep))
		print("")

		for cellblock in self.cells:
			for cell in cellblock:
				if cell.critter is None:							print("- "),
				elif isinstance(cell.critter, critter.Rabbit):		print("O "),
				elif isinstance(cell.critter, critter.Fox):			print("X "),
				else: print("<World.printWorld>::Error! wrong object in cell")
			print("")
	
	###############################################################
	#	cell Getter method
	###############################################################
	def GetCritterFromCell(self, coor):
		if self.isOffGrid(coor):
			print("<World.GetCritterFromCell>::Error! current coordinate is Off Grid")
		return self.cells[coor.x][coor.y].critter

	###############################################################
	#	cell Setter method
	###############################################################
	def SetCell(self, coor, critter):
		if self.isOffGrid(coor): print("<World.SetCell>::Error! current coordinate is Off Grid")

		if critter is None:	self.SetCellEmpty(coor)
		else:				self.cells[coor.x][coor.y].SetCritter(critter)
	
	def SetCellEmpty(self, coor):
		self.cells[coor.x][coor.y].SetEmpty()

	###############################################################
	#	tool method
	###############################################################
	def GetRandomCoor(self):
		return Coordinate(randint(0, self.maxX-1), randint(0, self.maxX-1))

	def isCellEmpty(self, coor):
		if self.cells[coor.x][coor.y].isEmpty():	return True
		else:										return False

	def isOffGrid(self, coor):
		if coor.x < 0 or coor.y < 0 or coor.x >= self.maxX or coor.y >= self.maxY:	return True
		else: 																		return False

	def isCanMove(self, coor):
		if not self.isOffGrid(coor) and self.isCellEmpty(coor):	return True
		else:													return False

	def isNoEmptySurround(self, coor):
		up 		= Coordinate(coor.x, coor.y+1)
		down	= Coordinate(coor.x, coor.y-1)
		left	= Coordinate(coor.x-1, coor.y)
		right	= Coordinate(coor.x+1, coor.y)

		if not self.isCanMove(up) and not self.isCanMove(down) and not self.isCanMove(left) and not self.isCanMove(right):	return True
		else:																												return False

	def GetRandomAdjacentCoor(self, coor):
		up 		= Coordinate(coor.x, coor.y+1)
		down	= Coordinate(coor.x, coor.y-1)
		left	= Coordinate(coor.x-1, coor.y)
		right	= Coordinate(coor.x+1, coor.y)

		while True:
			rand = randint(0, 3)
			if 		rand == 0 and self.isCanMove(up):	return up
			elif	rand == 1 and self.isCanMove(down):	return down
			elif	rand == 2 and self.isCanMove(left):	return left
			elif	rand == 3 and self.isCanMove(right):	return right
			else:	continue

	def isRabbitInCoor(self, coor):
		if self.isOffGrid(coor): return False

		rabbitOrNot = self.GetCritterFromCell(coor)
		if isinstance(rabbitOrNot, critter.Rabbit):	return True
		else:										return False

	def isRabbitInAdjacentCoor(self, coor):
		up 		= Coordinate(coor.x, coor.y+1)
		down	= Coordinate(coor.x, coor.y-1)
		left	= Coordinate(coor.x-1, coor.y)
		right	= Coordinate(coor.x+1, coor.y)

		if self.isRabbitInCoor(up) or self.isRabbitInCoor(down) or self.isRabbitInCoor(left) or self.isRabbitInCoor(right): return True
		else: return False

	def GetRabbitInAdjacentCoor(self, coor):
		up 		= Coordinate(coor.x, coor.y+1)
		down	= Coordinate(coor.x, coor.y-1)
		left	= Coordinate(coor.x-1, coor.y)
		right	= Coordinate(coor.x+1, coor.y)

		if 		self.isRabbitInCoor(up):		return up
		elif	self.isRabbitInCoor(down):	return down
		elif	self.isRabbitInCoor(left):	return left
		elif	self.isRabbitInCoor(right):	return right