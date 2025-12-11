from collections import *

with open('input.txt') as f:
    lines = f.read().splitlines()

# Make edge mapping
edges = defaultdict(list)
indegrees = defaultdict(int)
for line in lines:
    line = line.split()
    # Chop off the last character of the source as they are formatted like "edge:"
    edges[line[0][:-1]] = line[1:]
    # Get indegrees for topological sort
    for dest in line[1:]:
        indegrees[dest] += 1
edges['out'] = []

# Simple DFS for part 1
def get_paths_dfs(edge, goal):
    if edge == goal:
        return 1
    
    return sum(get_paths_dfs(dest, goal) for dest in edges[edge])

# Topological sort DP for part 2
def get_paths_toposort(start, end):
    # Count is [overall, after seeing fft, after seeing fft and dag]
    counts = {edge:[0, 0, 0] for edge in edges}
    counts[start] = [1,0,0]
    
    # Topological sort to count paths
    q = deque([start])
    while q:
        edge = q.popleft()
        # Copy over counts when we first reach fft and dac
        if edge == 'fft':
            counts[edge][1] = counts[edge][0]
        elif edge == 'dac':
            counts[edge][2] = counts[edge][1]
            
        for dest in edges[edge]:
            # Add all counts
            counts[dest][0] += counts[edge][0]
            counts[dest][1] += counts[edge][1]
            counts[dest][2] += counts[edge][2]
            # Add to queue if we've visited this node from all parents
            indegrees[dest] -= 1
            if indegrees[dest] == 0:
                q.append(dest)

    return counts[end][2]

print('Part 1:', get_paths_dfs('you', 'out'))
print('Part 2:', get_paths_toposort('svr', 'out'))