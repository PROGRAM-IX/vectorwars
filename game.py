import pygame
from game_engine import game_engine

class game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = None
        self.engine = None
        
    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.engine = game_engine(self.screen)
        self.engine.run()
        
def main():
    g = game(800, 600)
    g.start()
    
if __name__ == "__main__":
    main()