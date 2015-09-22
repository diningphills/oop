from world import World

numberOfRabbit = raw_input("Number of rabbit: ")
numberOfFox = raw_input("Number of fox: ")

world = World(int(numberOfRabbit), int(numberOfFox))

while True:
	world.timeStep()
	world.printWorld()
	
	put = None

	while put != '' and put != "exit":
		put = raw_input("Please Enter: ")
	if put == "exit": break
