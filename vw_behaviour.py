from pystroke.behaviour import Behaviour
from pystroke.vector2 import Vector2
import math
from random import randint

class FollowBeh(Behaviour):
    
    def __init__(self):
        Behaviour.__init__(self, 'follow')
    
    def process(self, enemy, player, surface, chance):
        if randint(0, 100) < chance:
            e_pos = enemy.dir_vec()
            p_pos = Vector2(player.x, player.y)
            v = e_pos - p_pos
            angle = math.atan2(v.x, v.y)
            #enemy.rotate_by_radians(angle)
            enemy.move(-v.normalised().x * 5, -v.normalised().y * 5, surface)

class AvoidBeh(Behaviour):
    
    def __init__(self):
        Behaviour.__init__(self, 'avoid')
    
    def process(self, enemy, player, surface, chance):
        if randint(0, 100) < chance:
            e_pos = enemy.dir_vec()
            p_pos = Vector2(player.x, player.y)
            v = e_pos - p_pos
            angle = math.atan2(v.x, v.y)
            #enemy.rotate_by_radians(angle)
            enemy.move(v.normalised().x * 5, v.normalised().y * 5, surface)
        
        