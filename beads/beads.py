"""
ID: kendotz1
LANG: PYTHON3
TASK: beads
"""

fin = open("beads.in", "r")
fout = open('beads.out', 'w')

length = int(fin.readline())
necklace = fin.readline().strip()

looped = necklace + necklace
max_collected = 0

for x in range(length):
    collected = 0

    # look left
    i = x - 1
    mode = "w"

    while i >= 0 and collected < length:
        bead = looped[i]
        if not bead == "w":
            if mode == "w" or mode == bead:
                mode = bead
                collected += 1
            else:
                break
        else:
            collected += 1

        i -= 1

    # look right
    i = x + 0
    mode = "w"
    while i < length * 2 and collected < length:
        bead = looped[i]
        if not bead == "w":
            if mode == "w" or mode == bead:
                mode = bead
                collected += 1
            else:
                break
        else:
            collected += 1

        i += 1

    if collected > max_collected:
        max_collected = collected


fout.write(str(max_collected) + "\n")
fout.close()
