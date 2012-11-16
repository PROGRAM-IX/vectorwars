import pygame
from pygame.locals import *
from random import *

from vector2 import vector2
from vex import vex
from player import vex_player

import math

import figure

screen = None
shapes = []
count = 0

clock = pygame.time.Clock()



def main():
    global count, shapes, screen, clock
    screen = pygame.display.set_mode((800, 600))
    shapes = []
    arrow_pts = [vector2(60, 0), vector2(20, 40), vector2(20, 20), 
            vector2(-60, 20), vector2(-60, -20), vector2(20, -20), 
            vector2(20, -40)]
    player = vex_player(50, 50, Color(255, 255, 255), arrow_pts, 2)
    shapes.append(player)
    rotate_done = False
    mousex = 400
    mousey = 300
    while True:
        screen.fill(0)
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if e.key == K_q:
                    return
                elif e.key == K_SPACE:
                    rotate_done = not rotate_done
                elif e.key == K_r:
                    del shapes[:]
                elif e.key == K_w:
                    #move up
                    player.move_up = True
                elif e.key == K_s:
                    #move down
                    player.move_down = True
                elif e.key == K_a:
                    #move left
                    player.move_left = True
                elif e.key == K_d:
                    #move right
                    player.move_right = True
                elif e.key == K_UP:
                    #rotate 45deg
                    player.rotate_by_radians(math.pi/4)
                elif e.key == K_DOWN:
                    #rotate -45deg
                    player.rotate_by_radians(-math.pi/4)
            elif e.type == KEYUP:
                if e.key == K_w:
                    #move up
                    player.move_up = False
                elif e.key == K_s:
                    #move down
                    player.move_down = False
                elif e.key == K_a:
                    #move left
                    player.move_left = False
                elif e.key == K_d:
                    #move right
                    player.move_right = False

            elif e.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if e.button == 1:
                    if len(shapes) >= 2:
                        shapes.append(shapes[-1].reproduce(shapes[-2], 
                            pos[0], pos[1]))
                    else:           
                        shapes.append(gen(pos[0], pos[1]))
                elif e.button == 3:
                    shapes.append(gen(pos[0], pos[1]))
                count += 1
            #elif e.type == MOUSEMOTION and not rotate_done:
            elif e.type == MOUSEMOTION:
                mousex, mousey = e.pos
            if not rotate_done:
                #if player_pos to dir_v is not facing player_pos to mouse_pos
                #    rotate_done = False
                #else
                #    rotate_done = True
                #print mousex, mousey
                """#player.rotate(e.pos[0], e.pos[1])
                for sh in [player]:
                    sh.rotate_to_face_point(e.pos[0], e.pos[1])
                    pygame.draw.line(screen, pygame.Color(0, 255, 0),
                            (e.pos[0], e.pos[1]), (sh.x, sh.y), 2) 
                    pygame.draw.line(screen, pygame.Color(0, 0, 255),
                            (sh.x, sh.y), (sh.direction_vector().x,
                                sh.direction_vector().y), 1)
                    pygame.draw.line(screen, pygame.Color(255, 255, 0),
                            (sh.direction_vector().x, 
                                sh.direction_vector().y), 
                            (e.pos[0], e.pos[1]), 1)
                #rotate_done = True"""
                for sh in [player]:
                    if not rotate_done:
                        sh.rotate_to_face_point(mousex, mousey)
                        #rotate_done = True
                        pygame.draw.line(screen, pygame.Color(0, 255, 0),
                            (mousex, mousey), (sh.x, sh.y), 2) 
                        pygame.draw.line(screen, pygame.Color(255, 255, 0),
                            (sh.dir_vec().x, sh.dir_vec().y), 
                                (mousex, mousey), 1)
        figure.display(screen, 800, 600) # display x, y axis
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
        clock.tick(10)
        
if __name__ == "__main__":
    main()
    pygame.quit()
    print count
