# level creation

import pygame

from pygame.locals import *

from constants import *

import random


class Level:
    """designing the maze"""
    def __init__(self):
        self.file = "map.txt"
        self.structure = []

    def generate(self):
        with open(self.file, "r") as file:  # read only on the map.txt file
            level_structure = []            # level as an empty list

            for line in file:
                line_level = []

                # adding sprites in lines list, then lines in structure list
                for sprite in line:
                    if sprite != "\n":  # eliminating line return
                        line_level.append(sprite)
                level_structure.append(line_level)
            self.structure = level_structure

    def display(self, window):
        wall = pygame.image.load('images/wall.png').convert()
        finish = pygame.image.load('images/finish.png').convert_alpha()

        num_line = 0
        for line in self.structure:
            num_case = 0
            for sprite in line:
                x = num_case * Sprite_Size    # sprites localisation
                y = num_line * Sprite_Size
                if sprite == 'w':             # w = wall in map.txt
                    window.blit(wall, (x, y))
                elif sprite == 'f':
                    window.blit(finish, (x, y))
                num_case = num_case + 1

            num_line = num_line + 1


class Char:

    """ This is the class used for MacGyver sprite"""
    def __init__(self, Image, level):
        self.Image = pygame.image.load(mg).convert_alpha()
        """self.Position = Char.get_rect()"""
        self.case_x = 0
        self.case_y = 1
        self.x = 0
        self.y = 30  # start is under black margin
        self.level = level

    # Keyboard touch used to moove MacGyver:
    def mooving(self, direction):
        if direction == 'right':
            if self.case_x < (Nbr_Sprite_Side - 1):  # stop at border !
                if self.level.structure[self.case_y][self.case_x + 1] != 'w':
                    self.case_x += 1
                    self.x = self.case_x * Sprite_Size
                    print(self.x, self.y)

        if direction == 'left':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x - 1] != 'w':
                    self.case_x -= 1
                    self.x = self.case_x * Sprite_Size
                    print(self.x, self.y)

        if direction == 'up':
            if self.case_y > 0:
                if self.level.structure[self.case_y - 1][self.case_x] != 'w':
                    if (self.level.structure[self.case_y - 1]
                            [self.case_x] != 't'):
                        self.case_y -= 1
                        self.y = self.case_y * Sprite_Size
                        print(self.x, self.y)

        if direction == 'down':
            if self.case_y < (Nbr_Sprite_Side):
                if self.level.structure[self.case_y+1][self.case_x] != 'w':
                    self.case_y += 1
                    self.y = self.case_y * Sprite_Size
                    print(self.x, self.y)


class Loot:  # the class for the items
    def __init__(self, Loot_Image, level):
        self.case_y = 0
        self.case_x = 0
        self.x = 0
        self.y = 0
        self.level = level
        self.loaded = True
        self.Loot_Image = Loot_Image

    def display(self, Loot_Image, Window):  # randomisation of item places
        while self.loaded:
            self.case_x = random.randint(0, 14)
            self.case_y = random.randint(0, 14)
            if self.level.structure[self.case_y][self.case_x] == '0':
                self.y = self.case_y * Sprite_Size
                self.x = self.case_x * Sprite_Size
                self.loaded = False
