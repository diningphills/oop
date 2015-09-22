states = { 0:"upper", 1:"below"}
class Position:
	def __init__(self, _x, _y):
		self.x = _x
		self.y = _y
	def __add__(self, other):
		pos = self
		pos.x += other.x
		pos.y += other.y
		return pos

	def MoveableDirections(self):
		directions = { "up":(-1,0), "down":(1,0), "left":(0,-1), "right":(0,1)}
		ret = []
		for direction in directions.items():
			if World.isEmpty(self, direction) :
				ret.append(direction)
		return ret

	def MoveTo(self, direction):
		self += direction