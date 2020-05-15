# Used for managing discrete/unique elements on a card:
# Keywords (Hollow, Melody, Goblin)

class CardTag:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.descr = kwargs['descr']
