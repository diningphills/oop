import animal

class Fox(Animal):
	def __init__(self, _pos):
		super(Fox, self).__init__(_pos)
		self.sign = 'X'
		self.breed_counter = 8

	def breed(self, grids):
		breed_position = emptyDirection(grids)
		#if there is no place to move
		if breed_position[0] < 0 : return;
		return Rabbit(breed_position, self.sign)
	

class RabbitManager(AnimalManager):
	def __init__(self, _positions):
		super(RabbitManager, self).__init__()
		self._animals = [ Rabbit(position, 'O') for position in _positions]

