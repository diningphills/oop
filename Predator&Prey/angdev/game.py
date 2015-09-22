from rabbit import Rabbit
from fox import Fox

class Game:
  def __init__(self, world_map, rabbits, foxes):
    self.world_map = world_map

    self.objects = []
    for i in range(rabbits):
      self.objects.append(Rabbit())

    for i in range(foxes):
      self.objects.append(Fox())

    for obj in self.objects:
      self.world_map.set_randomly(obj)

  def run(self):
    time = 0

    while True:
      time += 1
      print(time)

      foxes = list(filter(lambda x: isinstance(x, Fox), self.objects))
      rabbits = list(filter(lambda x: isinstance(x, Rabbit), self.objects))

      for i in range(len(foxes)):
        foxes[i].update(self)
      for i in range(len(rabbits)):
        rabbits[i].update(self)

      self.remove_died()

      self.world_map.inspect()
      input()

  def remove_died(self):
    targets = list(filter(lambda x: x.dead, self.objects))
    for target in targets:
      self.request_remove(target)

  def request_add(self, object):
    self.objects.append(object)

  def request_remove(self, object):
    self.objects.remove(object)