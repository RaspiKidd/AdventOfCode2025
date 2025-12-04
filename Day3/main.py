rows = open ("input.txt").read().split()

def argMax(xs):
    return max(enumerate(xs), key=lambda x: x[1])[0]

def pt1Joltage(row):
    i = argMax(row[:-1])
    j = argMax(row[i+1:]) + i+1
    return int(row[i] + row[j])

pt1Total = sum(pt1Joltage(row) for row in rows)

def pt2Joltage(row, leave=0):
    if leave > 0:
        i = argMax(row[:-leave])
        return row[i] + pt2Joltage(row[i+1:], leave = leave - 1)
    else:
        return max(row)
    
pt2Total = sum (int(pt2Joltage(row, 11)) for row in rows)

print(f"Part 1: {pt1Total}")
print(f"Part 2: {pt2Total}")