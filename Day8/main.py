lines = open('input.txt').read().splitlines()
n = len(lines)
aretes = []

for i, line1 in enumerate(lines):
    x1, y1, z1 = map(int, line1.split(','))
    for j, line2 in enumerate(lines[i+1:]):
        x2, y2, z2 = map(int, line2.split(','))
        dx = x2 - x1
        dy = y2 - y1
        dz = z2 - z1
        distsq = dx**2 + dy**2 + dz**2
        aretes.append((distsq, i, j + i + 1))
aretes.sort()

parent = list(range(n))
size = [1] * n

def find(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return 0
    parent[b] = a
    size[a] += size[b]
    return size[a]

for _, a, b in aretes[:1000]:
    union(a, b)

sizes = [size[i] for i in range(n) if i == parent[i]]
sizes.sort()
print('Part 1: ', sizes[-1]*sizes[-2]*sizes[-3])

parent = list(range(n))
size = [1] * n
k = 0
while True:
    _, a, b = aretes[k]
    if union(a, b) == n:
        break
    k += 1

x1 = int(lines[a].split(',')[0])
x2 = int(lines[b].split(',')[0])

print('Part 2: ', x1*x2)