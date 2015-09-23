import random

class Animal:
	def __init__(self, _pos):
		self.position = _pos
		self.sign = ''
		self.breed_counter = 3

	#Find new position and update on global map.
	def move(self, grids):
		new_position = self.emptyDirection(grids)

		#if there is no place to move
		if new_position[0] < 0 : return None;

		#Move to the empty grid(swap)
		#Update on global map
		grids[self.position[0]][self.position[1]] = grids[new_position[0]][new_position[1]]
		grids[new_position[0]][new_position[1]] = self.sign
		return new_position
		
		
		
	
	#Return the coordinate of breed-grid
	#if impossible, return (-1,-1)
	def breed(self, grids):
		self.breed_counter -= 1
		if self.breed_counter >= 0 : return (-1, -1);
		return self.emptyDirection(grids)

	def isEmpty(self, grids, pos) :
		if pos[0] < 0 or pos[0] > 19 : return False;
		if pos[1] < 0 or pos[1] > 19 : return False;
		return grids[pos[0]][pos[1]] == '-'
	
	#Return the coordinate of empty grid.
	#if impossible, return (-1,-1)
	def emptyDirection(self, grids):
		directions = { (-1,0), (1,0), (0,-1), (0,1)}
		ret = []
		for direction in directions:
			position = (self.position[0]+direction[0], self.position[1]+direction[1])
			if self.isEmpty(grids, position):
				ret.append(direction)
		if len(ret) > 0 :
			d = random.choice(ret)
			return (d[0] + self.position[0], d[1] + self.position[1])
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

	def showState(self):
		print(self._animals[0].sign)
		for animal in self._animals:
			print(animal.position)



