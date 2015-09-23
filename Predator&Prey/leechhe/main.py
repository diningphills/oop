from manager import GameManager

if __name__ == "__main__" :
	manager = GameManager()
	while not manager.gameOver():
		manager.showTimeStep()
		manager.drawWorld()
		input("Press Enter to proceed.")
		manager.move()
		manager.increaseTime()

	#draw world

	#keyborad input
	#Loop move

	#time increase