import animal

class Rabbit(Animal):
	def __init__(self, _pos):
		super(Rabbit, self).__init__(_pos)
		self.sign = 'O'
		self.breed_counter = 3

	def breed(self, grids):
		breed_position = super(Rabbit, self).breed(grids)
		#if there is no place to move
		if breed_position[0] < 0 : return;

		return Rabbit(breed_position)


class RabbitManager(AnimalManager):
	def __init__(self, _positions):
		super(RabbitManager, self).__init__()
		self._animals = [ Rabbit(position, 'O') for position in _positions]

