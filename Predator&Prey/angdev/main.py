from world_map import WorldMap
from game import Game

def main():
  world_map = WorldMap(20, 20)
  game = Game(world_map, 20, 20)
  game.run()

if __name__ == '__main__':
  main()