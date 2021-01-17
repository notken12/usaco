"""
ID: kendotz1
LANG: PYTHON3
TASK: ariprog
"""

from io import TextIOBase
import math


def bisquares():
    for p in range(bisquare_limit + 1):
        for q in range(bisquare_limit + 1):
            yield p ** 2 + q ** 2


def check(a, b):
    for j in range(prog_length):
        if not a + j * b in bisquare_set:
            return
    found.append([a, b])


def diffs(_bisquares):
    prev = None
    d = {}
    for s in _bisquares:
        if prev is not None:
            d[s - prev] = True
        prev = s
    return d


fin = open('ariprog.in', 'r')
fout = open('ariprog.out', 'w')

prog_length = int(fin.readline())
bisquare_limit = int(fin.readline())

print(prog_length, bisquare_limit)

bisquare_set = list(bisquares())
bisquare_set.sort()

bisquare_count = len(bisquare_set)
largest_bisquare = max(bisquare_set)

gaps = diffs(bisquare_set)
print(len(bisquare_set), gaps)
print(bisquare_set)

found = []
for y in gaps:
    for x in bisquare_set:
        check(x, y)

found.sort(key=lambda a: a[1])

for f in found:
    fout.write(str(f[0]) + ' ' + str(f[1]) + '\n')

if len(found) == 0:
    fout.write('NONE\n')

fout.close()
