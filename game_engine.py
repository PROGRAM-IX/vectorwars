import pygame
from pygame.locals import *
from hud import *

import random


from vex import *
from bullet import bullet
from vector2 import vector2

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
        self.player = vex(400, 300, pygame.Color(0, 255, 0), 
                          [vector2(0, -20), vector2(20, 0), vector2(0, 20), 
                           vector2(-20, 0)], 5)
        self.enemies = []
        self.bullets = []
        self.score = 100
        self.rep_interval = 60
        self.rep_count = 1
        
        
        
    def spawn(self, num):
        for i in xrange(num):
            x = randint(100, 700)
            y = randint(100, 500)
            self.enemies.append(gen(x, y))    
        

    def reset_game(self):
        del self.enemies
        self.enemies = []
        del self.bullets
        self.bullets = []
        self.spawn(2)

    def update(self):
        self.event_e.update()
        if self.event_e.input.keys[K_ESCAPE]==True:
            raise SystemExit
        if self.event_e.input.keys[K_SPACE]==True:
            self.score_inc(5)
        if self.event_e.input.keys[K_c] == True:
            self.reset_game()
        if self.event_e.input.keys[K_DOWN] == True:
            # Fire down
            self.player_shoot(0)
        elif self.event_e.input.keys[K_UP] == True:
            # Fire up
            self.player_shoot(2)
        elif self.event_e.input.keys[K_LEFT] == True:
            # Fire left            
            self.player_shoot(3)
        elif self.event_e.input.keys[K_RIGHT] == True:
            # Fire right
            self.player_shoot(1)
        
        if self.event_e.input.keys[K_w] == True:
            # Move up
            self.player.y -= 5
            pass
        elif self.event_e.input.keys[K_s] == True:
            # Move down
            self.player.y += 5
            pass
        
        if self.event_e.input.keys[K_a] == True:
            # Move left
            self.player.x -= 5
            pass
        elif self.event_e.input.keys[K_d] == True:
            # Move right
            self.player.x += 5
            pass
        
        self.bullet_update()
        
        
        if len(self.enemies) is not 0:
            self.rep()
            self.collide()
        else:
            self.spawn(4)
        
        self.clock.tick(30)
            
    def score_inc(self, pts):
        self.score += 50*pts
        sc = self._hud.get("Score")
        if(sc is not None):
            sc.text = "score "+str(self.score)
            
    def collide(self):
        dead_enemies = []
        dead_bullets = []
        for e in self.enemies:
            for b in self.bullets:
                if e.point_inside(vector2(b.x, b.y)): 
                    #print "COLLIDE2"       
                    self.score_inc(len(e.points))
                    if e not in dead_enemies:
                        dead_enemies.append(e)
                    if b not in dead_bullets:
                        dead_bullets.append(b)
                    
        for e in dead_enemies:
            self.enemies.remove(e)
        for b in dead_bullets:
            self.bullets.remove(b)
                    
    def draw(self):
        self.draw_e.begin_draw(pygame.Color(0,0,0))
        self.draw_e.draw(self.enemies)
        self.draw_e.draw(self.bullets)
        self.draw_e.draw([self.player])
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
            
    def rep(self):
        if(self.rep_count % self.rep_interval == 0 and len(self.enemies)>1):
            p1 = randint(0, len(self.enemies)-1)
            p2 = p1
            while (p1 == p2):
                p2 = randint(0, len(self.enemies)-1)
            if self.enemies[p1].x < self.enemies[p2].x:
                x = randint(self.enemies[p1].x, self.enemies[p2].x)
            else:
                x = randint(self.enemies[p2].x, self.enemies[p1].x)
            if self.enemies[p1].y < self.enemies[p2].y:
                y = randint(self.enemies[p1].y, self.enemies[p2].y)
            else:
                y = randint(self.enemies[p2].y, self.enemies[p1].y)
            self.enemies.append(
                self.enemies[p1].reproduce(self.enemies[p2], x, y))
        self.rep_count += 1
        #print self.rep_count

    def bullet_update(self):
        for b in self.bullets:
            if b.x > 700 or b.x < 100 or b.y > 500 or b.y < 100:
                self.bullets.remove(b)
            b.move()

    def player_shoot(self, dir):
        return self.bullets.append(bullet(self.player.x, self.player.y, dir))


        