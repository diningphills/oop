import rabbit
import world

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
		return self.rabbit_manager.count() == 0 or self.fox_manager.count() == 0

	def showTimeStep(self):
		print("Time_step : %d" %(self.time_step))
		print()

	def drawWorld(self):
		for line in grids :
			print(' '.join(line))
		print()

	def move(self):
		self.rabbit_manager.move(self.grids)
		self.rabbit_manager.breed(self.grids)

		self.fox_manager.move(self.grids)
		self.fox_manager.starve()
		self.fox_manager.breed(self.grids)

	def increaseTime(self):
		self.time_step += 1
		#TODO : count down life time




