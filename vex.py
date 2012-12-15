import pygame
from pygame.locals import *
from vector2 import Vector2
from random import *
import math

def print_randint(a, b):
    num = randint(a, b)
    print "Random: ", num
    return num

class Vex():
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
        #self.dir_vec = points[0]
        #print "Direction:", self.dir_vec()
        #print self.__str__()
    
    def dir_vec(self):
        #print self.points[0] + vector2(self.x, self.y)
        
        # Consider: store direction separately, but rotate it when everything
        # else rotates. 
        
        
        v = Vector2(self.points[0].x, self.points[0].y)
        """
        # Trying to avoid weird edge cases where the mouse is close to the 
        # rotating body
        if v.x < self.radius or v.y < self.radius:
            v = v * self.radius
        
        # Trying to normalise v without losing directionality
        if v.x > v.y and abs(v.x) > 0 and abs(v.y) > 0:
            v = v/(v.x)
        elif v.y > v.x and abs(v.x) > 0 and abs(v.y) > 0:
            v = v/(v.y)
        """
        return v + Vector2(self.x, self.y)

    def draw(self, surface):
        pygame.draw.polygon(surface, self.colour, 
                self.get_absolute_points_tuple(), self.width)
        #dir_v = self.dir_vec()
        #pygame.draw.aaline(surface, pygame.Color(255, 0, 0), 
                #(self.x, self.y), (dir_v.x, dir_v.y), 4)

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
    
    @staticmethod
    def clamp(x, a, b):
        return min(max(x, a), b)

    #def is_facing_point(self, x, y):

    def vector_between(self, p):
        # What if this took the direction ONLY into account?
        # Normalising won't work - only covers one sector then
       
        # Trying relative vector mathematics
        p = p - Vector2(self.x, self.y)
        direction = Vector2(self.points[0].x, self.points[0].y)
        #direction = self.dir_vec()
        v = p - direction
        return v

    def angle_to_face_point(self, p):
        v = self.vector_between(p)
        #if v.normalised() is not vector2(0,0):
        # Getting consistency by forcing angle to points on the 360deg circle
        #angle_deg = int(math.atan2(v.x, v.y) * (180 / math.pi))
        #angle = angle_deg / (180 / math.pi)
        # This is wrong, should be y, x
        angle = math.atan2(v.x, v.y)
        #print angle_deg, angle
        #angle_deg = int(angle * 180/math.pi)
        #angle = float(angle_deg) / 180/math.pi
        #print angle_deg
        #if int(angle) == 0:
        return angle
        #else:
            #return 0
        
    def rotate_to_face_point(self, p):
        """Rotate the vex to face a point x, y"""
        # Rotation doesn't work continuously unless the start point is always
        # the same. This sets it.
        angle_start = self.angle_to_face_point(Vector2(self.x, self.y))
        self.rotate_by_radians(angle_start)
        # For some reason everything points the wrong way. Simply reverse the
        # angle here.
        self.rotate_by_radians(math.pi)
        angle = self.angle_to_face_point(p)
        angle_deg = int(angle * (180/math.pi))
        #print angle, angle * 180/math.pi
        #if angle_deg is not 0:
        self.rotate_by_radians(-angle)
        pass    
        #print angle_deg, angle, self.points[0]
        #print self.dir_vec().normalised()
        
    def rotate_by_radians(self, a):
        """Rotate the shape by a given number of radians"""
        cos_a = math.cos(a) # save these so we only need to do the 
        sin_a = math.sin(a) # call once for each
        for i in self.points:
            old_x = i.x 
            old_y = i.y # preserve old values
            i.x = (old_x*cos_a - old_y*sin_a) # use old values to calculate
            i.y = (old_x*sin_a + old_y*cos_a) # new values
        #print "Finished rotating"

    def move(self, x, y, surface): 
        if abs(x) > 0 or abs(y) > 0:
            if abs(x) > 0 and abs(y) > 0:
                x = x * .707
                y = y * .707
            if ((self.x + x < surface.get_width() and self.x + x > 0)
                and (self.y + y < surface.get_height() and self.y + y > 0)):
                #for p in self.points:
                    #p.x += x
                    #p.y += y
                self.x += int(x)
                self.y += int(y)

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
            pts.append(Vector2(p.x, p.y))
        return pts

    def get_absolute_points_vector2(self):
        """
        Returns a list of vector2 objects representing 2D points, relative 
        to origin.
        """
        pts = []
        for p in self.points:
            pts.append(Vector2(p.x+self.x, p.y+self.y))
        return pts
    
    def point_inside(self, v):
        """Determines roughly if a given point is inside the vex"""
        max_x = self.points[0].x
        max_y = self.points[0].x
        min_x = max_x
        min_y = max_y
        for i in self.points:
            if i.x > max_x:
                max_x = i.x
            elif i.x < min_x:
                min_x = i.x
            if i.y > max_y:
                max_y = i.y
            elif i.y < min_y:
                min_y = i.y
        max_x = max_x + self.x
        max_y = max_y + self.y
        min_x = min_x + self.x
        min_y = min_y + self.y
        
        if v.x < max_x and v.y < max_y and v.x > min_x and v.y > min_y:
            return True
        else:
            return False
    
