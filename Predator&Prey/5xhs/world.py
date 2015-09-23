__author__ = 'hyunseok'

class World(object):
    def __init__(self, size):
        self.mapsize = size
        self.map = [[0 for x in range(self.mapsize)] for x in range(self.mapsize)]
        for i in range(0, self.mapsize):
            for j in range(0, self.mapsize):
                self.map[i][j] = '-'

    def print(self):
        for i in range(0, self.mapsize):
            for j in range(0, self.mapsize):
                print(self.map[i][j] + "\t", end="")
            print("")
        print("")

    def marking_rabbit(self, rabbit):
        self.map[rabbit.x][rabbit.y] = 'R'

    def marking_fox(self, fox):
        self.map[fox.x][fox.y] = 'F'

    def reset(self):
        for i in range(0, self.mapsize):
            for j in range(0, self.mapsize):
                self.map[i][j] = '-'
