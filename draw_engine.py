import pygame
from pygame.locals import *

class DrawEngine:
    def __init__(self, screen):
        self.screen = screen
    
    def draw(self, drawables):
        """Presumes everything in the drawables list has a draw()
        method, and draws all of them to screen."""
        for d in drawables:
            d.draw(self.screen)
            #print "Drawing", d
            
    def begin_draw(self, colour):
        self.screen.fill(colour)
        
    def end_draw(self):
        pygame.display.update()