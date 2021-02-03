"""
ID: kendotz1
LANG: PYTHON3
TASK: ariprog
"""

from io import TextIOBase
import math


# from M we will know the upper bound of the bi-squares (M**2 * 2), we refer to it as Mx
# becase a>=0, b>0, and v = a + n*b
# from N we will know the uppoer bounds of all possible a, and b.

# knowing M we can compute all the unique bi-squares


def bisquares(m: int):
    for p in range(m + 1):
        for q in range(m + 1):
            yield p ** 2 + q ** 2


fin = open('ariprog.in', 'r')
fout = open('ariprog.out', 'w')

N = int(fin.readline())
M = int(fin.readline())

print(N, M)

bisquare_set = frozenset(bisquares(M))  # optimization 1: handle unqiue bi-squares only
Mx = M ** 2 * 2
found = []


def get_b_range_given_n_and_mx(start_val, n, mx):
    return range(1, math.floor((mx - start_val) / (n - 1)) + 1)


def check(n, start_val, step, bsset):
    if n > 2:
        bsset = set([a for a in bsset if start_val <= a <= start_val + (n - 1) * step])

    for i in range(n):
        if not start_val + i * step in bsset:
            return

    found.append([start_val, step])


iterations = 0

for bs in bisquare_set:
    for b in get_b_range_given_n_and_mx(bs, N, Mx):
        iterations += 1
        check(N, bs, b, bisquare_set)

print(iterations, len(bisquare_set))
found.sort(key=lambda a: a[1])

for f in found:
    fout.write(f"{f[0]} {f[1]}\n")

if len(found) == 0:
    fout.write('NONE\n')

fout.close()
