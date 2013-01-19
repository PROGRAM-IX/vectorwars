from vw_behaviour import FollowBeh, AvoidBeh
from pystroke.behaviour_engine import BehaviourEngine

class VWBehaviourEngine(BehaviourEngine):
    def __init__(self, beh_dict={'follow': FollowBeh(), 'avoid': AvoidBeh()}):
        BehaviourEngine.__init__(self, beh_dict)
        
    def update(self, enemies, player, surface):
        for e in enemies:
            for b in e.beh:
                beh = self.beh_dict.get(b)
                beh.process(e, player, surface, e.beh[b])    
                