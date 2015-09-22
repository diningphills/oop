import coordinate

class WorldMap:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.underlying = [[None for x in range(height)] for x in range(width)]

  def inspect(self):
    for i in range(self.height):
      for j in range(self.width):
        object = self.underlying[i][j]
        if object == None:
          print("%-6s" % ".", end="")
        else:
          print("%-6s" % object, end="")
      print("")

  def set_randomly(self, object):
    while True:
      c = coordinate.rand(self.height, self.width)
      if self.underlying[c.row][c.col] == None:
        self.underlying[c.row][c.col] = object
        object.position = c
        break

  def at(self, coordinate):
    row, col = coordinate.row, coordinate.col
    if row < 0 or row >= self.height or col < 0 or col >= self.width:
      return False
    else:
      return self.underlying[row][col]

  def set(self, coordinate, object):
    self.underlying[coordinate.row][coordinate.col] = object

  def request_move(self, object, dest):
    self.set(dest, object)
    src = object.position
    self.set(src, None)
    object.position = dest

  def remove(self, target):
    for i in range(self.height):
      for j in range(self.width):
        if self.underlying[i][j] == target:
          self.underlying[i][j] = None
          return