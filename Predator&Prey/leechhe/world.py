class World:
	grids = world = [' '.join([ '-' for i in range(20)]) for j in range(20)]
	step = 0
	
	def nextStep():
		step += 1
	NextStep = staticmethod(nextStep)

	def isEmpty(position, direction):
		return grids[position.x+direction[0]][position.y+direction[1]] == '-'
	IsEmpty = staticmethod(isEmpty)
	
	def placeObject(sign, position):
		grids[position.x][position.y] = sign

	def moveTo(position, direction):
		placeObject(grids[position.x][position.y], position + direction)
		grids[position.x][position.y] = '-'
	MoveTo = staticmethod(MoveTo)
	def printState(self):
		print ("Time_step : %d" % self.step)
		for line in self.grids:
			print(line)