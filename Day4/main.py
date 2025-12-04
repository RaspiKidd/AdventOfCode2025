def getRolls(lines):
    result = []
    for y in range(1, len(lines)-1):
        for x in range(1, len(lines[0])-1):
            if lines[y][x] == '@':
                adjacent = 0
                adjacent += 1 if lines[y-1][x-1] == '@' else 0
                adjacent += 1 if lines[y-1][x] == '@' else 0
                adjacent += 1 if lines[y-1][x+1] == '@' else 0
                adjacent += 1 if lines[y][x-1] == '@' else 0
                adjacent += 1 if lines[y][x+1] == '@' else 0
                adjacent += 1 if lines[y+1][x-1] == '@' else 0
                adjacent += 1 if lines[y+1][x] == '@' else 0
                adjacent += 1 if lines[y+1][x+1] == '@' else 0
                if adjacent < 4:
                    result.append([y,x])
    return result

def solve(part):
    total = 0
    with open('input.txt', "r") as f:
        lines = [['.'] + list(line.strip()) + ['.'] for line in f]
        lines.insert(0, ['.'] * len(lines[0]))
        lines.append(['.'] * len(lines[0]))

        while True:
            rolls = getRolls(lines)
            total += len(rolls)
            if part == 1 or len(rolls) == 0:
                break
            for roll in rolls:
                lines[roll[0]][roll[1]] = '.'
    print(total)
#solve(part=1)
solve(part=2)