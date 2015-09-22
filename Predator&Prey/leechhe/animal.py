import coordinate
import random

class Animal:
	def __init__(self, _pos):
		self.position = _pos
		self.sign = ''
		self.breed_counter = 3

	def move(self, grids):
		new_position = emptyDirection(grids)

		#if there is no place to move
		if new_position[0] < 0 : return;

		#Move to the empty grid(swap)
		swap(grids[new_position[0]][new_position[1]], grids[self.position[0]][self.position[1]])
		#Set new position
		self.position = new_position
	
	def breed(self, grids):
		
		


	def isEmpty(grids, pos) :
		if pos[0] < 0 || pos[0] > 19 : return False;
		if pos[1] < 0 || pos[1] > 19 : return False;
		return grids[pos[0]][pos[1]] == '-'
	
	def emptyDirection(self, grids):
		directions = { (-1,0), (1,0), (0,-1), (0,1)}
		ret = []
		for direction in directions:
			if isEmpty(grids, [p+d for p,d in zip(self.position, direction])
				ret.append(direction)
		if len(ret) > 0 :
			d = random.choice(ret)
			return tuple(d[0] + self.position[0], d[1] + self.position[1])
		else :
			return (-1,-1)	


class AnimalManager:
	def __init__(self):
		self._animals = []
		pass

	def count(self):
		return len(self._animals)

	def move(self, grids):
		for animal in self._animals:
			animal.move(grids)

	def breed(self, grids):
		for animal in self._animals:
			sibling = animal.breed(grids)
			if sibling is not None :
				self._animals.append(sibling)



