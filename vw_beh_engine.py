from vw_behaviour import FollowBeh, AvoidBeh, GroupBeh
from pystroke.behaviour_engine import BehaviourEngine

class VWBehaviourEngine(BehaviourEngine):
    def __init__(self, beh_dict={'follow': FollowBeh(), 'avoid': AvoidBeh(),
                                 'group': GroupBeh(50, 2)}):
        BehaviourEngine.__init__(self, beh_dict)
        self.tick_count = 1
        
    def update(self, enemies, player, surface):
        if self.tick_count % 2 == 0:
            beh = self.beh_dict.get('group')
            beh.process(enemies, surface)        
        self.tick_count += 1
        for e in enemies:
            for b in e.beh:
                beh = self.beh_dict.get(b)
                beh.process(e, player, surface, e.beh[b])    