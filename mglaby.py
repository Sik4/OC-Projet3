"""
Labyrinthe Game : Help Mac Gyver to escape the maze.
Find the Needle, the Tube and the Ether to neutralize the Guard.
ARROWS to move
Files : mglaby.py, classes.py, constants.py, map.txt, images.
"""

import pygame
from pygame.locals import *
from classes import *
from constants import *

pygame.init()

#display the window

window = pygame.display.set_mode((WINDOW_SIDE + 50, WINDOW_SIDE + 50))

# Icone
icone = pygame.image.load(mg).convert_alpha()
pygame.display.set_icon(icone)
# Title
pygame.display.set_caption(title)


# displaying a background for the tile of the maze
background_tiles = pygame.image.load(background).convert()
window.blit(background_tiles,(25,25) )

# displaying the character .png
char_img = pygame.image.load(mg).convert_alpha()  # Add the png and transparency

# displaying the walls of the maze
wall = pygame.image.load(wall).convert()


# refresh
pygame.display.flip()



level = level('map.txt')
level.generate()
level.display(window)

#Note à moi même : Plus tard utiliser la structure

#Mac = Char(Char_img, level)
#tube = loot(tubeIMG, level)
#tube.display(tubeIMG, Window)
#needle = loot(needleIMG, level)
#needle.display(needleIMG, Window)
#ether = loot(etherIMG, level)
#ether.display(etherIMG, Window)
