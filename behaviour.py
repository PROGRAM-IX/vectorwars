from vector2 import Vector2
import math
from random import randint

class Behaviour:
    
    def process(self, enemy):
        print "Processing", enemy
        pass
    
class FollowBeh(Behaviour):
    
    def __init__(self):
        self.name = 'follow'
    
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
        self.name = 'avoid'
    
    def process(self, enemy, player, surface, chance):
        if randint(0, 100) < chance:
            e_pos = enemy.dir_vec()
            p_pos = Vector2(player.x, player.y)
            v = e_pos - p_pos
            angle = math.atan2(v.x, v.y)
            #enemy.rotate_by_radians(angle)
            enemy.move(v.normalised().x * 5, v.normalised().y * 5, surface)
        
        