from abc import ABC, abstractmethod


class SkillEffect(ABC):

    def __init__(self, **kwargs):
        self.nextTrigger = None  # SkillTrigger
        if kwargs['trigger']:
            self.nextTrigger = kwargs['trigger']

    @abstractmethod
    def executeeffect(self, **kwargs):
        pass

    def execute(self, **kwargs):
        events = self.executeeffect(kwargs)
        self.nextTrigger.checkEligibility(kwargs, events)
