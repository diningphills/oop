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
	
	def isEmpty(self,grids, pos) :
		if pos[0] < 0 or pos[0] > 19 : return False;
		if pos[1] < 0 or pos[1] > 19 : return False;
		return grids[pos[0]][pos[1]] != 'X'

	#Return the position of rabbit be caught
	def move(self, grids):
		new_position = super(Fox, self).move(grids)
		if new_position is not None:
			# Catch a rabbit.
			if grids[self.position[0]][self.position[1]] == 'O' :
				self.starve_counter = 3
				

			print('X at', end="")
			print(self.position, end="")
			print('to', end="")
			print(new_position)
			grids[self.position[0]][self.position[1]] = '-'
			self.position = new_position

	def starve(self):
		self.starve_counter -= 1
		return self.starve_counter <= 0

class FoxManager(AnimalManager):
	def __init__(self, _positions):
		super(FoxManager, self).__init__()
		self._animals = [ Fox(position) for position in _positions]

	def starve(self):
		self._animals = list(filter(lambda fox : not fox.starve(), self._animals ))
