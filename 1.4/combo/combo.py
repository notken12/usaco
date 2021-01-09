"""
ID: kendotz1
LANG: PYTHON3
TASK: combo
"""

from io import TextIOBase
import math

fin = open('combo.in', 'r')
fout = open('combo.out', 'w')


def fix_dial(d: int) -> int:
    if d < 1:
        return n + d
    if d > n:
        return d - n
    return d


def uniq(seq):
    # order preserving
    checked = []
    for e in seq:
        if e not in checked:
            checked.append(e)
    return checked


n = int(fin.readline().strip())
tolerance = min(n, 5)

farmer_combo = [int(a) for a in fin.readline().strip().split(' ')]
master_combo = [int(a) for a in fin.readline().strip().split(' ')]

possible_combos = []

lb = -min(n, 2)
ub = min(n, 2) + 1

for o1 in range(lb, ub):
    for o2 in range(lb, ub):
        for o3 in range(lb, ub):
            d1 = fix_dial(farmer_combo[0] + o1)
            d2 = fix_dial(farmer_combo[1] + o2)
            d3 = fix_dial(farmer_combo[2] + o3)
            possible_combos.append([d1, d2, d3])

            d1 = fix_dial(master_combo[0] + o1)
            d2 = fix_dial(master_combo[1] + o2)
            d3 = fix_dial(master_combo[2] + o3)
            possible_combos.append([d1, d2, d3])

possible_combos = uniq(possible_combos)

fout.write(str(len(possible_combos)) + '\n')
fout.close()
