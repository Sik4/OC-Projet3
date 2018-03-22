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

window = pygame.display.set_mode((WINDOW_SIDE, WINDOW_SIDE + 50))
