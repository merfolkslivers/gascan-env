import attr


# Instance of a card on board.
@attr.s(eq=False) # No, mi tarjeta no es su tarjeta.
class CardInstance:
    # Card that this instance is based on.
    card = attr.ib()

    faceup = attr.ib()

    # Where you put "This card gains..." SkillTriggers.
    # Remember to put these on the Bus.
    extratriggers = attr.ib(default=set())

    # Where you put "This card gains..." effects e.g. P/T boosts (MTG).
    effects = attr.ib(default=set())

    #Extra objects, such as:
    # CFV: Divine Gauge, Equip Gauge.
    # MTG: Mutate stack, Attach pile.
    # YGO: Equip Cards (remember, don't remove them from the Spell Slots!), XYZ Material.
    objs = attr.ib(default=set())