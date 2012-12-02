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
        #self.dir_vec = points[0]
        #print "Direction:", self.dir_vec()
        #print self.__str__()
    
    def dir_vec(self):
        #print self.points[0] + vector2(self.x, self.y)
        return vector2(self.x+self.points[0].x, self.y+self.points[0].y)

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


    def rotate_to_face_point(self, x, y):
        """Rotate the vex to face a point x, y"""
        """
        v = vector2(x, y) - vector2(self.dir_vec().x, 
                self.dir_vec().y)
        #a = self.dir_vec.radians_between(v)
        a = math.atan2(x - self.dir_vec().y, 
                y - self.dir_vec().x)
        mine = vector2(self.dir_vec().x, self.dir_vec().y)
        theirs = vector2(x, y)
        mine.normalise()
        theirs.normalise()
        res = mine - theirs
        print res
        # checking to see would fuzzy values make it at least half accurate
        #if (res.x < .6 and res.y < .6 and res.x > -.6 and res.y > -.6):
        self.rotate_by_radians(a)
        """
        # NEW PLAN 13/11/12 (No idea if this is already what's there)
        # Get angle between self.pos -> self.dir_v and self.pos -> point
        # Change it to be <= 180
        # Do rotation
        
        # Vector indicating direction 
        dir_v = self.dir_vec().normalised()
        # Vector from (x,y) to position
        goal_v = vector2(x-self.x, y-self.y).normalised()
        # Get dot product of two vectors
        d_p = dir_v.dot_product(goal_v)
        # Get cross product of two vectors
        c_p = dir_v.cross_product(goal_v)
        # Use acos to get the angle 
        angle = math.acos(d_p/(dir_v.get_magnitude() * goal_v.get_magnitude()))        
        print "Dir:", dir_v
        print "Goal:", goal_v
        print self.x, self.y
        print x, y  
        print "Dot:", d_p
        print "Cross:", c_p
        print "Angle (rad):", angle
        print "Angle (deg)", angle * 180/math.pi
        # HACK ALERT - seems there is a 33deg difference in everything
        # Hence this line
        # Still doesn't fix things
        angle -= 33.1 / 180/math.pi
        print "Modified angle (rad)", angle
        print "Modified angle (deg)", angle * 180/math.pi
        self.rotate_by_radians(angle)
        
        """
        dir_v = self.dir_vec().normalised()
        m_v = vector2(x, y).normalised()
        #angle = math.fabs(math.atan(self.y-y/self.x - x) - math.pi/2)
        
        cos_angle = ((dir_v.x * m_v.x + dir_v.y * m_v.y)
                / math.sqrt(dir_v.x*dir_v.x + dir_v.y*dir_v.y)
                * math.sqrt(m_v.x*m_v.x + m_v.y * m_v.y))
        angle = math.acos(cos_angle)
        #angle = angle * 180/math.pi
        if angle > math.pi:
            print "Greater than 180. Flipping."
            angle = -angle + math.pi
        """
        """
        dir_v = self.dir_vec()
        pt_v = dir_v + vector2(x, y) 
        dir_v.normalise()
        pt_v.normalise()
        #print dir_v
        print "----"
        print "DP:", dir_v.dot_product(pt_v)
        print dir_v, pt_v
        print "|dir_v|:", dir_v.get_magnitude()
        print "|pt_v|:", pt_v.get_magnitude()
        angle = dir_v.radians_between(pt_v)
        #angle = (dir_v.dot_product(pt_v) /
        #        dir_v.get_magnitude() * pt_v.get_magnitude())
        #angle = math.atan2(y - self.dir_vec().y, 
        #        x - self.dir_vec().x)
        if angle > math.pi*2: # make sure not to do too much rotation
            while angle > math.pi*2: # bigger than 360?
                angle = angle - math.pi*2 # cut it down to be less
        elif angle < -(math.pi*2):
            while angle < (-math.pi*2):
                angle = angle + math.pi*2
        #if angle > math.pi: # bigger than 180?
            #angle = -(math.pi - angle) # reverse it and invert the value
        #elif angle < -math.pi:
            #angle = math.pi + angle
        """
        """
        #print angle
        #print angle*(180/math.pi)
        dp = vector2(self.x-x, self.y-y).dot_product(self.dir_vec())
        #print dp
        print "Radians:", angle
        print "Degrees:", angle * 180/math.pi
        if angle*180/math.pi > 360 : # make sure not to do too much rotation
            angle = angle % math.pi*2
            print "Angle:", angle
        #if angle > math.pi: # bigger than 180?
            #angle = -(math.pi - angle) # reverse it and invert the value
        #elif angle < -math.pi:
            #angle = math.pi + angle
        #print math.atan2(dir_v.y, dir_v.x) * 180*math.pi
        #if(dp > 0):
        self.rotate_by_radians(angle)
        #if angle < .6 and angle > -.6:
        #    pass
        #if angle > .2:
        #    self.rotate_by_radians(math.pi/6)
        #elif angle < -.2:
        #    self.rotate_by_radians(-math.pi/6)
        """
        
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
            print "COLLIDE"
        else:
            return False
    
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
    return vex(x, y, colour, pts, 2)
