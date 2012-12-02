from vector2 import vector2
import math

class Behaviour:
    
    def process(self, enemy):
        print "Processing", enemy
        pass
    
class FollowBeh:
    
    def __init__(self):
        self.name = 'follow'
    
    def process(self, enemy, player, surface):
        e_pos = enemy.dir_vec()
        p_pos = vector2(player.x, player.y)
        v = e_pos - p_pos
        angle = math.atan2(v.x, v.y)
        #enemy.rotate_by_radians(angle)
        enemy.move(-v.normalised().x * 5, -v.normalised().y * 5, surface)
        
        