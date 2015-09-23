class StarveBehavior:
  def __init__(self, mortality, limit):
    self.mortality = mortality
    self.mortality.starve = 0
    self.limit = limit

  def run(self, game):
    self.mortality.starve += 1
    if self.limit <= self.mortality.starve:
      self.mortality.die(game)