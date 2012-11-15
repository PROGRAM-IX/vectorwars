import pygame
from pygame.locals import *
import copy

class hud_element:
    def __init__(self, label, colour):
        """
        label: description of the element
        colour: colour of the element (pygame.Colour)
        """
        self.label = label
        self.colour = colour
        
    def draw(self, screen):
        """Draw the element to the screen"""
        pass

class hud_text(hud_element):
    
    letters = {
       'a': ((-5, -10), (-5, 15), (-5, -5), (5, -5), (5, 15),
             (5, -10), (-5, -10))
       
       }
    def __init__(self, label, colour, text, pos, size):
        """
        label: description of the element
        colour: colour of the element (pygame.Colour)
        text: text portion ofthe element 
        pos: coordinates of element
        """
        
        hud_element.__init__(self, label, colour)
        self.text = text
        self.pos = pos
        self.size = size
        
    def draw(self, screen):
        """Render the text to the screen"""
        c_pos = self.pos
        for letter in xrange(len(self.text)):
            if self.text[letter] in self.letters:
                a = self.letters[self.text[letter]]
                last = a[0]
                for pt in a:
                    pygame.draw.line(screen, self.colour, 
                                     (last[0]*self.size+c_pos[0], 
                                        last[1]*self.size+c_pos[1]), 
                                     (pt[0]*self.size+c_pos[0],
                                        pt[1]*self.size+c_pos[1]),
                                     1)
                    last = pt
            
                """pts = copy.deepcopy(self.letters[self.text[a]])
                for p in pts:
                    p = ((p[0]*self.size)+self.pos[0], 
                         (p[1]*self.size)+self.pos[1])
                    print p
                pygame.draw.polygon(screen, self.colour, pts, 1)
                """
                print "DRAWING",self.text[letter]
            c_pos = (c_pos[0] + self.size * 15, c_pos[1])


class hud_line(hud_element):
    def __init__(self, label, colour, line):
        """
        label: description of the element
        colour: colour of the element (pygame.Colour)
        line: line portion of the element
            (start pos tuple, end pos tuple, width)
        """
        hud_element.__init__(self, label, colour)
        self.line = line
    
    def draw(self, screen):
        """Render the line to the screen"""
        pygame.draw.line(screen, self.colour, self.line[0], self.line[1], 
                         self.line[-1])
        
class hud_polygon(hud_element):
    def __init__(self, label, colour, lines):
        """
        label: description of the element
        colour: colour of the element (pygame.Colour)
        lines: lines portion of the element
            (points tuple, width)
        """
        hud_element.__init__(self, label, colour)
        self.lines = lines
        
    def draw(self, screen):
        """Render the polygon to the screen"""
        pygame.draw.polygon(screen, self.colour, self.lines[:-1], 
                            self.lines[-1])
    
class hud:
    def __init__(self):
        self.elements = []
    
    def add(self, hud_el):
        self.elements.append(hud_el)
        
    def draw(self, screen):
        """Draws all elements of the HUD to the screen"""
        for e in self.elements:
            e.draw(screen)
            