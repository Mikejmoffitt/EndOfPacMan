import pygame
import random
from pygame.locals import *
import Maze
import Ghost

# If we were to do this again, we'd render everything unscaled to a main buffer
# then scale that to fit the size of the display. 

def main():

	pygame.mixer.pre_init(44100,-16,2,2048)
	pygame.init()
	pygame.mixer.init()

	FRAMERATE = 60
	SCALEVALUE = 3
	
	GHOSTBLUEMAX = 270
	
	fDiv = 1
	
	MAZEWIDTH = (224+16) // 8
	MAZEHEIGHT = (248+8) // 8
	MAZEOFFSET = 16 * SCALEVALUE

	scrwidth = 224 * SCALEVALUE
	scrheight = 288 * SCALEVALUE
	
	bigDot = 0
	avoidGhost = 0

	size=[scrwidth, scrheight]
	pygame.display.set_mode(size, pygame.DOUBLEBUF)
	pygame.display.set_caption("The End of Pac-Man")
	screen=pygame.display.set_mode(size, pygame.DOUBLEBUF)
	clock=pygame.time.Clock()
	
	keys = []
	keysheld = []
	index = 0
	
	ghosts = []
	
	
	while index < 64:
		keys.append(0)
		keysheld.append(0)
		keys[index] = False
		keysheld[index] = 0
		index = index + 1
		
	def blitMaze(theMaze):
		indexx = 0
		indexy = 0
		screen.blit(pygame.transform.scale(theMaze.getTile(0), (224 * SCALEVALUE, 288 * SCALEVALUE)), (0,0))
		while (indexy < MAZEHEIGHT):
			while (indexx < MAZEWIDTH):
				if (theMaze.getMazeContents(indexx,indexy) == 4):
					screen.blit(pygame.transform.scale(theMaze.getTile(0), (8 * SCALEVALUE, 8 * SCALEVALUE)), ((indexx*8) * SCALEVALUE, ((indexy*8) * SCALEVALUE)+MAZEOFFSET))
				if (theMaze.getMazeContents(indexx,indexy) == 0):
					screen.blit(pygame.transform.scale(theMaze.getTile(0), (8 * SCALEVALUE, 8 * SCALEVALUE)), ((indexx*8) * SCALEVALUE, ((indexy*8) * SCALEVALUE)+MAZEOFFSET))
				if (theMaze.getMazeContents(indexx,indexy) == 1):
					# UP
					if (theMaze.getMazeContents(indexx,indexy-1) != 1):
						if (theMaze.getMazeContents(indexx,indexy+1) == 1):
							if (theMaze.getMazeContents(indexx-1,indexy) == 1):
								if (theMaze.getMazeContents(indexx+1,indexy) == 1):
									screen.blit(pygame.transform.scale(theMaze.getTile(6), (8 * SCALEVALUE, 8 * SCALEVALUE)), (((indexx*8) * SCALEVALUE)-(8*SCALEVALUE), ((indexy*8) * SCALEVALUE)+MAZEOFFSET))		
					# UP-RIGHT
					if (theMaze.getMazeContents(indexx,indexy-1) != 1):
						if (theMaze.getMazeContents(indexx,indexy+1) == 1):
							if (theMaze.getMazeContents(indexx-1,indexy) == 1):
								if (theMaze.getMazeContents(indexx+1,indexy) != 1):
									screen.blit(pygame.transform.scale(theMaze.getTile(7), (8 * SCALEVALUE, 8 * SCALEVALUE)), (((indexx*8) * SCALEVALUE)-(8*SCALEVALUE), ((indexy*8) * SCALEVALUE)+MAZEOFFSET))
					# DOWN
					if (theMaze.getMazeContents(indexx,indexy-1) == 1):
						if (theMaze.getMazeContents(indexx,indexy+1) != 1):
							if (theMaze.getMazeContents(indexx-1,indexy) == 1):
								if (theMaze.getMazeContents(indexx+1,indexy) == 1):
									screen.blit(pygame.transform.scale(theMaze.getTile(10), (8 * SCALEVALUE, 8 * SCALEVALUE)), (((indexx*8) * SCALEVALUE)-(8*SCALEVALUE), ((indexy*8) * SCALEVALUE)+MAZEOFFSET))
					# DOWN-RIGHT
					if (theMaze.getMazeContents(indexx,indexy-1) == 1):
						if (theMaze.getMazeContents(indexx,indexy+1) != 1):
							if (theMaze.getMazeContents(indexx-1,indexy) == 1):
								if (theMaze.getMazeContents(indexx+1,indexy) != 1):
									screen.blit(pygame.transform.scale(theMaze.getTile(9), (8 * SCALEVALUE, 8 * SCALEVALUE)), (((indexx*8) * SCALEVALUE)-(8*SCALEVALUE), ((indexy*8) * SCALEVALUE)+MAZEOFFSET))
					# LEFT
					if (theMaze.getMazeContents(indexx,indexy-1) == 1):
						if (theMaze.getMazeContents(indexx,indexy+1) == 1):
							if (theMaze.getMazeContents(indexx-1,indexy) != 1):
								if (theMaze.getMazeContents(indexx+1,indexy) == 1):
									screen.blit(pygame.transform.scale(theMaze.getTile(12), (8 * SCALEVALUE, 8 * SCALEVALUE)), (((indexx*8) * SCALEVALUE)-(8*SCALEVALUE), ((indexy*8) * SCALEVALUE)+MAZEOFFSET))
					# UP-LEFT
					if (theMaze.getMazeContents(indexx,indexy-1) != 1):
						if (theMaze.getMazeContents(indexx,indexy+1) == 1):
							if (theMaze.getMazeContents(indexx-1,indexy) != 1):
								if (theMaze.getMazeContents(indexx+1,indexy) == 1):
									screen.blit(pygame.transform.scale(theMaze.getTile(13), (8 * SCALEVALUE, 8 * SCALEVALUE)), (((indexx*8) * SCALEVALUE)-(8*SCALEVALUE), ((indexy*8) * SCALEVALUE)+MAZEOFFSET))
					# RIGHT
					if (theMaze.getMazeContents(indexx,indexy-1) == 1):
						if (theMaze.getMazeContents(indexx,indexy+1) == 1):
							if (theMaze.getMazeContents(indexx-1,indexy) == 1):
								if (theMaze.getMazeContents(indexx+1,indexy) != 1):
									screen.blit(pygame.transform.scale(theMaze.getTile(8), (8 * SCALEVALUE, 8 * SCALEVALUE)), (((indexx*8) * SCALEVALUE)-(8*SCALEVALUE), ((indexy*8) * SCALEVALUE)+MAZEOFFSET))
					# DOWN-LEFT
					if (theMaze.getMazeContents(indexx,indexy-1) == 1):
						if (theMaze.getMazeContents(indexx,indexy+1) != 1):
							if (theMaze.getMazeContents(indexx-1,indexy) != 1):
								if (theMaze.getMazeContents(indexx+1,indexy) == 1):
									screen.blit(pygame.transform.scale(theMaze.getTile(11), (8 * SCALEVALUE, 8 * SCALEVALUE)), (((indexx*8) * SCALEVALUE)-(8*SCALEVALUE), ((indexy*8) * SCALEVALUE)+MAZEOFFSET))
					# DOWN-LEFT
					if (theMaze.getMazeContents(indexx,indexy-1) == 1):
						if (theMaze.getMazeContents(indexx,indexy+1) != 1):
							if (theMaze.getMazeContents(indexx-1,indexy) != 1):
								if (theMaze.getMazeContents(indexx+1,indexy) == 1):
									screen.blit(pygame.transform.scale(theMaze.getTile(11), (8 * SCALEVALUE, 8 * SCALEVALUE)), (((indexx*8) * SCALEVALUE)-(8*SCALEVALUE), ((indexy*8) * SCALEVALUE)+MAZEOFFSET))
					# SUR1
					if (theMaze.getMazeContents(indexx,indexy-1) == 1):
						if (theMaze.getMazeContents(indexx,indexy+1) == 1):
							if (theMaze.getMazeContents(indexx-1,indexy) == 1):
								if (theMaze.getMazeContents(indexx+1,indexy) == 1):
									if (theMaze.getMazeContents(indexx+1,indexy-1) != 1):
										screen.blit(pygame.transform.scale(theMaze.getTile(5), (8 * SCALEVALUE, 8 * SCALEVALUE)), (((indexx*8) * SCALEVALUE)-(8*SCALEVALUE), ((indexy*8) * SCALEVALUE)+MAZEOFFSET))
					# SUR2
					if (theMaze.getMazeContents(indexx,indexy-1) == 1):
						if (theMaze.getMazeContents(indexx,indexy+1) == 1):
							if (theMaze.getMazeContents(indexx-1,indexy) == 1):
								if (theMaze.getMazeContents(indexx+1,indexy) == 1):
									if (theMaze.getMazeContents(indexx+1,indexy+1) != 1):
										screen.blit(pygame.transform.scale(theMaze.getTile(3), (8 * SCALEVALUE, 8 * SCALEVALUE)), (((indexx*8) * SCALEVALUE)-(8*SCALEVALUE), ((indexy*8) * SCALEVALUE)+MAZEOFFSET))
					# SUR3
					if (theMaze.getMazeContents(indexx,indexy-1) == 1):
						if (theMaze.getMazeContents(indexx,indexy+1) == 1):
							if (theMaze.getMazeContents(indexx-1,indexy) == 1):
								if (theMaze.getMazeContents(indexx+1,indexy) == 1):
									if (theMaze.getMazeContents(indexx-1,indexy+1) != 1):
										screen.blit(pygame.transform.scale(theMaze.getTile(2), (8 * SCALEVALUE, 8 * SCALEVALUE)), (((indexx*8) * SCALEVALUE)-(8*SCALEVALUE), ((indexy*8) * SCALEVALUE)+MAZEOFFSET))
					# SUR4
					if (theMaze.getMazeContents(indexx,indexy-1) == 1):
						if (theMaze.getMazeContents(indexx,indexy+1) == 1):
							if (theMaze.getMazeContents(indexx-1,indexy) == 1):
								if (theMaze.getMazeContents(indexx+1,indexy) == 1):
									if (theMaze.getMazeContents(indexx-1,indexy-1) != 1):
										screen.blit(pygame.transform.scale(theMaze.getTile(4), (8 * SCALEVALUE, 8 * SCALEVALUE)), (((indexx*8) * SCALEVALUE)-(8*SCALEVALUE), ((indexy*8) * SCALEVALUE)+MAZEOFFSET))
								
				if (theMaze.getMazeContents(indexx,indexy) == 2):
					screen.blit(pygame.transform.scale(theMaze.getTile(14), (8 * SCALEVALUE, 8 * SCALEVALUE)), (((indexx*8) * SCALEVALUE)-(8*SCALEVALUE), ((indexy*8) * SCALEVALUE)+MAZEOFFSET))
				if (theMaze.getMazeContents(indexx,indexy) == 3):
					screen.blit(pygame.transform.scale(theMaze.getTile(16), (8 * SCALEVALUE, 8 * SCALEVALUE)), (((indexx*8) * SCALEVALUE)-(8*SCALEVALUE), ((indexy*8) * SCALEVALUE)+MAZEOFFSET))
				if (theMaze.getMazeContents(indexx,indexy) == 6):
					if (bigDot >= 0 and bigDot < 6):
						screen.blit(pygame.transform.scale(theMaze.getTile(15), (8 * SCALEVALUE, 8 * SCALEVALUE)), (((indexx*8) * SCALEVALUE)-(8*SCALEVALUE), ((indexy*8) * SCALEVALUE)+MAZEOFFSET))
					else:
						screen.blit(pygame.transform.scale(theMaze.getTile(0), (8 * SCALEVALUE, 8 * SCALEVALUE)), (((indexx*8) * SCALEVALUE)-(8*SCALEVALUE), ((indexy*8) * SCALEVALUE)+MAZEOFFSET))
				indexx = indexx + 1
			indexx = 0
			indexy = indexy + 1
	
	gameMaze = Maze.Maze("./maze.txt")
	ghosts.append(Ghost.Ghost(116,112-16,0))
	ghosts[0].active = True
	ghosts.append(Ghost.Ghost(112,112+8,1))
	ghosts.append(Ghost.Ghost(112-8,112+8,2))
	ghosts.append(Ghost.Ghost(112+8,112+8,3))
	ghosts.append(Ghost.Ghost(112+8,200-8,4))
	toggle = 0
	gameStatus = 0
	quit = False
	selected = 0
	ghostsBlue = 0
	eatSnd = 0
	sounds = []
	sounds.append(pygame.mixer.Sound("./data/sfx/munch A.wav"))
	sounds.append(pygame.mixer.Sound("./data/sfx/munch B.wav"))
	sounds.append(pygame.mixer.Sound("./data/sfx/ghost eat 7.wav"))
	sounds.append(pygame.mixer.Sound("./data/sfx/ghost eat 3.wav"))
	while (quit == False):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					toggle = toggle + 1
				if event.key == pygame.K_F4:
					quit = True
				if event.key == pygame.K_1:
					print "SELECTED RED"
					selected = 0
				if event.key == pygame.K_2:
					print "SELECTED PINK"
					selected = 1
				if event.key == pygame.K_3:
					print "SELECTED CYAN"
					selected = 2
				if event.key == pygame.K_4:
					print "SELECTED ORANGE"
					selected = 3
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				print str(event.pos[0] // SCALEVALUE) + "," + str(event.pos[1] // SCALEVALUE)
				ghosts[selected].movePoint = 384
				ghosts[selected].xTar = (event.pos[0] // SCALEVALUE) // 8
				ghosts[selected].yTar = ((event.pos[1] // SCALEVALUE) // 8)-2
		
		if (toggle > 1):
			toggle = 0
		index = 0
		# Does ghost movement, compensates for frameskip
		
		while (index < fDiv and gameStatus >= 150):
			
			bigDot = bigDot + 1
			if (bigDot > 12):
				bigDot = 0
			if (toggle < 1):
				ghosts[0].move(gameMaze)
				ghosts[1].move(gameMaze)
				ghosts[2].move(gameMaze)
				ghosts[3].move(gameMaze)
				ghosts[4].move(gameMaze)
			
			if (ghostsBlue == GHOSTBLUEMAX):
				pygame.mixer.music.load("./data/sfx/large pellet loop.wav")
				pygame.mixer.music.play(-1)
				ghosts[0].status = ghostsBlue
				ghosts[1].status = ghostsBlue
				ghosts[2].status = ghostsBlue
				ghosts[3].status = ghostsBlue
			if (ghostsBlue == 1 and gameMaze.countNumDots() > 160):
				pygame.mixer.music.load("./data/sfx/siren slow 3.wav")
				pygame.mixer.music.play(-1)
			elif (ghostsBlue == 1 and gameMaze.countNumDots() > 80):
				pygame.mixer.music.load("./data/sfx/siren medium 3.wav")
				pygame.mixer.music.play(-1)
				
			else:
				if (ghostsBlue == 1):
					pygame.mixer.music.load("./data/sfx/siren fast 2.wav")
					pygame.mixer.music.play(-1)
				
				
			if (ghostsBlue > 0):
				ghostsBlue = ghostsBlue - 1
				
		
			# Eats damn dots
			if (int(gameMaze.getMazeContents(ghosts[4].xPos // 8, ghosts[4].yPos // 8)) == 2):
				setStr = ""
				tempList = list(gameMaze.maze[ghosts[4].yPos // 8])
				tempList[(ghosts[4].xPos // 8)] = 0
				for elem in tempList:
					setStr = setStr + str(elem)
				gameMaze.maze[ghosts[4].yPos // 8] = setStr
				if (eatSnd == 0):
					sounds[0].play()
				else:
					sounds[1].play()
				eatSnd = eatSnd + 1
			
			if (eatSnd >= 2):
				eatSnd = 0
				
				
			if (int(gameMaze.getMazeContents(ghosts[4].xPos // 8, ghosts[4].yPos // 8)) == 6):
				setStr = ""
				tempList = list(gameMaze.maze[ghosts[4].yPos // 8])
				tempList[(ghosts[4].xPos // 8)] = 0
				for elem in tempList:
					setStr = setStr + str(elem)
				gameMaze.maze[ghosts[4].yPos // 8] = setStr
				ghostsBlue = GHOSTBLUEMAX
				if (eatSnd == 0):
					sounds[0].play()
				else:
					sounds[1].play()
				eatSnd = eatSnd + 1
			
			# Check for eating a ghost
			indo = 0
			while (indo < len(ghosts)-1):
				if (ghosts[indo].status > 0):
					if (ghosts[4].xPos // 8 == ghosts[indo].xPos // 8):
						if (ghosts[4].yPos // 8 == ghosts[indo].yPos // 8):
							ghosts[indo].status = -1
							sounds[2].play()
				elif (ghosts[indo].status == 0): 
					if (ghosts[4].xPos // 8 == ghosts[indo].xPos // 8):
						if (ghosts[4].yPos // 8 == ghosts[indo].yPos // 8):
							quit = True
							print "PAC-MAN IS DEAD, LONG LIVE SATAN"
							
					
				indo = indo + 1
			index += 1
			
			# Give pac-man a target
			#ghosts[4].doPacIntel(ghosts[:4])
			
		if (gameStatus == 0):
			pygame.mixer.music.load("./data/sfx/intro.wav")
			pygame.mixer.music.play(1)
			ghosts[0].dir = 2
		if (gameStatus == 150):
		
			pygame.mixer.music.load("./data/sfx/siren slow 3.wav")
			pygame.mixer.music.play(-1)
			
		if (gameStatus == 250):
			ghosts[1].active = True
			ghosts[1].yTar = (142//8) -6
			print "RELEASING PINK..."
		if (gameStatus == 400):
			ghosts[2].active = True
			ghosts[2].yTar = (142//8) -6
			print "RELEASING CYAN..."
		if (gameStatus == 550):
			ghosts[3].active = True
			ghosts[3].yTar = (142//8) -6
			print "RELEASING ORANGE..."
			
		avoidGhost = avoidGhost + 1
		if (avoidGhost > 240):
			avoidGhost = 0
			
		# Increments the game timer
		gameStatus = gameStatus + 1
		
		# Blits the maze and dots backdrop
		blitMaze(gameMaze)
		# Renders the ghosts to the screen
		index = 0
		#while (index < len(ghosts)):
			#print str(index) + ": " + str(ghosts[index].xTar) + "," + str(ghosts[index].yTar)
			#index = index + 1
		screen.blit(pygame.transform.scale(ghosts[0].getFrame(), (16 * SCALEVALUE, 16 * SCALEVALUE)), (SCALEVALUE*(ghosts[0].getX() - 12),MAZEOFFSET+(SCALEVALUE*(ghosts[0].getY()-4))))
		screen.blit(pygame.transform.scale(ghosts[1].getFrame(), (16 * SCALEVALUE, 16 * SCALEVALUE)), (SCALEVALUE*(ghosts[1].getX() - 12),MAZEOFFSET+(SCALEVALUE*(ghosts[1].getY()-4))))
		screen.blit(pygame.transform.scale(ghosts[2].getFrame(), (16 * SCALEVALUE, 16 * SCALEVALUE)), (SCALEVALUE*(ghosts[2].getX() - 12),MAZEOFFSET+(SCALEVALUE*(ghosts[2].getY()-4))))
		screen.blit(pygame.transform.scale(ghosts[3].getFrame(), (16 * SCALEVALUE, 16 * SCALEVALUE)), (SCALEVALUE*(ghosts[3].getX() - 12),MAZEOFFSET+(SCALEVALUE*(ghosts[3].getY()-4))))
		screen.blit(pygame.transform.scale(ghosts[4].getFrame(), (16 * SCALEVALUE, 16 * SCALEVALUE)), (SCALEVALUE*(ghosts[4].getX() - 12),MAZEOFFSET+(SCALEVALUE*(ghosts[4].getY()-4))))

		index = 0
		while (index < len(ghosts)-1):
			if (ghosts[index].movePoint <= 0):
				screen.blit(pygame.transform.scale(ghosts[index].getFlagFrame(), (8 * SCALEVALUE, 8 * SCALEVALUE)), (SCALEVALUE*(32 + (8 * index)),MAZEOFFSET+(SCALEVALUE*(260))))
			else:
				screen.blit(pygame.transform.scale(gameMaze.getTile(0), (8 * SCALEVALUE, 8 * SCALEVALUE)), (SCALEVALUE*(32 + (8 * index)),MAZEOFFSET+(SCALEVALUE*(260))))
			index = index + 1
		# blits waypoints
		if (ghosts[0].active):
			screen.blit(pygame.transform.scale(ghosts[0].getFlagFrame(), (8 * SCALEVALUE, 8 * SCALEVALUE)), (SCALEVALUE*(ghosts[0].xTar * 8),MAZEOFFSET+(SCALEVALUE*(ghosts[0].yTar * 8))))
		
		if (ghosts[1].active):
			screen.blit(pygame.transform.scale(ghosts[1].getFlagFrame(), (8 * SCALEVALUE, 8 * SCALEVALUE)), (SCALEVALUE*(ghosts[1].xTar * 8),MAZEOFFSET+(SCALEVALUE*(ghosts[1].yTar * 8))))
		
		if (ghosts[2].active):
			screen.blit(pygame.transform.scale(ghosts[2].getFlagFrame(), (8 * SCALEVALUE, 8 * SCALEVALUE)), (SCALEVALUE*(ghosts[2].xTar * 8),MAZEOFFSET+(SCALEVALUE*(ghosts[2].yTar * 8))))
		
		if (ghosts[3].active):
			screen.blit(pygame.transform.scale(ghosts[3].getFlagFrame(), (8 * SCALEVALUE, 8 * SCALEVALUE)), (SCALEVALUE*(ghosts[3].xTar * 8),MAZEOFFSET+(SCALEVALUE*(ghosts[3].yTar * 8))))

		index = 0
	#	while (index < len(ghosts)-1):
		#	if (ghosts[index].xPos // 8 == ghosts[4].yPos // 8):
		#		if (ghosts[index].yPos // 8 == ghosts[4].yPos // 8):
		#			print "PAC-MAN IS DEAD, LONG HAIL SATAN"
		#			quit = True
		#	index = index + 1
		# Limit to 60 frames per second
		clock.tick(FRAMERATE/fDiv)
		
		# Update the screen with our blits
		pygame.display.flip()

if __name__ == "__main__":
	main()