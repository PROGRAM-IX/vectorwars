from vex import vex
from vector2 import vector2
from random import *
import pygame
from pygame import *

class Enemy(vex):
    def __init__(self, x, y, colour, points, width, 
                 beh_dict={'follow': 100}):
        vex.__init__(self, x, y, colour, points, width)
        self.beh = beh_dict
    
    def reproduce(self, v, x, y): # Factory method pattern?
        pts = []
        num_pts = 0 # number of points in child 
        pos = vector2(x, y) # vector of position to place child
        this_rel_pts = self.get_relative_points_vector2() 
        v_rel_pts = v.get_relative_points_vector2()
        # decide number of points in child
        if len(this_rel_pts) < len(v_rel_pts):
            num_pts = randint(len(this_rel_pts), len(v_rel_pts))
        else:
            num_pts = randint(len(v_rel_pts), len(this_rel_pts))
        
        colour = None
        rand_r = choice((True, False))
        rand_g = choice((True, False))
        rand_b = choice((True, False))
        
        # Decide red part (random between parents)
        if self.colour.r < v.colour.r:
            col_r = randint(self.colour.r, v.colour.r)
        else:
            col_r = randint(v.colour.r, self.colour.r)
        # Decide green part (random between parents)
        if self.colour.g < v.colour.g:
            col_g = randint(self.colour.g, v.colour.g)
        else:
            col_g = randint(v.colour.g, self.colour.g)
        # Decide blue part (random between parents)
        if self.colour.b < v.colour.b:
            col_b = randint(self.colour.b, v.colour.b) 
        else:
            col_b = randint(v.colour.b, self.colour.b)

        if rand_r and (col_r + 100) <= 255 and col_r >= 0:
            col_r += randint(1,100)
        elif rand_r and (col_r + 100) > 255:
            col_r -= randint(1,100)
        
        if rand_g and (col_g + 100) <= 255 and col_g >= 0:
            col_g += randint(1, 100)
        elif rand_g and (col_g + 100) > 255:
            col_g -= randint(1, 100)

        if rand_b and (col_b + 100) <= 255 and col_b >= 0:
            col_b += randint(1, 100)
        elif rand_b and (col_b + 100) > 255:
            col_b -= randint(1, 100)

        colour = pygame.Color(col_r, col_g, col_b)
        # Grab points from both parents and generate random ones
        for i in xrange(0, num_pts/2):
            if i % 3 == 0:
                pt = vector2(randint(-vex.radius, 0), 
                        randint(-vex.radius, vex.radius))
                pts.append(pt)
            elif i % 2 == 0:
                if i < len(this_rel_pts):
                    pts.append(this_rel_pts[i])
                else:
                    pts.append(v_rel_pts[i])
            else:
                if i < len(v_rel_pts):
                    pts.append(v_rel_pts[i])
                else:
                    pts.append(this_rel_pts[i])
        pts_rev = pts[:]
        pts_rev.reverse()
        for i in pts_rev:
            pts.append(vector2(-i.x, i.y))
            #print pts[-1]
        return Enemy(x, y, colour, pts, 2)
    
def gen(x, y):
    pts = []
    num_pts = randint(4, 20)
    col_r = randint(10, 255)
    col_g = randint(10, 255)
    col_b = randint(10, 255)
    colour = pygame.Color(col_r, col_g, col_b)
    for i in range(0, num_pts/2):
        pts.append(vector2(randint(-vex.radius, 0), 
             randint(-vex.radius, vex.radius)))
    # Duplicate the list
    pts_rev = pts[:]
    # Reverse the new list
    pts_rev.reverse()
    # Copy the horizontally-inverted points into the array
    for i in pts_rev:
        pts.append(vector2(-i.x, i.y))
    return Enemy(x, y, colour, pts, 2)
