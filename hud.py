import pygame
from pygame.locals import *

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
    def __init(self, label, colour, text):
        """
        label: description of the element
        colour: colour of the element (pygame.Colour)
        text: text portion ofthe element 
        """
        hud_element.__init__(self, label, colour)
        self.text = text
        
    def draw(self, screen):
        """Render the text to the screen"""
        pass

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
                         self.width)
        
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
            