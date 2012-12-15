import pygame
from pygame.locals import *
import copy

class HUDElement:
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

class HUDText(HUDElement):
    
    letters = { 
        'a': ((-5, -10), (-5, 15), (-5, 0), (5, 0), (5, 15), 
              (5, -10), (-5, -10)),
        'b': ((-5, -10), (-5, 15), (5, 15), (5, 0), (-5, 0),
              (0, 0), (0, -10), (-5, -10)),
        'c': ((5, -10), (-5, -10), (-5, 15), (5, 15)),
        'd': ((0, -10), (-5, -10), (-5, 15), (0, 15), (5, 10), 
              (5, -5), (0, -10)),
        'e': ((5, -10), (-5, -10), (-5, 0), (0, 0), (-5, 0),
              (-5, 15), (5, 15)),
        'f': ((5, -10), (-5, -10), (-5, 0), (0, 0), (-5, 0),
              (-5, 15)),
        'g': ((5, -10), (-5, -10), (-5, 15), (5, 15), (5, 0), 
              (0, 0)),
        'h': ((-5, -10), (-5, 15), (-5, 0), (5, 0), (5, -10), 
              (5, 15)),
        'i': ((-5, -10), (5, -10), (0, -10), (0, 15), (-5, 15), 
              (5, 15)),
        'j': ((-5, -10), (5, -10), (0, -10), (0, 15), (-5, 15), 
              (-5, 10)),
        'k': ((-5, -10), (-5, 0), (5, -10), (-5, 0), (5, 15), 
              (-5, 0), (-5, 15)),
        'l': ((-5, -10), (-5, 15), (5, 15)),
        'm': ((-5, 15), (-5, -10), (0, -10), (0, 0), (0, -10), 
              (5, -10), (5, 15)),
        'n': ((-5, 15), (-5, -10), (5, 15), (5, -10)),
        'o': ((-5, -10), (-5, 15), (5, 15), (5, -10), (-5, -10)),
        'p': ((-5, 15), (-5, -10), (5, -10), (5, 0), (-5, 0)),
        'q': ((-5, -10), (-5, 10), (0, 10), (0, 15), (5, 15),
              (0, 15), (0, 10), (5, 10), (5, -10), (-5, -10)),
        'r': ((-5, 15), (-5, -10), (5, -10), (5, 0), (-5, 0),
              (5, 15)),
        's': ((5, -10), (-5, -10), (-5, 0), (5, 0), (5, 15), 
              (-5, 15)),
        't': ((-5, -10), (5, -10), (0, -10), (0, 15)),
        'u': ((-5, -10), (-5, 15), (5, 15), (5, -10)),
        'v': ((-5, -10), (0, 15), (5, -10)),
        'w': ((-5, -10), (-5, 15), (0, 15), (0, 0), (0, 15), 
              (5, 15), (5, -10)),
        'x': ((-5, -10), (5, 15), (0, 0), (-5, 15), (5, -10)),
        'y': ((-5, -10), (0, 0), (-5, 15), (5, -10)),
        'z': ((-5, -10), (5, -10), (-5, 15), (5, 15)),
        '1': ((-5, -5), (0, -10), (0, 15), (-5, 15), (5, 15)),
        '2': ((-5, -5), (-5, -10), (5, -10), (5, -5), (-5, 15), (5, 15)),
        '3': ((-5, -10), (5, -10), (0, 0), (5, 5), (0, 15), (-5, 15)),
        '4': ((0, 15), (0, -10), (-5, 0), (5, 0)),
        '5': ((5, -10), (-5, -10), (-5, 0), (0, 0), (5, 5), (5, 10),
              (0, 15), (-5, 15)),
        '6': ((5, -10), (-5, 0), (-5, 15), (5, 15), (5, 0), (-5, 0)),
        '7': ((-5, -10), (5, -10), (-5, 15)),
        '8': ((-5, -10), (5, -10), (5, -5), (0, 0), (-5, 5), 
              (-5, 15), (5, 15), (5, 5), (0, 0), (-5, -5), (-5, -10)),
        '9': ((5, 15), (5, -10), (-5, -10), (-5, 0), (5, 0)),
        '0': ((5, 15), (-5, -10), (-5, 15), (5, 15), (5, -10), (-5, -10))
       
       }
    def __init__(self, label, colour, text, pos, size, width):
        """
        label: description of the element
        colour: colour of the element (pygame.Colour)
        text: text portion ofthe element 
        pos: coordinates of element
        """
        
        HUDElement.__init__(self, label, colour)
        self.text = text
        self.pos = pos
        self.size = size
        self.width = width
        
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
                                     self.width)
                    last = pt
                #print "DRAWING",self.text[letter]
            c_pos = (c_pos[0] + self.size * 15, c_pos[1])


class HUD_Line(HUDElement):
    def __init__(self, label, colour, line):
        """
        label: description of the element
        colour: colour of the element (pygame.Colour)
        line: line portion of the element
            (start pos tuple, end pos tuple, width)
        """
        HUDElement.__init__(self, label, colour)
        self.line = line
    
    def draw(self, screen):
        """Render the line to the screen"""
        pygame.draw.line(screen, self.colour, self.line[0], self.line[1], 
                         self.line[-1])
        
class HUDPolygon(HUDElement):
    def __init__(self, label, colour, lines):
        """
        label: description of the element
        colour: colour of the element (pygame.Colour)
        lines: lines portion of the element
            (points tuple, width)
        """
        HUDElement.__init__(self, label, colour)
        self.lines = lines
        
    def draw(self, screen):
        """Render the polygon to the screen"""
        pygame.draw.polygon(screen, self.colour, self.lines[:-1], 
                            self.lines[-1])
    
class HUD:
    def __init__(self):
        self.elements = []
    
    def add(self, hud_el):
        self.elements.append(hud_el)
        
    def draw(self, screen):
        """Draws all elements of the HUD to the screen"""
        for e in self.elements:
            e.draw(screen)
            
    def get(self, id):
        """Returns a hud_element with matching id from elements, otherwise
        returns None"""
        for e in self.elements:
            if e.label == id:
                return e
        return None