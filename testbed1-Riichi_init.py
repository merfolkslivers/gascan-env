from collections import deque
from csv import DictReader

from boardobj.Card import Card
from boardobj.CardInstance import CardInstance
from boardobj.OrderedZone import OrderedZone
from boardobj.UnorderedZone import UnorderedZone

# Create a wall of Riichi Mahjong tiles, shuffle it, then deal a hand of 12.
# Also includes basic uniqueness tests (136 tiles in Riichi, and we don't create tile references out of thin air).

tiles = []
with open('riichi.csv', encoding='utf-8') as f:
    for row in DictReader(f):
        key = int(row["id"])
        name = row["subtype"] + '-' + row["value"]
        c = Card(
            name=name,
            id=key,
            aspects={k: row[k] for k in ('type', 'subtype', 'value')}
        )
        for _ in range(4):
            ci = CardInstance(
                card=c,
                faceup=False
            )
            tiles.append(ci)
wall = OrderedZone(
    cardlist=deque(tiles)
)
wall.shuffle()
hand = UnorderedZone(
    cardlist=set(wall.draw(12))
)
wallsize = len(wall.cardlist)
handsize = len(hand.cardlist)
print(handsize)
print(wallsize)
print(handsize + wallsize)
print(len(hand.cardlist.intersection(wall.cardlist)))
print(hand.cardlist)
