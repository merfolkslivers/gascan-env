# I *guess* it's an area of board state that gets shared by one or more players.
# Right now, I'm designing it for a single player since most CCGs are built with the minimum of
# moving cards between players.

import attr

@attr.s
class BoardArea:
    # Data structure of zones that are relevant to the player.
    # By default, I'm expecting a dict.
    zones: dict = attr.ib(default=dict())

    # Function and regex. Run through the zones that match the types and any name requirement and filter out cards
    # that match the filter function.
    # I'm not removing the cards. We handle that in whatever called this.
    # cardfilterfunction is a boolean return.
    def filtercards(self, cardfilterfunction, zonenamelist, onlyfaceup=False):
        zones = [
           self.zones[x] for x in self.zones.keys() if x in zonenamelist
        ]
        if not zones:
            return None
        cardlist = []
        for zone in zones:
            cardlist.extend([
                x for x in zone.cardlist if (not onlyfaceup or x.faceup) and cardfilterfunction(x) is True
            ])
        return cardlist

    # This version will throw an error if you try to add a Zone when one exists by that name already.
    def addzone(self, zone, zonename):
        if zonename not in self.zones.keys():
            self.zones.update({zonename, zone})
        else:
            raise ValueError("Attempting to add duplicate zone named: " + zonename)

    # I leave any zone merging shenanigans to the implementing SkillEffect.
    # Having a prescribed method in this class is asking for workarounds.
