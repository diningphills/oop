from coordinate import Coordinate
import random

class BreedBehavior:
  def __init__(self, breeder, period):
    self.breeder = breeder
    self.period = period

  def run(self, game):
    if self.breeder.age % self.period != 0:
      return

    positions = self.breedable_positions(game)
    if len(positions) == 0:
      return

    position = random.choice(positions)

    breedee = self.breeder.__class__()
    breedee.position = position
    game.request_add(breedee)
    game.world_map.set(position, breedee)

  def breedable_positions(self, game):
    breedables = []
    for (col, row) in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
      c = self.breeder.position + Coordinate(col, row)
      if game.world_map.at(c) == None:
        breedables.append(c)

    return breedables