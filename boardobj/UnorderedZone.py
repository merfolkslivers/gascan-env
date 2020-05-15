import attr


# Unordered set of cards (e.g. MTG creature area/land area).
# Also, use this for slot-style board zones e.g. CFV circles, YGO mob/spell zones.

@attr.s
class UnorderedZone:
    cardlist = attr.ib(default=set())  # If provided, a set of CardInstances that this instance contains.
    slotstyle = attr.ib(default=False)

    # As much as possible, I want to keep the card instances and the set inside this Zone the same.
    def replacecards(self, cardset=set()):
        outset = set()
        for e in self.cardlist:
            outset.add(e)
        self.cardlist.clear()
        for e in cardset:
            self.cardlist.add(e)
        return outset

    def addcard(self, cardinstance):
        if self.slotstyle is False:
            self.cardlist.add(cardinstance)
        else:
            raise ValueError("Attempted to add a card to a Slot Zone.")

    def addreplacecard(self, cardinstance):
        if self.slotstyle:
            outcard = self.cardlist.pop()
            self.cardlist.add(cardinstance)
            return outcard
        else:
            self.cardlist.add(cardinstance)

    def addall(self, cardset):
        if self.slotstyle:
            raise ValueError("Slot Zones don't support this operation.")
        # Pop still works, set or dict.
        while cardset:
            self.cardlist.add(cardset.pop())

