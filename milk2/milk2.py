"""
ID: kendotz1
LANG: PYTHON3
TASK: milk2
"""

from io import TextIOBase

fin = open("milk2.in", "r")
fout = open('milk2.out', 'w')


def read_bands_from_file(file: TextIOBase) -> list:
    collected = []
    for x in range(farmers):
        band = file.readline().strip().split(" ")
        band[0] = int(band[0])
        band[1] = int(band[1])
        collected.append(band)
    print(farmers, collected)
    return collected


def sort_by_start_asc_and_end_desc(_bands: list) -> list:
    _bands.sort(key=lambda a: a[0])
    _bands.sort(key=lambda a: (1000000 - a[0]) * 10000000 + a[1], reverse=True)
    return _bands


def merge_bands_from_index(band1, band2) -> tuple:
    merged = [None, None]
    merged[0] = min(band1[0], band2[0])
    merged[1] = max(band1[1], band2[1])
    return merged


def handle_bands(band1, band2) -> list:
    global longest_milking
    global longest_idle
    if band1 is None or band2 is None:
        return None

    if band1[0] == band2[0]:  # same start, earlier finish
        return [band1]  # discard
    if band2[0] > band1[0] and band2[0] <= band1[1]:  # different start, fits in first band
        if band2[1] <= band1[1]:  # fits within first band
            return [band1]  # discard
        else:
            return [merge_bands_from_index(band1, band2)]  # merge bands, band 2 extends out
    gap = band2[0] - band1[1]
    if gap > longest_idle:
        longest_idle = gap

    return [band1, band2]


longest_milking = 0
longest_idle = 0

farmers = int(fin.readline())
bands = read_bands_from_file(fin)
sorted_bands = sort_by_start_asc_and_end_desc(bands)
print(sorted_bands)

merged_bands = []
i = 0
band = None
while i < len(sorted_bands):
    band = sorted_bands[i]
    merged_band = None
    t = len(sorted_bands) - i
    if i > len(sorted_bands) - 2:
        merged_bands.append(band)
        break

    for j in range(t):
        if i + j + 1 > len(sorted_bands) - 1:
            merged_bands.append(band)
            i += j + 1
            break
        compared = handle_bands(band, sorted_bands[i+j+1])
        if compared is None:
            merged_bands.append(band)
            i += j + 1
            break
        if len(compared) == 1:  # discard smaller band or merge
            band = compared[0]
            continue
        else:  # gap, new band, move on
            band = compared[0]
            merged_bands.append(band)
            i += j + 1
            break

for _band in merged_bands:
    if _band[1] - _band[0] > longest_milking:
        longest_milking = _band[1] - _band[0]

fout.write(str(longest_milking) + " " + str(longest_idle) + "\n")
fout.close()
print(merged_bands)
