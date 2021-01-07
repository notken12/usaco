"""
ID: kendotz1
LANG: PYTHON3
TASK: palsquare
"""

from io import TextIOBase
import string

digs = string.digits + string.ascii_letters


def int_to_base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[int(x % base)].upper())
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)


def get_reverse(s: str) -> str:
    return s[::-1]


def is_palindromic(_n: str) -> bool:
    reversed_n = get_reverse(str(_n))
    return reversed_n == str(_n)


fin = open('palsquare.in', 'r')
fout = open('palsquare.out', 'w')

base = int(fin.readline().strip())

for n in range(1, 301):
    n_squared_in_base = str(int_to_base(n**2, base))
    if is_palindromic(n_squared_in_base):
        fout.write(str(int_to_base(n, base)) + " " + n_squared_in_base + '\n')

fout.close()
