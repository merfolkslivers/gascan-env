# gascan-env
Discrete-time CCG/TCG simulation/development library

## specs


## but why
Anything, really:
* Monte Carlo simulation seeing if [Frank](https://www.channelfireball.com/all-strategy/articles/magic-math-hogaak-can-be-played-on-turn-2-in-60-of-its-games/) underestimated how busted [Hogaak](https://scryfall.com/card/mh1/202/hogaak-arisen-necropolis) is
* Trying to ML a decklist that makes [Tsuk Standard](https://cardfight.fandom.com/wiki/Goddess_of_the_Full_Moon,_Tsukuyomi_(V_Series)) actually work
* Extend this and build your own TCG backend!

## but how
~~Nanomachines, son.~~
### Implemented
* Super-generic objects for representing board/hand state.

### TODO:
* Event bus that manages dynamic/stackable game logic e.g. [Panharmonicon](https://scryfall.com/card/kld/226/panharmonicon) storm
* Support for (un)marshalling and (un)pickling to various data representations in support of AI applications (read: gascan-ai at a later date)
* LALR support to represent and implement game logic in filthy casuals-readable format

## but why "gascan"
Because [cute robot gascan](https://azurlane.koumakan.jp/Gascogne) wants to be the very best, [but never was](https://en.wikipedia.org/wiki/Richelieu-class_battleship#Clemenceau_and_Gascogne)

(by the way, [Frank](https://twitter.com/karsten_frank/) you are my hero)

(All product names, logos, and brands, game mechanics, card names, general references, etc. contained within are property of their respective owners. All company, product, service names, game mechanics, card names, etc. used in this code are for identification purposes only. Use and reference of these properties does not imply endorsement.)
