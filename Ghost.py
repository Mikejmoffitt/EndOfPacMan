#Jeff Haak
import pygame
from pygame.locals import *
import Maze
import math
import random

class Ghost:
	# type determines pathfinding junk
	#   Red =	   0
	#   Pink =	  1
	#   Cyan =	  2
	#   Orange =	3
	#
	# Status = (-1 to > 0)
	#
	# direction = Which way ghost is faceing
	#   up -	0
	#   down -  1
	#   left -  2
	#   right - 3
	__slots__ = ('xPos', 'yPos', 'type', 'status', 'dir', 'xTar', 'yTar', 'frames', 'animOsc', 'active', 'movePoint')
	
	def __init__(self, xPos, yPos, ghostType):
		MAXMAZE = 30
		FLASHTIME = 32
		self.xPos = xPos
		self.yPos = yPos
		self.movePoint = 0
		self.type = int(ghostType)
		self.dir = 1
		self.active = False
		self.status = 0
		self.animOsc = 0
		self.frames = self.loadFrames()
		
		if ghostType == 0:
			self.xTar = 30
			self.yTar = 0
		else:
			self.xTar = (112//8)
			self.yTar = (142//8)-2
	
	def loadFrames(self):
		returnMe = []
		#if (self.type == 0):
		#	index = 0
		#	while (index < 8):			
		#		if (index < 10):
		#			returnMe.append(pygame.image.load("./data/sprites/red0" + str(index) + ".png").convert_alpha())
		#		else:
		#			returnMe.append(pygame.image.load("./data/sprites/red" + str(index) + ".png").convert_alpha())
		#		index = index + 1
		if (self.type == 0):
			returnMe.append(pygame.image.load("./data/sprites/red00.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/red01.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/red02.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/red03.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/red04.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/red05.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/red06.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/red07.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/blue00.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/blue01.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/white00.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/white01.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/redflag.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/eyesup.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/eyesdown.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/eyesleft.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/eyesright.png").convert_alpha())
		if (self.type == 1):
			returnMe.append(pygame.image.load("./data/sprites/pink00.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/pink01.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/pink02.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/pink03.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/pink04.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/pink05.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/pink06.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/pink07.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/blue00.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/blue01.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/white00.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/white01.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/pinkflag.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/eyesup.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/eyesdown.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/eyesleft.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/eyesright.png").convert_alpha())
		if (self.type == 2):
			returnMe.append(pygame.image.load("./data/sprites/cyan00.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/cyan01.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/cyan02.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/cyan03.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/cyan04.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/cyan05.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/cyan06.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/cyan07.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/blue00.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/blue01.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/white00.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/white01.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/cyanflag.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/eyesup.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/eyesdown.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/eyesleft.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/eyesright.png").convert_alpha())
		if (self.type == 3):
			returnMe.append(pygame.image.load("./data/sprites/orange00.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/orange01.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/orange02.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/orange03.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/orange04.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/orange05.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/orange06.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/orange07.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/blue00.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/blue01.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/white00.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/white01.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/orangeflag.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/eyesup.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/eyesdown.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/eyesleft.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/eyesright.png").convert_alpha())
		if (self.type == 4):
			returnMe.append(pygame.image.load("./data/sprites/pacman00.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/pacman01.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/pacman02.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/pacman04.png").convert_alpha())
			returnMe.append(pygame.image.load("./data/sprites/pacman03.png").convert_alpha())
		return returnMe
					
					
	def getFlagFrame(self):
		return self.frames[12]
					
	def getFrame(self):
		if (self.type < 4):
			if (self.status < 0):
				if (self.dir == 0):
					return self.frames[13]
				elif (self.dir == 1):
					return self.frames[14]
				elif (self.dir == 2):
					return self.frames[15]
				else:
					return self.frames[16]
			if (self.status == 0):
				if (self.animOsc < 5):
					if (self.dir == 0):
						return self.frames[2]
					elif (self.dir == 1):
						return self.frames[6]
					elif (self.dir == 2):
						return self.frames[4]
					else:
						return self.frames[0]
				else:
					if (self.dir == 0):
						return self.frames[3]
					elif (self.dir == 1):
						return self.frames[7]
					elif (self.dir == 2):
						return self.frames[5]
					else:
						return self.frames[1]
			elif (self.status > 0):
				if (self.animOsc < 5):
					if (self.status > 32):
						return self.frames[8]
					else:
						return self.frames[10]
				else:
					if (self.status > 32):
						return self.frames[9]
					else:
						return self.frames[11]
		else:
			if (self.animOsc < 5):
				return self.frames[0]
			else:
				if (self.dir == 0):
					return self.frames[4]
				if (self.dir == 1):
					return self.frames[3]
				if (self.dir == 2):
					return self.frames[2]
				if (self.dir == 3):
					return self.frames[1]

	def euclidDist(self, x1, y1, x2, y2):
		dist = math.sqrt( pow((x1 - x2), 2) + pow((y1 - y2), 2) ) 
		return dist
	
	def report(self):
		print "Dir: " + str(self.dir)
		print "     X: " + str(self.xPos)
		print "     Y: " + str(self.yPos)
		print "    Xt: " + str(self.xPos // 8)
		print "    Yt: " + str(self.yPos // 8)
		print "  Xtar: " + str(self.xTar)
		print "  Ytar: " + str(self.yTar)
	
	def move(self, theMaze):
		# go back to base if necessary
		if (self.status == -1):
			self.xTar = (112//8)
			self.yTar = (142//8)-2
	
		if (self.xPos // 8 == (112//8)):
			if (self.yPos // 8 == (142//8)-2):
				self.status = 0
	
		if (self.movePoint > 0):
			self.movePoint -= 1
		if (self.active == False):
			self.xTar = 112//8
			self.yTar = 142//8
		self.animOsc = self.animOsc + 1
		if (self.animOsc > 10):
			self.animOsc = 0
		if (self.xPos < 0):
			self.xPos = 224
		if (self.xPos > 224):
			self.xPos = 0
			
		# Check for touching waypoint


		if (self.xPos // 8 == self.xTar):
			if (self.yPos // 8 == self.yTar):
				self.movePoint = 0
		
				
		# Checks for all possible directions
		if (self.yPos%8 == 0 and self.xPos%8 == 0):
			possibleDirs = []
			if (self.dir == 0):
				if (theMaze.getMazeContents((self.xPos)//8, (self.yPos-1)//8) != 1):
					possibleDirs.append(0)
				if (theMaze.getMazeContents((self.xPos-1)//8, (self.yPos)//8) != 1):
					possibleDirs.append(2)
				if (theMaze.getMazeContents((self.xPos+8)//8, (self.yPos)//8) != 1):
					possibleDirs.append(3)
			if (self.dir == 1 and self.status != -1):
				if (theMaze.getMazeContents((self.xPos)//8, (self.yPos+8)//8) != 1 and theMaze.getMazeContents((self.xPos)//8, (self.yPos+8)//8) != 3):
					possibleDirs.append(1)
				if (theMaze.getMazeContents((self.xPos-1)//8, (self.yPos)//8) != 1):
					possibleDirs.append(2)
				if (theMaze.getMazeContents((self.xPos+8)//8, (self.yPos)//8) != 1):
					possibleDirs.append(3)
			if (self.dir == 2 and self.status != -1):
				if (theMaze.getMazeContents((self.xPos)//8, (self.yPos-1)//8) != 1):
					possibleDirs.append(0)
				if (theMaze.getMazeContents((self.xPos)//8, (self.yPos+8)//8) != 1 and theMaze.getMazeContents((self.xPos)//8, (self.yPos+8)//8) != 3):
					possibleDirs.append(1)
				if (theMaze.getMazeContents((self.xPos-1)//8, (self.yPos)//8) != 1):
					possibleDirs.append(2)
			if (self.dir == 3 and self.status != -1):
				if (theMaze.getMazeContents((self.xPos)//8, (self.yPos-1)//8) != 1):
					possibleDirs.append(0)
				if (theMaze.getMazeContents((self.xPos)//8, (self.yPos+8)//8) != 1 and theMaze.getMazeContents((self.xPos)//8, (self.yPos+8)//8) != 3):
					possibleDirs.append(1)
				if (theMaze.getMazeContents((self.xPos+8)//8, (self.yPos)//8) != 1):
					possibleDirs.append(3)
			if (self.dir == 1 and self.status == -1):
				if (theMaze.getMazeContents((self.xPos)//8, (self.yPos+8)//8) != 1):
					possibleDirs.append(1)
				if (theMaze.getMazeContents((self.xPos-1)//8, (self.yPos)//8) != 1):
					possibleDirs.append(2)
				if (theMaze.getMazeContents((self.xPos+8)//8, (self.yPos)//8) != 1):
					possibleDirs.append(3)
			if (self.dir == 2 and self.status == -1):
				if (theMaze.getMazeContents((self.xPos)//8, (self.yPos-1)//8) != 1):
					possibleDirs.append(0)
				if (theMaze.getMazeContents((self.xPos)//8, (self.yPos+8)//8) != 1):
					possibleDirs.append(1)
				if (theMaze.getMazeContents((self.xPos-1)//8, (self.yPos)//8) != 1):
					possibleDirs.append(2)
			if (self.dir == 3 and self.status == -1):
				if (theMaze.getMazeContents((self.xPos)//8, (self.yPos-1)//8) != 1):
					possibleDirs.append(0)
				if (theMaze.getMazeContents((self.xPos)//8, (self.yPos+8)//8) != 1):
					possibleDirs.append(1)
				if (theMaze.getMazeContents((self.xPos+8)//8, (self.yPos)//8) != 1):
					possibleDirs.append(3)
					
			#print possibleDirs
			dists = []
			index = 0
			while (index < len(possibleDirs)):
				if (possibleDirs[index] == 0):
					dists.append(self.euclidDist(((self.xPos)//8), ((self.yPos-1) // 8),self.xTar,self.yTar))
				elif (possibleDirs[index] == 1):
					dists.append(self.euclidDist(((self.xPos)//8), ((self.yPos+8) // 8),self.xTar,self.yTar))
				elif (possibleDirs[index] == 2):
					dists.append(self.euclidDist(((self.xPos-1)//8), ((self.yPos) // 8),self.xTar,self.yTar))
				elif (possibleDirs[index] == 3):
					dists.append(self.euclidDist(((self.xPos+8)//8), ((self.yPos) // 8),self.xTar,self.yTar))
				index = index + 1
			lowest = 1337
			lowestIndex = -1
			index = 0
			if (self.type != 4):
				while (index < len(dists)):
					if (self.status <= 0):
						if (dists[index] <= lowest ):
							lowestIndex = index
							lowest = dists[index]
					else:
						if (dists[index] >= lowest ):
							lowestIndex = index
							lowest = dists[index]
						
					index = index + 1
				self.dir = possibleDirs[lowestIndex]
			else:
				choice = random.randint(0,len(possibleDirs)-1)
				while (choice > len(possibleDirs)):
					choice -= 1
				self.dir = possibleDirs[choice]
			
		# Handles movement
		if (self.dir == 0): # up
			if (theMaze.getMazeContents((self.xPos)//8, (self.yPos-1)//8) != 1):
				self.yPos = self.yPos - 1
		elif (self.dir == 1): # down
			if (theMaze.getMazeContents((self.xPos)//8, (self.yPos+8)//8) != 1):
				self.yPos = self.yPos + 1
		elif (self.dir == 2): # left
			if (theMaze.getMazeContents((self.xPos-1)//8, (self.yPos)//8) != 1):
				self.xPos = self.xPos - 1
		elif (self.dir == 3): # right
			if (theMaze.getMazeContents((self.xPos+8)//8, (self.yPos)//8) != 1):
				self.xPos = self.xPos + 1

		if self.status > 0:
			self.status -= 1
	def doPacIntel(self, otherGhosts):
		#self.xTar = otherGhosts[0].xPos // 8
		#self.yTar = otherGhosts[0].yPos // 8
		pass
			
	def getxTile(self):
		return self.xPos//8

	def getyTile(self):
		return self.yPos//8
		
	def getX(self):
		return self.xPos

	def getY(self):
		return self.yPos

	def getTile(self):
		return (getxTile, getyTile)

	def decStatus(self):
		self.status -= 1

	def increaseStatue(self, amount):
		self.status += amount
		
	def setTarget(self, xCoor, yCoor):
		self.xTar = xCoor
		self.yTar = yCoor