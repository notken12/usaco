"""
ID: kendotz1
LANG: PYTHON3
TASK: transform
"""

from io import TextIOBase

fin = open('transform.in', 'r')
fout = open('transform.out', 'w')


def read_square(file: TextIOBase, n: int) -> list:
    square = []
    # 2d array construct
    for i in range(n):
        line = fin.readline().strip()
        square.append([char for char in line])
    return square


def construct_square_array(size):
    mapped = []
    # construct array of same dimensions
    for y in range(size):
        row = []
        for x in range(size):
            row.append(None)
        mapped.append(row)
    return mapped


def get_origin(size):
    return (size - 1.0) / 2.0


def square_to_str(square: list) -> str:
    _str = ""
    for row in square:
        for tile in row:
            _str += tile
        _str += "\n"
    return _str


def map_90_deg_rotation(square: list) -> list:  # 1
    size = len(square)
    mapped = construct_square_array(size)

    # map transformation
    # y, x -> x, -y
    origin = get_origin(size)
    for y in range(size):
        for x in range(size):
            cy, cx = int(-(y-origin)+origin), x

            mapped[cx][cy] = square[y][x]
    return mapped


def map_180_deg_rotation(square: list) -> list:  # 2
    size = len(square)
    mapped = construct_square_array(size)

    # map transformation
    # y, x -> -y, -x
    origin = get_origin(size)
    print(origin)
    for y in range(size):
        for x in range(size):
            cy, cx = int(-(y-origin)+origin), int(-(x-origin)+origin)

            mapped[cy][cx] = square[y][x]
    return mapped


def map_270_deg_rotation(square: list) -> list:  # 3
    size = len(square)
    mapped = construct_square_array(size)

    # map transformation
    # y, x -> -x, y
    origin = get_origin(size)
    print(origin)
    for y in range(size):
        for x in range(size):
            cy, cx = y, int(-(x - origin) + origin)

            mapped[cx][cy] = square[y][x]
    return mapped


def map_horizontal_reflection(square: list) -> list:  # 4
    size = len(square)
    mapped = construct_square_array(size)

    # map transformation
    # y, x -> y, -x
    origin = get_origin(size)
    print(origin)
    for y in range(size):
        for x in range(size):
            cy, cx = y, int(-(x - origin) + origin)

            mapped[cy][cx] = square[y][x]
    return mapped

mapping_funcs = [None, map_90_deg_rotation, map_180_deg_rotation, map_270_deg_rotation, map_horizontal_reflection]


"""
#5: combination, reflection + any rotation
#6: no change
#7: invalid transformation (none of the transformations were used)
"""


n = int(fin.readline())

sq1 = read_square(fin, n)
sq2 = read_square(fin, n)

print(square_to_str(sq1))
print(square_to_str(map_horizontal_reflection(sq1)))

result = 7

for x in range(1, 7):
    if 1 <= x <= 4:
        if mapping_funcs[x](sq1) == sq2:
            result = x
            break
    elif x == 5:  # combination (reflection + any rotation)
        reflected = map_horizontal_reflection(sq1)
        success = False
        for y in range(1, 4):
            if mapping_funcs[y](reflected) == sq2:
                success = True
                break
        if success:
            result = x
            break
    elif x == 6:
        if sq1 == sq2:
            result = x
            break

fout.write(str(result) + '\n')
fout.close()
