import pygame
from pygame.locals import *

from input_engine import input_engine
from event_engine import event_engine
from draw_engine import draw_engine

class game_engine:
    def __init__(self, screen):
        i_e = input_engine()
        self.event_e = event_engine(i_e)
        self.draw_e = draw_engine(screen)
        #self.beh_e = behaviour_engine()
        self.clock = pygame.time.Clock()
        
    def update(self):
        self.event_e.update()
        if self.event_e.input.keys[K_ESCAPE]==True:
            raise SystemExit
        elif self.event_e.input.keys[K_SPACE]==True:
            print self
       
        self.clock.tick(30)
            
    def run(self):
        while True:
            self.update()
            #self.draw_e.draw()