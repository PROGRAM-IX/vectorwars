from pystroke.behaviour import Behaviour
from pystroke.vector2 import Vector2
import math
from random import randint

class FollowBeh(Behaviour):
    
    def __init__(self):
        Behaviour.__init__(self, 'follow')
    
    def process(self, enemy, player, surface, chance):
        if (randint(0, 100) < chance 
        and enemy.distance_to(Vector2(player.x, player.y)) > 100-chance):
            e_pos = enemy.dir_vec()
            p_pos = Vector2(player.x, player.y)
            v = e_pos - p_pos
            angle = math.atan2(v.x, v.y)
            #enemy.rotate_by_radians(angle)
            enemy.move_rel(-v.normalised().x * 3, -v.normalised().y * 3, surface)

class AvoidBeh(Behaviour):
    
    def __init__(self):
        Behaviour.__init__(self, 'avoid')
    
    def process(self, enemy, player, surface, chance):
        if (randint(0, 100) < chance 
        and enemy.distance_to(Vector2(player.x, player.y)) < 100-chance):
            e_pos = enemy.dir_vec()
            p_pos = Vector2(player.x, player.y)
            v = e_pos - p_pos
            angle = math.atan2(v.x, v.y)
            #enemy.rotate_by_radians(angle)
            enemy.move_rel(v.normalised().x * 3, v.normalised().y * 3, surface)
        
class GroupBeh(Behaviour):
    
    def __init__(self):
        Behaviour.__init__(self, 'group')
        
    def process(self, enemies, player, surface):
        for e in enemies:
            for f in enemies:
                if e is not f:
                    dist = e.distance_to(Vector2(f.x, f.y))
                    if dist < 50:
                        print "Colliding"
                        v = (Vector2(e.x, e.y)-Vector2(f.x, f.y)).normalised()
                        print v
                        e.move_rel(v.x * dist/20, v.y * dist/20, surface)
        