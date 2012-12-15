import pygame
from pygame.locals import *

class EventEngine:
    """Manages the event queue and passes events to other engines"""
    
    def __init__(self, i_e):
        """Takes an input_engine and passes all relevant events to it"""
        self.input = i_e
    
    def update(self):
        """Pulls all relevant events from the event queue and passes
        them to the appropriate engines"""
        for e in pygame.event.get():
            if e.type == MOUSEMOTION:
                self.input.mouse_motion(e)
            elif e.type == MOUSEBUTTONDOWN:
                self.input.mouse_b_down(e)
            elif e.type == MOUSEBUTTONUP:
                self.input.mouse_b_up(e)
            elif e.type == KEYDOWN:
                self.input.key_down(e)
            elif e.type == KEYUP:
                self.input.key_up(e)
    
    def get_input(self):
        self.input.get_all()