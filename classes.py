
#level creation

import pygame  # needed ?

from pygame.locals import *

from constants import *



class level:
	"""designing the maze"""
	def __init__(self,file):
		self.file = "map.txt"
		self.structure = 0

		def generate(self):
			with open(self.file, "r") as file:  #read only on the map.txt file
				level_structure = []            #creating the level design as an empty list


				for line in file:
					line_level = []

					#adding sprites in lines list, then lines in structure list
					for sprite in line:
						if sprite != "\n" : #eliminating line return
							line_level.append(sprite)
					level_structure.append(line_level)
				self.structure = level_structure

		def display(self,window):
			wall = pygame.image.load('images/wall.png').convert()
			finish = pygame.image.load('images/finish.png').convert_alpha()

			num_line=0
			for line in self.structure:
				x = num_case * SPRITE_SIZE    #sprites localisation
				y = num_line * SPRITE_SIZE
				if sprite == 'w':             # W = wall in map.txt
					window.blit(wall, (x,y))
				elif sprite == 'f':
					window.blit(finish, (x,y))
				num_case = num_case +1

			num_line = num_line +1
