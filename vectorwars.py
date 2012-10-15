import pygame
from pygame.locals import *
from random import *

from vector2 import vector2
from vex import vex
from player import vex_player

screen = None
shapes = []
count = 0

clock = pygame.time.Clock()

def gen_shape(x, y):
    pts = []
    num_pts = randint(4, 50)
    col_r = randint(10, 255)
    col_g = randint(10, 255)
    col_b = randint(10, 255)
    colour = pygame.Color(col_r, col_g, col_b)
    for i in range(0, num_pts/2):
         pts.append(vector2(randint(-vex.radius, vex.radius), randint(-vex.radius, vex.radius)))
    pts_rev = pts[:]
    pts_rev.reverse()
    for i in pts_rev:
        pts.append(vector2(-i.x, -i.y))
    return vex(x, y, colour, pts, 2)

def main():
    global count, shapes, screen, clock
    screen = pygame.display.set_mode((800, 600))
    shapes = []
    arrow_pts = [vector2(30, 0), vector2(10, 20), vector2(10, 10), 
            vector2(-30, 10), vector2(-30, -10), vector2(10, -10), 
            vector2(10, -20)]
    player = vex_player(50, 50, Color(255, 255, 255), arrow_pts, 2)
    shapes.append(player)
    while True:
        screen.fill(0)
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if e.key == K_q:
                    return
                elif e.key == K_r:
                    del shapes[:]
                elif e.key == K_w:
                    #move up
                    player.move_up = True
                    for i in shapes:
                        i.move_up = True
                elif e.key == K_s:
                    #move down
                    player.move_down = True
                    for i in shapes:
                        i.move_down = True
                elif e.key == K_a:
                    #move left
                    player.move_left = True
                    for i in shapes:
                        i.move_left = True
                elif e.key == K_d:
                    #move right
                    player.move_right = True
                    for i in shapes:
                        i.move_right = True
            elif e.type == KEYUP:
                if e.key == K_w:
                    #move up
                    player.move_up = False
                    for i in shapes:
                        i.move_up = False
                elif e.key == K_s:
                    #move down
                    player.move_down = False
                    for i in shapes:
                        i.move_down = False
                elif e.key == K_a:
                    #move left
                    player.move_left = False
                    for i in shapes:
                        i.move_left = False
                elif e.key == K_d:
                    #move right
                    player.move_right = False
                    for i in shapes:
                        i.move_right = False

            elif e.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if e.button == 1:
                    if len(shapes) >= 2:
                        shapes.append(shapes[-1].reproduce(shapes[-2], 
                            pos[0], pos[1]))
                    else:           
                        shapes.append(gen_shape(pos[0], pos[1]))
                elif e.button == 3:
                    shapes.append(gen_shape(pos[0], pos[1]))
                count += 1
            elif e.type == MOUSEMOTION:
                player.rotate(e.pos[0], e.pos[1]) 
        for s in shapes:
            if s.x < 0 or s.x > 800:
                #shapes.remove(s)
                s.xMod = -s.xMod
            elif s.y < 0 or s.y > 600:
                #shapes.remove(s)
                s.yMod = -s.yMod
            s.update(screen)
            s.draw(screen)
        pygame.display.update()
        clock.tick(30)
        
if __name__ == "__main__":
    main()
    print count
