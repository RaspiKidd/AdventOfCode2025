with open('input.txt') as f:
    tiles = f.read().splitlines()

tiles = tuple(
    tuple(int(i) for i in tile.split(','))
    for tile in tiles
    )

rows = {}
cols = {}
for i in range(len(tiles)):
    if tiles[i][0] == tiles[i-1][0]:
        cols[tiles[i][0]] = sorted(
            (tiles[i][1], tiles[i-1][1])
            )
    elif tiles[i][1] == tiles[i-1][1]:
        rows[tiles[i][1]] = sorted(
            (tiles[i][0], tiles[i-1][0])
            )
    else:
        print(f'Not lined up: {tiles[i]}, {tiles[i-1]}')

def extend(axis1, axis2):
    extendedAxis1 = {}
    index2 = sorted(axis2.keys())
    for x in sorted(axis1.keys()):
        start, end = axis1[x]
        inside = False
        for y in index2:
            if y == start:
                if inside:
                    start = prevCross
                break
            if axis2[y][0] < x < axis2[y][1]:
                inside ^= True
                prevCross = y

        inside = False
        for y in reversed(index2):
            if y == end:
                if inside:
                    end = prevCross
                break
            if axis2[y][0] < x < axis2[y][1]:
                inside ^= True
                prevCross = y
        extendedAxis1[x] = (start,end)
    return extendedAxis1

rows, cols = extend(rows, cols), extend(cols, rows)

part1 = 0
part2 = 0

for i in range(len(tiles)-1):
    for j in range(i+1,len(tiles)):
        xLow, xHi = sorted((tiles[i][0], tiles[j][0]))
        yLow, yHi = sorted((tiles[i][1], tiles[j][1]))
        area = (xHi-xLow+1)*(yHi-yLow+1)
        if area > part1:
            part1 = area

        if area > part2:
            contained = True
            contained &= rows[yLow][0] <= xLow
            contained &= xHi <= rows[yLow][1]
            contained &= rows[yHi][0] <= xLow
            contained &= xHi <= rows[yHi][1]
            contained &= cols[xLow][0] <= yLow
            contained &= yHi <= cols[xLow][1]
            contained &= cols[xHi][0] <= yLow
            contained &= yHi <= cols[xHi][1]
            if contained:
                part2 = area

print(f'{part1 = }')
print(f'{part2 = }')
