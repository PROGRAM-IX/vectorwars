import pygame
from pygame.locals import *

import vex
from vector2 import vector2
from vex import vex

class bullet(vex):
    def __init__(self, x, y, dir):
        if dir == 0:
            vex.__init__(self, x, y, Color(0, 255, 0),
                     [vector2(0, 10), vector2(5, -10), vector2(-5, -10)], 
                     1)
        if dir == 1:
            vex.__init__(self, x, y, Color(0, 255, 0),
                     [vector2(10, 0), vector2(-10, -5), vector2(-10, 5)], 
                     1)
        if dir == 2:
            vex.__init__(self, x, y, Color(0, 255, 0),
                     [vector2(0, -10), vector2(5, 10), vector2(-5, 10)], 
                     1)
        if dir == 3:
            vex.__init__(self, x, y, Color(0, 255, 0),
                     [vector2(-10, 0), vector2(10, -5), vector2(10, 5)], 
                     1)
            
        if dir == 0:
            self.x_mod = 0
            self.y_mod = 15
        elif dir == 1:
            self.x_mod = 15
            self.y_mod = 0
        elif dir == 2:
            self.x_mod = 0
            self.y_mod = -15
        elif dir == 3:
            self.x_mod = -15
            self.y_mod = 0
        self.dir = dir
        
    def move(self):
        self.x += self.x_mod
        self.y += self.y_mod