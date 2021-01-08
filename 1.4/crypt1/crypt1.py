"""
ID: kendotz1
LANG: PYTHON3
TASK: crypt1
"""

from io import TextIOBase
import math

fin = open('crypt1.in', 'r')
fout = open('crypt1.out', 'w')


def read_possible_digits_from_file(file: TextIOBase, digit_count: int) -> list:
    return [int(a) for a in file.readline().strip().split(' ')]


def get_factor_pairs(_digits: list) -> list:
    pairs = []
    for digit in _digits:
        for i in range(n):
            if digit * _digits[i] in _digits:
                pairs.append([digit, _digits[i]])
    return pairs


def verify_cryptarithm(n1: int, n2: int, _digits: list):  # -> bool
    # fail if 5 digit result
    product = str(n1 * n2)
    if len(product) > 4:
        return False

    if not len([e for e in product if int(e) in _digits]) == len(product):
        return False  # mismatching digits in product

    # verify partial products
    p1 = str(n1 * (n2 % 10))  # p1 x p2's ones place
    p2 = str(n1 * (math.floor((n2 / 10) % 10)))  # p1 x p2's tens place

    if len(p1) > 3 or len(p2) > 3:
        return False  # partial product(s) too long

    # verify partial product digits
    if not len([e for e in p1 if int(e) in _digits]) == len(p1) or not len([e for e in p2 if int(e) in _digits]) == len(p2):
        return False  # mismatching digits in partial products
    return True


n = int(fin.readline().strip())
digits = read_possible_digits_from_file(fin, n)
digits.sort()
factor_pairs = get_factor_pairs(digits)
solution_count = 0

print(digits)
print(factor_pairs)

c = 0
"""
for pair in factor_pairs:
    
    test every possible cryptarithm with pair digits filled in
    
    for x in range(n):
        for y in range(n):
            for z in range(n):
                d1 = digits[x]
                d2 = digits[y]
                d3 = digits[z]
                f1, f2 = d1 * 100 + d2 * 10 + pair[0], d3 * 10 + pair[1]
                # print(d1, d2, pair[0], d3, pair[1], f1*pair[1], f1*d3, f1*f2, verify_cryptarithm(f1, f2, digits))

                if verify_cryptarithm(f1, f2, digits):
                    solution_count += 1
                    print(d1, d2, pair[0], d3, pair[1], f1*pair[1], f1*d3, f1*f2, verify_cryptarithm(f1, f2, digits))
                c += 1
"""

for a in range(n):
    for b in range(n):
        for x in range(n):
            for y in range(n):
                for z in range(n):
                    d1 = digits[x]
                    d2 = digits[y]
                    d3 = digits[z]
                    d4 = digits[a]
                    d5 = digits[b]
                    f1, f2 = d1 * 100 + d2 * 10 + d4, d3 * 10 + d5
                    # print(d1, d2, pair[0], d3, pair[1], f1*pair[1], f1*d3, f1*f2, verify_cryptarithm(f1, f2, digits))

                    if verify_cryptarithm(f1, f2, digits):
                        solution_count += 1
                        # print(d1, d2, d4, d3, d5, f1*d5, f1*d3, f1*f2, verify_cryptarithm(f1, f2, digits))
                    c += 1

print(str(c))
print(solution_count)
fout.write(str(solution_count) + '\n')
fout.close()
