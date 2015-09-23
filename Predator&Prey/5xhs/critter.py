__author__ = 'hyunseok'

import random

class Critter(object):
    def __init__(self, world, num):
        self.count = 0
        self.num = num

        while True:
            self.x = random.randrange(0, world.mapsize)
            self.y = random.randrange(0, world.mapsize)
            if world.map[self.x][self.y] == '-':
                break

    def move(self, world):
        # 0:up  1:right  2:down  3:left

        is_empty = [True, True, True, True]

        if self.x - 1 < 0 or world.map[self.x-1][self.y] != '-':
            is_empty[3] = False

        if self.x + 1 >= world.mapsize or world.map[self.x+1][self.y] != '-':
            is_empty[1] = False

        if self.y - 1 < 0 or world.map[self.x][self.y-1] != '-' :
            is_empty[0] = False

        if self.y + 1 >= world.mapsize or world.map[self.x][self.y+1] != '-':
            is_empty[2] = False


        temp = random.randrange(0,4)

        if temp == 0 and is_empty[0] :
            self.y -= 1
            return
        elif temp == 1 and is_empty[1] :
            self.x += 1
            return
        elif temp == 2 and is_empty[2] :
            self.y += 1
            return
        elif temp == 3 and is_empty[3] :
            self.x -= 1
            return

        if is_empty[0] :
            self.y -= 1
            return
        elif is_empty[1] :
            self.x += 1
            return
        elif is_empty[2] :
            self.y += 1
            return
        elif is_empty[3] :
            self.x -= 1
            return

        pass

    def get_old(self):
        self.count += 1


class Rabbit(Critter):
    def is_too_old(self):
        if self.count > 3:
            self.count = 1
            too_old = True
            return True
        return False


class Fox(Critter):

    def is_too_old(self):
        if self.count > 8:
            self.count = 1
            return True
        return False

    def eat(self, simulator):
        if self.x+1 < simulator.world.mapsize and simulator.world.map[self.x + 1][self.y] == 'R':
            return [self.x+1, self.y]

        if self.y+1 < simulator.world.mapsize and simulator.world.map[self.x][self.y + 1] == 'R':
            return [self.x, self.y+1]

        if self.x - 1 > 0 and simulator.world.map[self.x - 1][self.y] == 'R':
            return [self.x-1, self.y]

        if self.y - 1 > 0 and simulator.world.map[self.x][self.y - 1] == 'R':
            return [self.x, self.y-1]

        return [-1, -1]