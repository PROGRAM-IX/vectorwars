from behaviour import *

class BehaviourEngine:
    def __init__(self, beh_dict={'follow': FollowBeh()}):
        self.beh_dict = beh_dict
        
    def update(self, enemies, player, surface):
        for e in enemies:
            for b in e.beh:
                beh = self.beh_dict.get(b)
                beh.process(e, player, surface)    
                    