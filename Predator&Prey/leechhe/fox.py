from animal import Animal, AnimalManager

class Fox(Animal):
	def __init__(self, _pos):
		super(Fox, self).__init__(_pos)
		self.sign = 'X'
		self.breed_counter = 8
		self.starve_counter = 3

	#Return the sibling.
	#If impossible, return None
	def breed(self, grids):
		breed_position = super(Fox, self).breed(grids)
		# if there is no place to breed or it's not time to do
		if breed_position[0] < 0 : return;

		#Initialize counter
		self.breed_counter = 8
		return Fox(breed_position)

	def isRabbit(self, grids, pos) :
		if pos[0] < 0 or pos[0] > 19 : return False;
		if pos[1] < 0 or pos[1] > 19 : return False;
		return grids[pos[0]][pos[1]] == 'O'

	#Return the position of rabbit be caught
	#if fails, return (-1, -1)
	def move(self, grids):
		prey_position = self.adjacentPrey(grids)
		new_position = None

		#if huting is successful,
		if prey_position[0] >= 0:
			new_position = prey_position
			grids[new_position[0]][new_position[1]] = self.sign
			grids[self.position[0]][self.position[1]] = '-'
			self.starve_counter = 4
		else :
			new_position = super(Fox, self).move(grids)
		# if new_position is not None:
		# 	# Catch a rabbit.
		# grids[self.position[0]][self.position[1]] = '-'
		self.position = new_position
		return prey_position

	def starve(self, grids):
		self.starve_counter -= 1
		if self.starve_counter <= 0:
			grids[self.position[0]][self.position[1]] = '-'
			return True
		return False

	#if fail to find the prey, return (-1, -1)
	def adjacentPrey(self,grids):
		#check from upward direction. clockwise.
		for direction in [(-1,0),(0,1),(1,0),(0,-1)]:
			current = (self.position[0] + direction[0], self.position[1] + direction[1])
			if self.isRabbit(grids, current) :
				return current
		return (-1,-1)

class FoxManager(AnimalManager):
	def __init__(self, _positions):
		super(FoxManager, self).__init__()
		self._animals = [ Fox(position) for position in _positions]

	def starve(self, grids):
		self._animals = list(filter(lambda fox : not fox.starve(grids), self._animals ))

	#return the list of hunted rabbits' positions
	def move(self, grids):
		hunted = list()
		for animal in self._animals:
			prey_position = animal.move(grids)
			#if catch a rabbit,
			if prey_position[0] > -1 :
				hunted.append(prey_position)
		return hunted
