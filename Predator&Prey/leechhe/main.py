from manager import GameManager

if __name__ == "__main__" :
	manager = GameManager()
	while True:
		manager.showTimeStep()
		manager.drawWorld()
		input("Press Enter to proceed.")
		if manager.gameOver() : break;
		manager.move()
		manager.increaseTime()


	#draw world

	#keyborad input
	#Loop move

	#time increase