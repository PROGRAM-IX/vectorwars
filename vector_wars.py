import pygame
from vw_game_engine import VWGameEngine
from pystroke.game import Game

class VectorWars(Game):
    def __init__(self, width, height):
        Game.__init__(self, width, height)
        
    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.engines = [VWGameEngine(self.screen, self.e_e)]
        self.engine = self.engines[0]
        self.run()
        
def main():
    g = VectorWars(800, 600)
    g.start()
    
if __name__ == "__main__":
    main()