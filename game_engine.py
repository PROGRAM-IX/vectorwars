import pygame
from pygame.locals import *
from hud import *

from behaviour_engine import BehaviourEngine

from random import randint

from vex import Vex
from enemy import gen
from bullet import BulletD, BulletP
from vector2 import Vector2
from player import Player

from input_engine import InputEngine
from event_engine import EventEngine
from draw_engine import DrawEngine


class GameEngine:
    def __init__(self, screen):
        self.FPS = 60
        i_e = InputEngine()
        
        self.screen = screen
        self.event_e = EventEngine(i_e)
        self.draw_e = DrawEngine(screen)
        self.beh_e = BehaviourEngine()
        self.clock = pygame.time.Clock()
        self._hud = HUD()
        self.player = Player(400, 300, pygame.Color(0, 255, 0), 
                          [Vector2(0, 20), Vector2(10, 0), Vector2(10, -20), 
                           Vector2(-10, -20), Vector2(-10, 0)], 3)
        self.enemies = []
        self.bullets = []
        self.score = 0
        self.high_score = 0
        #self.rep_interval = self.FPS * 10 / 3
        self.rep_interval = self.FPS/10
        self.rep_count = 1
        self.shoot_interval = self.FPS/10
        self.shoot_count = 0
        self.player_speed = 5
        
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
        self.shoot_count = 0
    
    def populate(self):
        self.spawn(4)

    def game_over(self):
        self.reset_game()
        self.reset_score()

    def update(self):
        p_move_x = 0 # How much the player will move (H)
        p_move_y = 0 # How much the player will move (V)
        
        self.event_e.update()
        if self.event_e.input.keys[K_ESCAPE] == True:
            raise SystemExit
        if self.event_e.input.keys[K_SPACE] == True:
            self.score_inc(5)
        if self.event_e.input.keys[K_c] == True:
            self.reset_game()
            self.populate()
        if self.event_e.input.keys[K_DOWN] == True:
            # Fire down
            self.player_shoot_dir(0)
        elif self.event_e.input.keys[K_UP] == True:
            # Fire up
            self.player_shoot_dir(2)
        elif self.event_e.input.keys[K_LEFT] == True:
            # Fire left            
            self.player_shoot_dir(3)
        elif self.event_e.input.keys[K_RIGHT] == True:
            # Fire right
            self.player_shoot_dir(1)
        elif self.event_e.input.mouse_buttons[1] == True:
            # Fire towards the mouse cursor
            self.player_shoot_point(Vector2(self.event_e.input.mouse_pos[0],
                                    self.event_e.input.mouse_pos[1]))
        else:
            self.shoot_count = 0
        
        if self.event_e.input.keys[K_w] == True:
            # Move up
            p_move_y -= self.player_speed

        elif self.event_e.input.keys[K_s] == True:
            # Move down
            p_move_y += self.player_speed
        
        if self.event_e.input.keys[K_a] == True:
            # Move left
            p_move_x -= self.player_speed
            
        elif self.event_e.input.keys[K_d] == True:
            # Move right
            p_move_x += self.player_speed
        
        self.player.rotate_to_face_point(Vector2(
                self.event_e.input.mouse_pos[0], 
                self.event_e.input.mouse_pos[1]))
        
        self.beh_e.update(self.enemies, self.player, self.screen)
        
        self.player.move(p_move_x, p_move_y, self.screen)
        
        self.bullet_update()
        
        
        if len(self.enemies) > 1:
            self.rep()
        elif len(self.enemies) == 0 and self.score > 0:
            self.game_over()
        #else:
            #self.spawn(4)
        
        self.collide()
        
        self.clock.tick(self.FPS)

    def score_inc(self, pts):
        self.score += 50*pts
        sc = self._hud.get("Score")
        if sc is not None:
            sc.text = "score "+str(self.score)
        if self.score > self.high_score:
            self.high_score = self.score
            hsc = self._hud.get("HighScore")
            if hsc is not None:
                hsc.text = "high score "+str(self.high_score)
                
    def reset_score(self):
        print "SCORE RESET FROM", self.score
        self.score = 0
        sc = self._hud.get("Score")
        if(sc is not None):
            sc.text = "score "+str(self.score)        
    
    def collide(self):
        dead_enemies = []
        dead_bullets = []
        for e in self.enemies:
            for b in self.bullets:
                if e.point_inside(Vector2(b.x, b.y)): 
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
        
        for p in self.player.points:
            for e in self.enemies:
                if e.point_inside(p+Vector2(self.player.x, self.player.y)):
                    self.game_over()
                    
    def draw(self):
        self.draw_e.begin_draw(pygame.Color(0,0,0))
        self.draw_e.draw(self.enemies)
        self.draw_e.draw(self.bullets)
        self.draw_e.draw([self.player])
        self.draw_e.draw([self._hud])
        self.draw_e.end_draw()
        
    def run(self):
        self._hud.add(HUDPolygon("Box1", pygame.Color(255, 255, 255),
                                  ((50, 50), (750, 50), 
                                  (750, 550), (50, 550), 2)))
        self._hud.add(HUDText("Score", pygame.Color(255, 255, 255),
                               "score "+str(self.score), (15, 20), 1, 2))
        self._hud.add(HUDText("HighScore", pygame.Color(255, 255, 255),
                               "high score "+str(self.high_score), (15, 575), 
                               1, 2))
        """
        self._hud.add(hud_line("Y", pygame.Color(255, 0, 255), 
                               ((400, 0), (400, 600), 2)))
        self._hud.add(hud_line("X", pygame.Color(255, 0, 255), 
                               ((0, 300), (800, 300), 2)))
        
        
        self._hud.add(hud_text("A1", pygame.Color(255, 255, 0), 
                               "abcdefghijk", (400, 300), 1, 2))
        self._hud.add(hud_text("A2", pygame.Color(255, 255, 0), 
                               "lmnopqrs", (400, 350), 1, 2))
        self._hud.add(hud_text("A2", pygame.Color(255, 255, 0), 
                               "tuvwxyz", (400, 400), 1, 2))
        self._hud.add(hud_text("A2", pygame.Color(255, 255, 0), 
                               "0123456789", (400, 450), 1, 2))
        """
        self.spawn(4)
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
        elif len(self.enemies) < 2:
            self.spawn(2)
        self.rep_count += 1
        #print self.rep_count

    def bullet_update(self):
        for b in self.bullets:
            if b.x > 800 or b.x < 0 or b.y > 600 or b.y < 0:
                self.bullets.remove(b)
            b.move()

    def player_shoot_dir(self, direction):
        if self.shoot_count % self.shoot_interval == 0:
            b = BulletD(self.player.x, self.player.y, direction)
            self.bullets.append(b)
        self.shoot_count += 1

    def player_shoot_point(self, point):
        if self.shoot_count % self.shoot_interval == 0:
            b = BulletP(self.player.x, self.player.y, point)
            self.bullets.append(b)
        self.shoot_count += 1