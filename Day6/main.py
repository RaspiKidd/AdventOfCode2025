from collections import defaultdict

def calcNums(col, op):
    if op == '+':
        return sum(col)
    prod = 1
    for v in col:
        prod *= v
    return prod

# ---- PART 1 ----
with open('input.txt', 'r') as file:
    data = file.read()
    lines = data.splitlines()
    vals = defaultdict(list)
    for i in range(len(lines)-1):
        line = lines[i]
        nums = [int(x) for x in line.split()]
        for j in range(len(nums)):
            vals[j].append(nums[j])
    ops = lines[-1].split()
    ans = 0
    for i in range(len(ops)):
        ans += calcNums(vals[i], ops[i])
    print("Part 1: ", ans)

# ---- PART 2 ----
with open('input.txt', 'r') as file:
    data = file.read()
    lines = data.splitlines()
    nums = []
    curOp = ''
    maxLen = max(len(line) for line in lines)
    ans = 0
    for x in range(maxLen):
        curNum = 0
        for y in range(len(lines)):
            if x < len(lines[y]):
                if lines[y][x] in '+*':
                    curOp = lines[y][x]
                elif lines[y][x] == ' ':
                    pass
                else:
                    curNum *= 10
                    curNum += int(lines[y][x])
        if curNum != 0:
            nums.append(curNum)
        else:
            ans += calcNums(nums, curOp)
            nums = []
    ans += calcNums(nums, curOp)
    print("Part 2: ", ans)