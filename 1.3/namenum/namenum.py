"""
ID: kendotz1
LANG: PYTHON3
TASK: namenum
"""

from io import TextIOBase

fin = open('namenum.in', 'r')
fout = open('namenum.out', 'w')

serial = fin.readline().strip()

fnames = open('dict.txt', 'r')
names = fnames.read().splitlines()

keypad_mapping = [None, None, 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PRS', 'TUV', 'WXY']


def sort_names_by_length(_names: list, length: int) -> list:
    return [n for n in _names if len(n) == length]


def sort_names_by_letters_at(_names: list, letters: str, index: int) -> list:
    letters_list = [char for char in letters]
    return [n for n in _names if n[index] in letters_list]


# print(sort_names_by_start_letters(sort_names_by_length(names, 5), "GJE"))
# find all 5 letter names that start with G,J, or E

sorted_length = sort_names_by_length(names, int(len(serial)))

final_sort = sorted_length

for x in range(len(serial)):
    final_sort = sort_names_by_letters_at(final_sort, keypad_mapping[int(serial[x])], x)
    if not final_sort:
        break

if not final_sort:
    fout.write("NONE\n")
    fout.close()
else:
    for name in final_sort:
        fout.write(name + "\n")
    fout.close()
