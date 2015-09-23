__author__ = 'hyunseok'


from simulator import Simulator

def main():
    # Simulator(# of rabbits, # of foxes, size of world)
    simulator = Simulator(30, 10, 20)

    while (True):
        simulator.print()

        simulator.move()
        simulator.reset()

        simulator.eat()
        simulator.reset()

        simulator.getold()
        simulator.reset()

        simulator.starve()
        simulator.reset()


        input("Enter: ")


main()
