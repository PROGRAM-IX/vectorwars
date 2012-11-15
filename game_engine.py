import pygame
from pygame.locals import *
from hud import *

from input_engine import input_engine
from event_engine import event_engine
from draw_engine import draw_engine

class game_engine:
    def __init__(self, screen):
        i_e = input_engine()
        #self.screen = screen
        self.event_e = event_engine(i_e)
        self.draw_e = draw_engine(screen)
        #self.beh_e = behaviour_engine()
        self.clock = pygame.time.Clock()
        self._hud = hud()
        self.enemies = []
        
    def update(self):
        self.event_e.update()
        if self.event_e.input.keys[K_ESCAPE]==True:
            raise SystemExit
        elif self.event_e.input.keys[K_SPACE]==True:
            print self
        
        self.clock.tick(30)
            
    def draw(self):
        self.draw_e.draw(self.enemies)
        self.draw_e.draw([self._hud])
        pygame.display.update()
        
    def run(self):
        self._hud.add(hud_polygon("Box1", pygame.Color(255, 255, 255),
                                  ((50, 50), (750, 50), 
                                  (750, 550), (50, 550), 2)))
        self._hud.add(hud_line("Line1", pygame.Color(255, 0, 255), 
                               ((100, 100), (700, 100), 4)))
        self._hud.add(hud_text("A1", pygame.Color(255, 255, 0), 
                               "aaaaa", (400, 300), 1))
        while True:
            self.update()
            self.draw()