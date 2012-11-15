import pygame
from pygame.locals import *
from hud import *

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
        self._hud = hud()
        self.enemies = []
        self.score = 100
        
    def update(self):
        self.event_e.update()
        if self.event_e.input.keys[K_ESCAPE]==True:
            raise SystemExit
        elif self.event_e.input.keys[K_SPACE]==True:
            print self
        elif self.event_e.input.keys[K_UP] == True:
            self.score += 1
            sc = self._hud.get("Score")
            if(sc is not None):
                sc.text = "score "+str(self.score)
        self.clock.tick(30)
            
    def draw(self):
        self.draw_e.begin_draw(pygame.Color(0,0,0))
        self.draw_e.draw(self.enemies)
        self.draw_e.draw([self._hud])
        self.draw_e.end_draw()
        
    def run(self):
        self._hud.add(hud_polygon("Box1", pygame.Color(255, 255, 255),
                                  ((50, 50), (750, 50), 
                                  (750, 550), (50, 550), 2)))
        self._hud.add(hud_text("Score", pygame.Color(255, 255, 255),
                               "score "+str(self.score), (15, 20), 1, 2))
        """
        self._hud.add(hud_line("Line1", pygame.Color(255, 0, 255), 
                               ((100, 100), (700, 100), 4)))
        self._hud.add(hud_text("A1", pygame.Color(255, 255, 0), 
                               "abcdefghijk", (400, 300), 1, 2))
        self._hud.add(hud_text("A2", pygame.Color(255, 255, 0), 
                               "lmnopqrs", (400, 350), 1, 2))
        self._hud.add(hud_text("A2", pygame.Color(255, 255, 0), 
                               "tuvwxyz", (400, 400), 1, 2))
        self._hud.add(hud_text("A2", pygame.Color(255, 255, 0), 
                               "0123456789", (400, 450), 1, 2))
        """
        while True:
            self.update()
            self.draw()