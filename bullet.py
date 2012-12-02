import pygame
from pygame.locals import *

import vex
import math
from vector2 import vector2
from vex import vex

class bullet_d(vex):
    """Bullet that flies in one of the four cardinal directions"""
    def __init__(self, x, y, dir):
        if dir == 0:
            vex.__init__(self, x, y, Color(0, 255, 0),
                     [vector2(0, 5), vector2(2, -5), vector2(-2, -5)], 
                     1)
        if dir == 1:
            vex.__init__(self, x, y, Color(0, 255, 0),
                     [vector2(5, 0), vector2(-5, -2), vector2(-5, 2)], 
                     1)
        if dir == 2:
            vex.__init__(self, x, y, Color(0, 255, 0),
                     [vector2(0, -5), vector2(2, 5), vector2(-2, 5)], 
                     1)
        if dir == 3:
            vex.__init__(self, x, y, Color(0, 255, 0),
                     [vector2(-5, 0), vector2(5, -2), vector2(5, 2)], 
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
        
class bullet_p(vex):
    """Bullet that moves towards a point"""
    def __init__(self, x, y, p):
        """Create new bullet"""
        vex.__init__(self, x, y, Color(0, 255, 0),
                 [vector2(0, 5), vector2(2, -5), vector2(-2, -5)], 1)
        direction = self.dir_vec()
        point = p
        #print self.dir_vec().normalised()
        #print "---------"
        v = p - direction
        angle = math.atan2(v.x, v.y)
        # Fail to negate this, bullets spawn directly opposite point
        self.rotate_by_radians(-angle) 
        direction = self.dir_vec().normalised()

        #print self.dir_vec()
        #print self.points[0]
        #print direction.x, direction.y
        #print "---------"

        self.x_mod = v.normalised().x * 15
        self.y_mod = v.normalised().y * 15
    
    def move(self):
        self.x += self.x_mod
        self.y += self.y_mod