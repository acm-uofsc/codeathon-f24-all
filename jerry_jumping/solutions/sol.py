import sys
import re
x = int(input())
s = int(input())
tiles = [int(tile) for tile in input().split()]
assert len(tiles) == x
pos = 0
for i in range(s):
    pos += 1
    if pos == len(tiles):
        pos = 0
    elif tiles[pos] == 0:
        tiles[pos] = 5
        pos = 0
    # print(f"after move {i+1}:", file=sys.stderr)
    # print(*tiles, file=sys.stderr)
    # for j in range(x):
    #     if j == pos:
    #         print("^", file=sys.stderr, end='')

    #     print(re.sub(r"\d", " ", str(tiles[j])), end=' ', file=sys.stderr)
    # print(file=sys.stderr)
print(tiles[pos])