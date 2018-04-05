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
import time

pygame.init()

# display the window

window = pygame.display.set_mode((window_side, window_side + 30))

# Icone
icone = pygame.image.load(mg).convert_alpha()
pygame.display.set_icon(icone)
# Title
pygame.display.set_caption(title)


# displaying a background for the tile of the maze
background_tiles = pygame.image.load(background).convert()
window.blit(background_tiles, (30, 30))

# displaying the character .png
char_img = pygame.image.load(mg).convert_alpha()  # Add the image

win = False
loose = False

# displaying the walls of the maze
wall = pygame.image.load(wall).convert()


# displaying the objects png's
tube_img = pygame.image.load(tube).convert_alpha()
needle_img = pygame.image.load(needle).convert_alpha()
ether_img = pygame.image.load(ether).convert_alpha()
victory_img = pygame.image.load(victory_img).convert_alpha()
defeat_img = pygame.image.load(defeat_img).convert_alpha()
# refresh
pygame.display.flip()


# Variable for the infinite loop
continue_game = 1

# items picked or not:
TubeNotPicked = True
EtherNotPicked = True
NeedleNotPicked = True


level = Level()
level.generate()
level.display(window)

# Note à moi même : Plus tard utiliser la structure
# defining constants

mac = Char(char_img, level)
tube = Loot(tube_img, level)
tube.display(tube_img, window)
needle = Loot(needle_img, level)
needle.display(needle_img, window)
ether = Loot(ether_img, level)
ether.display(ether_img, window)


while continue_game:

    pygame.time.Clock().tick(30)  # Limiting speed

    for event in pygame.event.get():  # waiting for quit input
        if event.type == QUIT:  # If any of these events is QUIT type
            continue_game = 0   # game windows is closed

        # Keyboard touch used to moove MacGyver:
        elif event.type == KEYDOWN:
            if event.key == K_DOWN:  # If ARROW DOWN pressed
                mac.mooving('down')
            elif event.key == K_UP:
                mac.mooving('up')
            elif event.key == K_LEFT:
                mac.mooving('left')
            elif event.key == K_RIGHT:
                mac.mooving('right')

    # Re-pasting after the events
    # Posting objects on top if picked
    window.blit(background_tiles, (0, 30))  # displaying window
    level.display(window)
    window.blit(mac.Image, (mac.x, mac.y))

    if TubeNotPicked:
        window.blit(tube.Loot_Image, (tube.x, tube.y))
    if (mac.x, mac.y) == (tube.x, tube.y):
        TubeNotPicked = False
        window.blit(tube.Loot_Image, (0, 0))

    if NeedleNotPicked:
        window.blit(needle.Loot_Image, (needle.x, needle.y))
    if (mac.x, mac.y) == (needle.x, needle.y):
        NeedleNotPicked = False
        window.blit(needle.Loot_Image, (10, 0))

    if EtherNotPicked:
        window.blit(ether.Loot_Image, (ether.x, ether.y))
    if (mac.x, mac.y) == (ether.x, ether.y):
        EtherNotPicked = False
        window.blit(ether.Loot_Image, (30, 0))

    # refreshing screen
    pygame.display.flip()

# EndGame Victory or loose
    if level.structure[mac.case_y][mac.case_x] == 'f':
        if (TubeNotPicked is False and NeedleNotPicked is False and
            EtherNotPicked is False):  # testing if objects are picked

            win = True
        else:
            loose = True  # Else it's game over !

    if win is True:
        window.blit(victory_img, (0, 30))
        pygame.display.flip()
        time.sleep(3)
        continue_game = 0

    if loose is True:
        window.blit(defeat_img, (0, 30))
        pygame.display.flip()
        time.sleep(3)
        continue_game = 0
