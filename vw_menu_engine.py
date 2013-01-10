import pygame
from pygame.locals import *
from pystroke.hud import *
from pystroke.game_engine import GameEngine
from pystroke.vector2 import Vector2
from pystroke.vex import Vex
from pystroke.input_engine import InputEngine
from pystroke.event_engine import EventEngine


class VWMenuEngine(GameEngine):
    """
    VectorWars menu state
    
    @author: James Heslin (PROGRAM_IX)
    """
    def __init__(self, screen, event_e=EventEngine(InputEngine())):
        """
        Constructs a VWMenuEngine
        
        @type screen: pygame.Surface
        @param screen: The screen on which the game will be rendered - this will
        be passed around to other classes
        
        @author: James Heslin (PROGRAM_IX)  
        """
        GameEngine.__init__(self, screen, event_e)
        self._hud.add(HUDText("VectorWars", pygame.Color(0, 255, 0), 
                                  "vectorwars", (100, 100), 4, 2))
        self._hud.add(HUDText("credits1", pygame.Color(0, 255, 0), 
                                  "by program_ix", (200, 200), 2, 1))
        self._hud.add(HUDText("instructions1", pygame.Color(0, 255, 0), 
                                  "press enter to begin", (200, 250), 1, 1))
        self._hud.add(HUDText("instructions2", pygame.Color(0, 255, 0), 
                                  "wsad to move", (200, 300), 1, 1))
        self._hud.add(HUDText("instructions3", pygame.Color(0, 255, 0), 
                                  "left mouse to shoot", (200, 350), 1, 1))
        self._hud.add(HUDText("instructions4", pygame.Color(0, 255, 0), 
                                  "mouse to aim", (200, 400), 1, 1))
        self._hud.add(HUDText("instructions5", pygame.Color(0, 255, 0), 
                                  "c to reset", (200, 450), 1, 1))
        self._hud.add(HUDText("instructions6", pygame.Color(0, 255, 0), 
                                  "q to quit to menu", (200, 500), 1, 1))
        self._hud.add(HUDText("instructions7", pygame.Color(0, 255, 0), 
                                  "esc to quit game", (200, 550), 1, 1))
        
    def update(self):
        """
        Performs per-frame logic
        
        @rtype: int
        @return: Flag to tell Game what to do
        
        @author: James Heslin (PROGRAM_IX)
        """
        self.event_e.update()
        
        if self.event_e.input.keys[K_RETURN] == True:
            return 0
        elif self.event_e.input.keys[K_ESCAPE] == True:
            return 1
        
        # To switch state
        #if switch_state_condition:
        #    return 0
        
        # To quit 
        #elif quit_condition:
        #    return 1
        
        # To maintain consistency
        #else:
        #    return 2
        
        self.clock.tick(60)
                
        return 2
    
    def draw(self):
        """
        Draws all necessary elements using the DrawEngine
        
        @author: James Heslin (PROGRAM_IX)
        """
        self.draw_e.begin_draw(pygame.Color(0, 0, 0))
        self.draw_e.draw([self._hud])
        # Draw your drawables here
        # They must be passed in as lists
        # self.draw_e.draw([some_drawable, some_other_drawable])
        # self.draw_e.draw([another_drawable])
        self.draw_e.end_draw()
            