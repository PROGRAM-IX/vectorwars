import pygame
from pygame.locals import *

class draw_engine:
    def __init__(self, screen):
        self.screen = screen
    
    def draw(self, drawables):
        """Presumes everything in the drawables list has a draw()
        method, and draws all of them to screen."""
        for d in drawables:
            d.draw(self.screen)
            #print "Drawing", d