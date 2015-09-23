__author__ = 'hyunseok'

from world import World
from critter import Rabbit, Fox

class Simulator(object):
    def __init__(self, rabbit_num, fox_num, world_size):
        self.rabbit_list = []
        self.fox_list = []
        self.world = World(world_size)

        for i in range(1, rabbit_num):
            self.rabbit_list.append(Rabbit(self.world, i))

        for r in self.rabbit_list:
            self.world.marking_rabbit(r)

        for i in range(1, fox_num):
            self.fox_list.append(Fox(self.world, i))

        for f in self.fox_list:
            self.world.marking_fox(f)

        pass



    def print(self):
        self.world.print()
        pass

    def reset(self):
        self.world.reset()
        for r in self.rabbit_list:
            self.world.marking_rabbit(r)
        for f in self.fox_list:
            self.world.marking_fox(f)

    def move(self):
        for r in self.rabbit_list:
            r.move(self.world)

        for f in self.fox_list:
            f.move(self.world)



    def eat(self):
        rabbit_die = []
        for f in self.fox_list:
            temp = f.eat(self)
            if temp[0] != -1 and temp[1] != -1 :
                for r in self.rabbit_list:
                    if temp[0] == r.x and temp[1] == r.y:
                        rabbit_die.append(r)

        for dr in rabbit_die:
            self.rabbit_list.remove(dr)




    def starve(self):
        fox_starve = []
        for f in self.fox_list:
            if f.is_too_old():
                fox_starve.append(f)

        for sf in fox_starve:
            self.fox_list.remove(sf)


    def getold(self):
        for f in self.fox_list:
            f.get_old()
            print(f.count)