import pygame
from pygame.locals import *
from vex import vex

class vex_player(vex):
    def __init__(self, x, y, colour, points, width):
        vex.__init__(self, x, y, colour, points, width)
