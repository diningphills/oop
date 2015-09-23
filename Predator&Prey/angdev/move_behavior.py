from coordinate import Coordinate
import random

class MoveBehavior:
  def __init__(self, movable):
    self.movable = movable

  def run(self, game):
    movables = self.movable_position(game)
    if len(movables) == 0:
      return

    dest = random.choice(movables)
    game.world_map.request_move(self.movable, dest)

  def movable_position(self, game):
    movables = []
    for (col, row) in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
      c = self.movable.position + Coordinate(col, row)
      if game.world_map.at(c) == None:
        movables.append(c)

    return movables