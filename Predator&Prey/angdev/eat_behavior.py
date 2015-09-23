from coordinate import Coordinate
import random

class EatBehavior:
  def __init__(self, eater, eatable_classes):
    self.eater = eater
    self.eatable_classes = eatable_classes

  def run(self, game):
    eatables = self.eatable_position(game)
    if len(eatables) == 0:
      return False

    self.eater.starve = 0

    feed = random.choice(eatables)
    game.world_map.request_move(self.eater, feed.position)
    feed.die(game)

    return True

  def eatable_position(self, game):
    eatables = []
    for (col, row) in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
      c = self.eater.position + Coordinate(col, row)
      obj = game.world_map.at(c)
      if obj != None and any(isinstance(obj, klass) for klass in self.eatable_classes):
        eatables.append(obj)

    return eatables