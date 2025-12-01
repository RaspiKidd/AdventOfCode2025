with open ('input.txt') as file:
    lines = file.readlines()

steps = [int(i[1:]) * (2 * (i[0] == 'R') - 1) for i in lines]
pos = 50
pt_1 = 0
pt_2 = 0

for step in steps:
    div, pos, prev = *divmod(pos + step, 100), pos
    pt_1 += (pos == 0)
    pt_2 += abs(div) - (prev == 0 and div < 0) + (pos == 0 and step < 0)

print(f"Part 1: {pt_1} \nPart 2: {pt_2}")