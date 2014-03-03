# coding: utf-8

import pygame
import random
from pygame.locals import *

class Maze:
	# Maze: 
	# 0 - Blank
	# 1 - Wall
	# 2 - Dot (untraveled spot)
	# 3 - Ghost line
	# 4 - Tunnel (slowdown spot)
	# 5 - No-up spot
	# 6 - Large dot
	# 7 - Pac-Man Start
	# 9 - Outer wall
	
	__slots__ = ('maze', 'tiles')
	
	def __init__(self, filename):
		self.maze = []
		self.loadMaze(filename)
		self.tiles = self.loadTiles()
		
	def loadTiles(self):
		someTiles = []
		someTiles.append(pygame.image.load("./data/tiles/null.png").convert_alpha())      # 0
		someTiles.append(pygame.image.load("./data/tiles/blue.png").convert_alpha())      # 1
		someTiles.append(pygame.image.load("./data/tiles/cdl.png").convert_alpha())       # 2
		someTiles.append(pygame.image.load("./data/tiles/cdr.png").convert_alpha())       # 3
		someTiles.append(pygame.image.load("./data/tiles/cul.png").convert_alpha())       # 4
		someTiles.append(pygame.image.load("./data/tiles/cur.png").convert_alpha())       # 5
		someTiles.append(pygame.image.load("./data/tiles/u.png").convert_alpha())         # 6
		someTiles.append(pygame.image.load("./data/tiles/ur.png").convert_alpha())        # 7
		someTiles.append(pygame.image.load("./data/tiles/r.png").convert_alpha())         # 8
		someTiles.append(pygame.image.load("./data/tiles/dr.png").convert_alpha())        # 9
		someTiles.append(pygame.image.load("./data/tiles/d.png").convert_alpha())         # 10
		someTiles.append(pygame.image.load("./data/tiles/dl.png").convert_alpha())        # 11
		someTiles.append(pygame.image.load("./data/tiles/l.png").convert_alpha())         # 12
		someTiles.append(pygame.image.load("./data/tiles/ul.png").convert_alpha())        # 13
		someTiles.append(pygame.image.load("./data/tiles/dot.png").convert_alpha())       # 14
		someTiles.append(pygame.image.load("./data/tiles/bigdot.png").convert_alpha())    # 15
		someTiles.append(pygame.image.load("./data/tiles/line.png").convert_alpha())      # 16
		return someTiles
	
	def loadMaze(self, filename):
		file = open(filename)
		for line in file:	
			self.maze.append(line);
			
	def getTile(self, tile):
		return self.tiles[tile]
			
	def getMazeContents(self, atX, atY):
		try:
			return int(self.maze[atY][atX])
		except:
			return 0
		
	def countNumDots(self):
		indexx = 0
		indexy = 0
		total = 0
		while (indexy < len(self.maze)):
			while (indexx < 30):
				if (int(self.maze[indexy][indexx]) == 2):
					total = total + 1
				indexx += 1
			indexx = 0
			indexy += 1
		return total
		
	def renderMaze(self):
		for line in self.maze:
			outstring = ""
			for cell in line:
				if ( cell == "1"):
					outstring = outstring + "Û" # Wall
				elif ( cell == "2" ):
					outstring = outstring + "ù"
				elif ( cell == "0" ):
					outstring = outstring + " "
				elif ( cell == "6" ):
					outstring = outstring + "O"
				elif ( cell == "4" ):
					outstring = outstring + " "
				elif ( cell == "3" ):
					outstring = outstring + "-"
				elif ( cell == "7" ):
					outstring = outstring + ">"
				elif ( cell == "8" ):
					outstring = outstring + "]"
				elif ( cell == "9" ):
					outstring = outstring + "±"
			print outstring
	
	def eatDot(self, atX, atY):
		if (self.maze.getMazeContents(atX, atY) == "2"):
			self.maze[atY][atX] = "0"
	
