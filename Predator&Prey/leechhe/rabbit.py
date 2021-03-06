from animal import Animal, AnimalManager

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

	def move(self, grids):
		new_position = super(Rabbit, self).move(grids)
		if new_position is not None :
			#Set new position
			self.position = new_position

class RabbitManager(AnimalManager):
	def __init__(self, _positions):
		super(RabbitManager, self).__init__()
		self._animals = [ Rabbit(position) for position in _positions]

	def hunted(self, pos):
		self._animals = list(filter(lambda rabbit : not all(p == q for p, q in zip(rabbit.position, pos)), self._animals ))
