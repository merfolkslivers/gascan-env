import attr


@attr.s
class Card:
    # Human-readable, ideally.
    # One day we might have to switch to object representation for fast equality.
    name = attr.ib()

    # Numeric ID, in case we decide to move to internationalization of cards.
    id = attr.ib()

    # Red/Goblin (MTG), Hero/Coral (CFV), Spellcaster/Dragonmaid (YGO)
    # Used for fast lookup by other effects, for eligibility purposes e.g. "if the revealed card is a..."
    tagdict = attr.ib(default=set())

    # Event listeners for effects.
    # e.g. Planeswalker abilities, ACT/AUTO/CONT in CFV, or individual skill line items in YGO/MTG.
    # Ones added to individual card instances are done at the CardInstance level.
    # e.g. "Equipped creature gains...",
    listeners = attr.ib(default=set())

    # Primitive value storage e.g. P/T/mana cost (MTG), Grade (CFV), Rank (YGO).
    aspects = attr.ib(default=dict())

