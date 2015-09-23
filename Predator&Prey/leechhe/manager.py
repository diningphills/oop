from random import shuffle
from rabbit import RabbitManager
from fox import FoxManager

class GameManager:
	def __init__(self):
		rabbit_count, fox_count = [int(input("Write the number of rabbits : ")), int(input("Write the number of foxes : "))]

		# make the random coordinate
		positions = []
		for x in range(20):
			for y in range(20):
				positions.append((x,y))
		shuffle(positions)

		#Initialize animal manager with random position
		self.rabbit_manager = RabbitManager(positions[:rabbit_count])
		self.fox_manager = FoxManager(positions[rabbit_count:rabbit_count+fox_count])
		
		#Assign the sign for each animals
		self.grids = [['-' for i in range(20)] for j in range(20)]
		for position in positions[:rabbit_count] :
			self.grids[position[0]][position[1]] = 'O'
		for position in positions[rabbit_count:rabbit_count+fox_count] :
			self.grids[position[0]][position[1]] = 'X'

		#Initialize time step
		self.time_step = 1

	def gameOver(self):
		#print('O :' + str(self.rabbit_manager.count()))
		#print('X :' + str(self.fox_manager.count()))
		return self.rabbit_manager.count() == 0 or self.fox_manager.count() == 0

	def showTimeStep(self):
		print("Time_step : %d" %(self.time_step))
		#self.rabbit_manager.showState()
		#self.fox_manager.showState()

	def drawWorld(self):
		for line in self.grids :
			print(' '.join(line))
		print()

	def move(self):
		hunted = self.fox_manager.move(self.grids)

		for rabbit_position in hunted:
			print("Rabbit on ", end="")
			print(rabbit_position, end="")
			print("is hunted.")
			self.rabbit_manager.hunted(rabbit_position)
		
		self.fox_manager.starve(self.grids)
		self.fox_manager.breed(self.grids)

		self.rabbit_manager.move(self.grids)
		self.rabbit_manager.breed(self.grids)

	def increaseTime(self):
		self.time_step += 1
		#TODO : count down life time





