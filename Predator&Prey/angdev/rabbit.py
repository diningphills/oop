from coordinate import Coordinate
from move_behavior import MoveBehavior
from breed_behavior import BreedBehavior

class Rabbit:
  def __init__(self):
    self.age = 0
    self.dead = False
    self.position = Coordinate()
    self.move_behavior = MoveBehavior(self)
    self.breed_behavior = BreedBehavior(self, 3)

  def __repr__(self):
    return "R(%d)" % self.age

  def __str__(self):
    return "R(%d)" % self.age

  def update(self, game):
    if self.dead:
      return

    self.age += 1

    self.move_behavior.run(game)
    self.breed_behavior.run(game)

  def die(self, game):
    self.dead = True
    game.world_map.remove(self)