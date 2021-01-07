"""
ID: kendotz1
LANG: PYTHON3
TASK: milk
"""

from io import TextIOBase

fin = open('milk.in', 'r')
fout = open('milk.out', 'w')


def collect_farmer_data(file: TextIOBase, count: int) -> list:
    _farmers = []
    for i in range(count):
        line = file.readline().strip().split(' ')
        _farmers.append([int(line[0]), int(line[1])])
    return _farmers


def sort_cost_asc(_farmers: list) -> list:
    _farmers.sort(key=lambda e: e[0])
    return _farmers


line1 = fin.readline().strip().split(' ')
units_needed = int(line1[0])
farmer_count = int(line1[1])

farmers = sort_cost_asc(collect_farmer_data(fin, farmer_count))
total_cost = 0

x = 0
while x < farmer_count and units_needed > 0:
    """
    buy milk until we reach the units_needed
    """
    farmer = farmers[x]
    price = farmer[0]
    stock = farmer[1]
    if stock > units_needed:  # more stock than remaining units needed
        total_cost += price * units_needed
        units_needed = 0
        break
    else:
        total_cost += price * stock
        units_needed -= stock
    x += 1

fout.write(str(total_cost) + '\n')
fout.close()
