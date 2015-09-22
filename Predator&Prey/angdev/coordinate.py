from random import randrange

class Coordinate:
  def __init__(self, row = 0, col = 0):
    self.row = row
    self.col = col

  def __repr__(self):
    return "(%d, %d)" % (self.row, self.col)

  def __str__(self):
    return "(%d, %d)" % (self.row, self.col)

  def __add__(self, other):
    return Coordinate(self.row + other.row, self.col + other.col)

def rand(row_range, col_range):
  row, col = randrange(0, row_range), randrange(0, col_range)
  return Coordinate(row, col)