"""
ID: kendotz1
LANG: PYTHON3
TASK: wormhole
"""

from io import TextIOBase
from itertools import permutations, combinations
import math

fin = open('wormhole.in', 'r')
fout = open('wormhole.out', 'w')


class Coordinate(object):
    """Instances of the wormhole instances"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.paired = None

    def __repr__(self): # for debugging # may be better to subclass from tuple
        return '(' + str(self.x) + ', ' + str(self.y) + ')'


def pair_coordinates(p):
    c1, c2 = p[0], p[1]
    c1.paired = c2
    c2.paired = c1


def get_wormholes_from_file(file: TextIOBase, n: int) -> list:
    _wormholes = []
    for x in range(n):
        x, y = map(int, file.readline().split())
        _wormholes.append(Coordinate(x, y))
    _wormholes.sort(key=lambda e: e.x)
    return _wormholes


def different(p1, p2):
    if p1[0] in p2 or p1[1] in p2:
        return False
    return True


def get_wormhole_pairings(set_of_wh):
    l = list(set_of_wh)

    if len(l) == 2:
        # last pairing
        return [[(l[0], l[1])]]

    result = []
    i = 0
    for j in range(1, len(set_of_wh)):
        others = get_wormhole_pairings(set_of_wh - {l[i], l[j]})
        pair = [[(l[i], l[j])] + other for other in others]
        result += pair
    return result


def is_loop(_pairing: list, _wormholes: list) -> bool:
    for wh in _wormholes:
        cow = Coordinate(wh.x, wh.y)
        # move +x
        for step in range(len(_wormholes) - 1):
            wormholes_to_the_right = [w for w in _wormholes if w.x > cow.x and w.y == cow.y]
            if not wormholes_to_the_right:
                break
            wormholes_to_the_right.sort(key=lambda a: a.x)
            first = wormholes_to_the_right[0]  # get first wormhole to the right
            out = first.paired  # get corresponding exit portal
            cow = Coordinate(out.x, out.y)  # tp cow
            if cow.x == wh.x and cow.y == wh.y:  # loop!
                return True
    return False


wormhole_count = int(fin.readline().strip())
wormholes = get_wormholes_from_file(fin, wormhole_count)
print(wormholes)


"""
bessie the cow always moves in +x direction

get possible combinations of wormholes,
then teleport bessie into each wormhole and iterate thru each step
to test if she loops

d c
a b
(a c) (b d)
tp bessie to b
exits thru d
tp into first wormhole to the right (c) (move cow)
exits thru a
tp into first wormhole to the right (b) (move cow)

b -> d -> c -> a -> b
"""

pairings = get_wormhole_pairings(set(wormholes))

looping_pairings = 0

for pairing in pairings:
    # do stuffs
    for pair in pairing:
        pair_coordinates(pair)

    if is_loop(pairing, wormholes):
        looping_pairings += 1

fout.write(str(looping_pairings) + '\n')
fout.close()
