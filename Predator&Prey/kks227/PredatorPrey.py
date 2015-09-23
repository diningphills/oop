from constant import *
from rabbit import *
from fox import *
import random
import sys
import os			# to use os.system()



def invalid(x, y):
	return (x<0 or x>=SIZE or y<0 or y>=SIZE)



# OS system check
clearCommand = "clear"
from sys import platform as _platform
if _platform == "win32":
	# Windows...
	clearCommand = "cls"

# input the number of each animals
# os.system(clearCommand)
rNum = int(input("Enter initial number of rabbits: "))
fNum = int(input("Enter initial number of foxes: "))

# exception: too many animals or negative numbers!
if rNum+fNum > SIZE*SIZE or rNum < 0 or fNum < 0:
	print("invalid input!")
	sys.exit()



# initialization
map = []
for i in range(0, SIZE):
	inner = []
	for j in range (0, SIZE):
		inner.append(NOT)
	map.append(inner)

rabbits = []
foxes = []
emptyPos = list(range(0, SIZE*SIZE))
for cnt in range(rNum+fNum):
	target = random.randrange(len(emptyPos))
	ty = int(emptyPos[target]/SIZE)
	tx = emptyPos[target]%SIZE
	if cnt < rNum:
		map[ty][tx] = RAB
		newRabbit = Rabbit(tx, ty)
		rabbits.append(newRabbit)
	else:
		map[ty][tx] = FOX
		newFox = Fox(tx, ty)
		foxes.append(newFox)
	emptyPos.pop(target)

step = 1
while True:
	# print
	print("Time_step: " + str(step) + '\n')
	step += 1
	for i in range(SIZE):
		for j in range(SIZE):
			sys.stdout.write(CH[map[i][j]])
		print()
	print("\nPress Enter to proceed.")

	# hunt, move, starve, breed
	# hunt
	for f in foxes:
		target = []
		for k in range(4):
			xNext = f.x + XOFF[k]
			yNext = f.y + YOFF[k]
			if invalid(xNext, yNext):
				continue
			if map[yNext][xNext] == RAB:
				target.append(k)

		if len(target) == 0:		# no adjacent rabbits
			continue

		dir = target[random.randrange(len(target))]
		xNext = f.x + XOFF[dir]
		yNext = f.y + YOFF[dir]
		prey = 0
		for prey in range(len(rabbits)):
			if rabbits[prey].x == xNext and rabbits[prey].y == yNext:
				break
		map[f.y][f.x] = NOT
		map[yNext][xNext] = FOX
		f.hunt(dir)
		rabbits.pop(prey)

	# move
	for r in rabbits:
		dir = random.randrange(4)
		xNext = r.x + XOFF[dir]
		yNext = r.y + YOFF[dir]
		if not invalid(xNext, yNext) and map[yNext][xNext] == NOT:
			map[r.y][r.x] = NOT
			map[yNext][xNext] = RAB
			r.move(dir)

	for f in foxes:
		dir = random.randrange(4)
		xNext = f.x + XOFF[dir]
		yNext = f.y + YOFF[dir]
		if not invalid(xNext, yNext) and map[yNext][xNext] == NOT:
			xPrev = f.x
			yPrev = f.y
			if f.move(dir):
				map[yPrev][xPrev] = NOT
				map[f.y][f.x] = FOX

	# starve
	loops = len(foxes)
	i = 0
	while i < loops:
		if foxes[i].isTimeToStarve():
			map[foxes[i].y][foxes[i].x] = NOT
			foxes.pop(i)
			loops -= 1
		else:
			i += 1

	# breed
	cnt = len(rabbits)
	for r in rabbits:
		if r.isTimeToBreed():
			target = []
			for k in range(4):
				xNext = r.x + XOFF[k]
				yNext = r.y + YOFF[k]
				if not invalid(xNext, yNext) and map[yNext][xNext] == NOT:
					target.append(k)

			if len(target) == 0:		# no adjacent rabbits
				continue

			dir = target[random.randrange(len(target))]
			xNext = r.x + XOFF[dir]
			yNext = r.y + YOFF[dir]
			map[yNext][xNext] = RAB
			newRabbit = Rabbit(xNext, yNext)
			rabbits.append(newRabbit)
		cnt -= 1
		if cnt == 0:		# new hatches have no acts
			break

	cnt = len(foxes)
	for f in foxes:
		if f.isTimeToBreed():
			target = []
			for k in range(4):
				xNext = f.x + XOFF[k]
				yNext = f.y + YOFF[k]
				if not invalid(xNext, yNext) and map[yNext][xNext] == NOT:
					target.append(k)

			if len(target) == 0:		# no adjacent rabbits
				continue

			dir = target[random.randrange(len(target))]
			xNext = f.x + XOFF[dir]
			yNext = f.y + YOFF[dir]
			map[yNext][xNext] = FOX
			newFox = Fox(xNext, yNext)
			foxes.append(newFox)
		cnt -= 1
		if cnt == 0:		# new hatches have no acts
			break
			
			


	# next step
	input()