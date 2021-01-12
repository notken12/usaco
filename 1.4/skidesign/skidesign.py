"""
ID: kendotz1
LANG: PYTHON3
TASK: skidesign
"""

from io import TextIOBase
import math

fin = open('skidesign.in', 'r')
fout = open('skidesign.out', 'w')


def get_slopes_from_file(file: TextIOBase, c: int) -> list:
    result = []
    for i in range(c):
        result.append(int(file.readline().strip()))
    result.sort()
    return result


def get_min_max_slopes(_slopes: list) -> list:
    return [min(*_slopes), max(*_slopes)]


def get_difference_of_min_max(_slopes: list) -> int:
    minmax = get_min_max_slopes(_slopes)
    return minmax[1] - minmax[0]


def get_target_range(_slopes: list) -> list:
    d = get_difference_of_min_max(_slopes)
    minmax = get_min_max_slopes(_slopes)
    #minmax = [43, 60]
    avg = (minmax[0] + minmax[1]) / 2
    avg = sum(_slopes) / len(_slopes)
    # avg = sum(slopes) / len(slopes)
    if d - 17 <= 0:
        return get_min_max_slopes(_slopes)
    if d % 1 == 0:
        return [int(avg) - 9, int(avg) + 8]
    else:
        return [int(avg) - 9, int(avg) + 8]


def adjust_slopes_to_range(_slopes: list, _range: list) -> list:
    result = []
    for slope in _slopes:
        if slope < _range[0]:
            result.append(_range[0])
        elif slope > _range[1]:
            result.append(_range[1])
        else:
            result.append(slope)
    return result


def get_cost(_slopes: list, _adjusted: list) -> int:
    result = 0
    for i in range(len(_slopes)):
        result += abs(_slopes[i] - _adjusted[i]) ** 2
    return result


slope_count = int(fin.readline().strip())

slopes = get_slopes_from_file(fin, slope_count)


"""
test possible price ranges
"""
cheapest = None
minmax = get_min_max_slopes(slopes)

for r in range(0, max(slopes) - 16):
    price = get_cost(slopes, adjust_slopes_to_range(slopes, [r, r + 17]))
    if cheapest is None:
        cheapest = price
    elif price < cheapest:
        cheapest = price

fout.write(str(cheapest) + '\n')
fout.close()
