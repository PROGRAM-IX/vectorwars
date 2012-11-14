import pygame
from pygame.locals import *

class input_engine:
    def __init__(self):
        self.keys = [0] * 256
        self.mouse_pos = (0,0)
        self.mouse_buttons = [0] * 256
    
    def mouse_motion(self, event):
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