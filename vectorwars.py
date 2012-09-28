import pygame
from pygame.locals import *
from random import *

from vector2 import vector2
from vex import vex

screen = None
shapes = []
count = 0

clock = pygame.time.Clock()

def gen_shape(x, y):
    pts = []
    num_pts = randint(4, 10)
    col_r = randint(10, 255)
    col_g = randint(10, 255)
    col_b = randint(10, 255)
    colour = pygame.Color(col_r, col_g, col_b)
    for i in range(1, num_pts):
         pts.append(vector2(randint(x-40, x+40), randint(y-40, y+40)))
    return vex(x, y, colour, pts, 2)

def main():
    global count, shapes, screen, clock
    screen = pygame.display.set_mode((800, 600))
    shapes = []
    while True:
        screen.fill(0)
        for e in pygame.event.get():
            if e.type == KEYDOWN and e.key == K_q:
                return
            if e.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if len(shapes) >= 2:
                    shapes.append(shapes[-1].reproduce(shapes[-2], 
                            pos[0], pos[1]))
                else:           
                    shapes.append(gen_shape(pos[0], pos[1]))
                count += 1
        for s in shapes:
            if s.x < 0 or s.x > 800:
                shapes.remove(s)
            elif s.y < 0 or s.y > 600:
                shapes.remove(s)
            s.update(screen)
            s.draw(screen)
        pygame.display.update()
        clock.tick(30)
        
if __name__ == "__main__":
    main()
    print count
