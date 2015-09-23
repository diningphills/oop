from coordinate import Coordinate
from eat_behavior import EatBehavior
from move_behavior import MoveBehavior
from breed_behavior import BreedBehavior
from starve_behavior import StarveBehavior
from rabbit import Rabbit

class Fox:
  def __init__(self):
    self.age = 0
    self.dead = False
    self.position = Coordinate()
    self.move_behavior = MoveBehavior(self)
    self.eat_behavior = EatBehavior(self, [Rabbit])
    self.breed_behavior = BreedBehavior(self, 8)
    self.starve_behavior = StarveBehavior(self, 3)

  def __repr__(self):
    return "F(%d,%d)" % (self.age, self.starve)

  def __str__(self):
    return "F(%d,%d)" % (self.age, self.starve)

  def update(self, game):
    if self.dead:
      return

    self.age += 1

    success = self.eat_behavior.run(game)
    if not success:
      self.move_behavior.run(game)
    self.breed_behavior.run(game)
    self.starve_behavior.run(game)

  def die(self, game):
    self.dead = True
    game.world_map.remove(self)