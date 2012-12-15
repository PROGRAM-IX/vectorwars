import pygame
from pygame.locals import *

class InputEngine:
    def __init__(self):
        self.keys = [0] * 1024
        self.mouse_pos = (1,1)
        self.mouse_buttons = [0] * 16
        
    def mouse_motion(self, event):
        if self.mouse_pos is not event.pos:
            self.mouse_pos = event.pos    
    
    def mouse_b_down(self, event):
        self.mouse_buttons[event.button] = True
    
    def mouse_b_up(self, event):
        self.mouse_buttons[event.button] = False
    
    def key_down(self, event):
        self.keys[event.key] = True
        
    def key_up(self, event):
        self.keys[event.key] = False
        
    def get_all(self):
        print self.keys
        print self.mouse_pos
        print self.mouse_buttons