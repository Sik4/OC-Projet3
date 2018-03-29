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

# displaying the objects png's
tube_img = pygame.image.load(tube).convert_alpha()
needle_img = pygame.image.load(needle).convert_alpha()
ether_img = pygame.image.load(ether).convert_alpha()

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

#Note à moi même : Plus tard utiliser la structure

mac = Char(char_img, level)
tube = Loot(tube_img, level)
tube.display(tube_img, window)
needle = Loot(needle_img, level)
needle.display(needle_img, window)
ether = Loot(ether_img, level)
ether.display(ether_img, window)

while continue_game:

    pygame.time.Clock().tick(30)  # Limiting the loop speed to 30f/s to save processor ressources

    for event in pygame.event.get():    #Seeking every events happening while the game is running
        if event.type == QUIT:  # If any of these events is QUIT type
            continue_game = 0   # Loop is stopped and the game windows is closed

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
    window.blit(background_tiles, (0, 30))  # the background is streched from below the black margin to the opposite corner
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
