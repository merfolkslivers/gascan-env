# The entry hook for all skills. Basically a Listener that puts a Skill on the Standby List when triggered.
# It can be manually triggered e.g. ACT/activated abilitities, or it can have a conditional trigger that this will
# listen to e.g. if event.type == ATTACK and event.origin = self.gamecard to represent "When this unit attacks".

#
from abc import ABC, abstractmethod


class SkillTrigger(ABC):

    @abstractmethod
    def checkevent(self, event):
        # This should inspect relevant details of the Event. Basically, the listener function.
        pass