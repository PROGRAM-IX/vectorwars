import pygame
from pygame.locals import *
from vector2 import vector2
from random import *

def print_randint(a, b):
    num = randint(a, b)
    print "Random: ", num
    return num

class vex():
    radius = 20
    def __str__(self):
        string = "Colour: %d, %d, %d" % (self.colour.r, self.colour.g, self.colour.b)
        #string = "Colour:", self.colour.r, self.colour.g, self.colour.b
        #string = string + ("Position: %d, %d" % self.x, self.y)
        #string = string + "Points:"
        #for p in self.points:
            #string = string + p
        return string


    def __init__(self, x, y, colour, points, width):
        self.colour = colour
        self.points = points
        self.width = width
        self.xMod = 5
        self.yMod = -5
        self.x = x
        self.y = y
        #print self.__str__()

    def draw(self, surface):
        pygame.draw.polygon(surface, self.colour, self.get_points_tuple(), self.width)

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
        for p in self.points:
            p.x += self.xMod
            p.y += self.yMod
        self.x += self.xMod
        self.y += self.yMod
        

    def get_points_tuple(self):
        pts = []
        for p in self.points:
            pts.append((p.x, p.y))
        return pts

    def get_relative_points(self):
        pts = []
        for p in self.points:
            pts.append(p.x - self.x, p.y - self.y)
        return pts

    def get_relative_points_vector2(self):
        pts = []
        for p in self.points:
            pts.append(vector2(p.x - self.x, p.y - self.y))
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
            if i % 5 == 0:
                pt = vector2(randint(-self.radius, self.radius), randint(-self.radius, self.radius))
                pts.append(pt + pos)
            elif i % 2 == 0:
                if i < len(this_rel_pts):
                    pts.append(this_rel_pts[i] + pos)
                else:
                    pts.append(v_rel_pts[i] + pos)
            else:
                if i < len(v_rel_pts):
                    pts.append(v_rel_pts[i] + pos)
                else:
                    pts.append(this_rel_pts[i] + pos)
        pts_rev = pts[:]
        pts_rev.reverse()
        for i in pts_rev:
            pts.append(vector2(x - i.x, y - i.y) + pos)
        return vex(x, y, colour, pts, 2)
