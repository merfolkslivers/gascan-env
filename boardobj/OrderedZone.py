# Ordered stack of cards (e.g. Decks).
# The card list itself is deque if ordered, in order to support en masse bottom-decking.
# TODO: Do we necessarily need to be able to pickle/unpickle an RNG seed for shuffling?
import itertools
from collections import deque
import random
import attr

@attr.s
class OrderedZone:
    cardlist = attr.ib(default=deque())

    def draw(self, numcards=1):
        # Probably have to use this for peek top X operations as well. More often than not you're manipulating deck
        # order. In that case, use puttop/putbottom when you're done.
        result = []
        for _ in itertools.repeat(None, numcards):
            result.append(self.cardlist.pop())
        return result

    def puttop(self, cards):
        # 0th element goes on first.
        self.cardlist.extend(cards)

    def putbottom(self, cards):
        # extendleft reverses the input list before sticking it on.
        # It feels too wonky for me. Rather stick the stack on end to end.
        i = len(cards) - 1
        while i <= 0:
            self.cardlist.appendleft(cards[i])

    def shuffle(self):
        random.shuffle(self.cardlist)

    def insertundertop(self, cardlist, depth):
        # depth is number of card objects from the top.
        # TODO: Is this the fast way to do it? I heard insertion being a *pain* for deques.
        if depth < len(self.cardlist):
            temp = []
            tmpdepth = depth
            while tmpdepth > 0:
                temp.append(self.cardlist.pop())
                tmpdepth -= 1
            self.cardlist.extend(cardlist)
            while len(temp) > 0:
                self.cardlist.append(temp.pop())
        else:
            # I assume you put the cards on the bottom.
            self.putbottom(cardlist)
