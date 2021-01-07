"""
ID: kendotz1
LANG: PYTHON3
TASK: dualpal
"""

from io import TextIOBase

fin = open('dualpal.in', 'r')
fout = open('dualpal.out', 'w')

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


"""
1 <= n <= 15
0 < s < 1000

find the first n numbers > s that are palindromes in two bases (2 <= base <= 10)
"""

line = fin.readline().strip().split(" ")
n = int(line[0])
s = int(line[1])

collected = []
i = 1
while len(collected) < n:
    palindromic_bases = 0
    for base in range(2, 11):
        if is_palindromic(str(int_to_base(s + i, base))):
            palindromic_bases += 1
            if palindromic_bases >= 2:
                collected.append(s + i)
                break
    i += 1

for num in collected:
    fout.write(str(num) + '\n')
fout.close()
