import pygame
from pygame.locals import *

import math
from vector2 import Vector2
from vex import Vex

class BulletD(Vex):
    """Bullet that flies in one of the four cardinal directions"""
    def __init__(self, x, y, direction):
        if direction == 0:
            Vex.__init__(self, x, y, Color(0, 255, 0),
                     [Vector2(0, 5), Vector2(2, -5), Vector2(-2, -5)], 
                     1)
        if direction == 1:
            Vex.__init__(self, x, y, Color(0, 255, 0),
                     [Vector2(5, 0), Vector2(-5, -2), Vector2(-5, 2)], 
                     1)
        if direction == 2:
            Vex.__init__(self, x, y, Color(0, 255, 0),
                     [Vector2(0, -5), Vector2(2, 5), Vector2(-2, 5)], 
                     1)
        if direction == 3:
            Vex.__init__(self, x, y, Color(0, 255, 0),
                     [Vector2(-5, 0), Vector2(5, -2), Vector2(5, 2)], 
                     1)
            
        if direction == 0:
            self.x_mod = 0
            self.y_mod = 15
        elif direction == 1:
            self.x_mod = 15
            self.y_mod = 0
        elif direction == 2:
            self.x_mod = 0
            self.y_mod = -15
        elif direction == 3:
            self.x_mod = -15
            self.y_mod = 0
        self.direction = direction
        
    def move(self):
        self.x += self.x_mod
        self.y += self.y_mod
        
class BulletP(Vex):
    """Bullet that moves towards a point"""
    def __init__(self, x, y, p):
        """Create new bullet"""
        Vex.__init__(self, x, y, Color(0, 255, 0),
                 [Vector2(0, 5), Vector2(2, -5), Vector2(-2, -5)], 1)
        self.p = p
        v = self.vector_between(p)
        self.x_mod = v.normalised().x * 15
        self.y_mod = v.normalised().y * 15
        self.x = self.x + self.x_mod
        self.y = self.y + self.y_mod
        self.rotate_to_face_point(p)
        """
        direction = self.dir_vec()
        point = p
        v = p - direction
        angle = math.atan2(v.x, v.y)
        self.rotate_by_radians(-angle) 
        self.x_mod = v.normalised().x * 15
        self.y_mod = v.normalised().y * 15
        """
    
    def move(self):
        self.x += self.x_mod
        self.y += self.y_mod
        #print self.dir_vec()
        #print self.dir_vec().normalised()
        #print self.vector_between(self.p).normalised()