import pygame
from pygame.locals import *
from vector2 import vector2
from random import *
import math

def print_randint(a, b):
    num = randint(a, b)
    print "Random: ", num
    return num

class vex():
    radius = 20
    def __str__(self):
        string = "Colour: %d, %d, %d" % (self.colour.r, self.colour.g, self.colour.b)
        #string = "Colour:", self.colour.r, self.colour.g, self.colour.b
        string = string + ("Position: %d, %d" % self.x, self.y)
        string = string + "Points:"
        for p in self.points:
            string = string + p
        return string


    def __init__(self, x, y, colour, points, width):
        self.colour = colour
        self.points = points
        self.width = width
        self.x = x
        self.y = y
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False
        self.direction_vector = points[0]
        #print self.__str__()

    def draw(self, surface):
        pygame.draw.polygon(surface, self.colour, 
                self.get_absolute_points_tuple(), self.width)

    def update(self, surface): # surface => check collision with outer bounds
        
        """
        if ((self.x < surface.get_width() and self.x > 0)
            and (self.y < surface.get_height() and self.y > 0)):
        if self.xMod % 5 == 0:
            self.xMod = -self.xMod - 1
        else:
            self.xMod -= 2
        if self.yMod % 5 == 0:
            self.yMod = -self.yMod - 1
        else:
            self.yMod -= 2
        for p in self.points:
            p.x += self.xMod
            p.y += self.yMod
        self.x += self.xMod
        self.y += self.yMod
        """
        #for p in self.points:
            #p.x += self.xMod
            #p.y += self.yMod
        #self.x += self.xMod
        #self.y += self.yMod
        #print"DERP"
        if self.move_up:
            self.move(0, -10, surface)
        elif self.move_down:
            self.move(0, 10, surface)
        elif self.move_left:
            self.move(-10, 0, surface)
        elif self.move_right:
            self.move(10, 0, surface)
    
    #def clamp(self, x, a, b):
        #return min(max(x, a), b)

    def rotate(self, x, y):
        """Rotate the vex to face a point x, y"""
        v = vector2(x, y)
        # get angle between (x, y) and points[0]
        # x = (x*cos(angle)) - (y*sin(angle))
        # y = (y*cos(angle)) + (x*sin(angle))
        #print self.points[0].angle_between(v) 
        a = self.direction_vector.radians_between(v)
        print a
        cos_a = math.cos(a)
        sin_a = math.sin(a)
        for i in self.points:
            old_x = i.x 
            old_y = i.y # preserve old values
            i.x = (old_x*cos_a - old_y*sin_a)
            i.y = (old_x*sin_a + old_y*cos_a)

    def move(self, x, y, surface): 
        if ((self.x + x < surface.get_width() and self.x + x > 0)
            and (self.y + y < surface.get_height() and self.y + y > 0)):
            #for p in self.points:
                #p.x += x
                #p.y += y
            self.x += x
            self.y += y

    def get_relative_points_tuple(self):
        """
        Returns a list of 2D points as tuples, relative to vex position.
        """
        pts = []
        for p in self.points:
            pts.append((p.x, p.y))
        return pts
    
    def get_absolute_points_tuple(self):
        """
        Returns a list of 2D points as tuples, relative to origin.
        """
        pts = []
        for p in self.points:
            pts.append((p.x+self.x, p.y+self.y))
        return pts

    def get_relative_points_vector2(self):
        """
        Returns a list of vector2 objects representing 2D points, relative 
        to vex position.
        """
        pts = []
        for p in self.points:
            pts.append(vector2(p.x, p.y))
        return pts

    def get_absolute_points_vector2(self):
        """
        Returns a list of vector2 objects representing 2D points, relative 
        to origin.
        """
        pts = []
        for p in self.points:
            pts.append(vector2(p.x+self.x, p.y+self.y))
        return pts
    
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
        return vex(x, y, colour, pts, 2)
