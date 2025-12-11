import re
import scipy

with open('input.txt', 'r') as f:
    inp = f.read().split('\n')

if len (inp[-1]) == 0:
    inp.pop()

machines = []
buttons = []
joltages = []

for line in inp:
    mach = re.findall(r'\[([^\]]*)\]', line)
    machines.append(mach[0])

    btns = re.findall(r'\(([^\(]*)\)', line)
    btns = [[int(x) for x in btn.split(',')] for btn in btns]
    buttons.append(btns)

    jolts = re.findall(r'\{([^\{]*)\}', line)
    jolts = [int(x) for x in jolts[0].split(',')]
    joltages.append(jolts)

def findXors(target, nums):
    ans = []
    n = len(nums)
    least = n + 1

    for i in range(2**n):
        # Each i is a subset
        xor = 0
        subset = []
        for j in range(n):
            if (i >> j) % 2 == 1:
                xor ^= nums[j]
                subset.append(j)
        if xor == target and len(subset) < least:
            least = len(subset)
            ans = subset
    return ans

def pt1():
    nbtns = []
    for i, btns in enumerate(buttons):
        nbtn = [sum([2**( len(machines[i]) - x - 1) for x in btn]) for btn in btns]
        nbtns.append(nbtn)

    ans = 0
    for i, mach in enumerate(machines):
        target = 0
        for j, ch in enumerate(mach[-1::-1]):
            if ch == '#':
                target += 2**j
        ans += len(findXors(target, nbtns[i]))
    return ans

def pt2():
    ans = 0
    for i, jolts in enumerate(joltages):
        buts = buttons[i]
        
        A = [[0 for i_ in range(len(buts))] for j in range(len(jolts))]
        for j, but in enumerate(buts):
            for light in but:
                A[light][j] = 1

        c = [1 for i_ in range(len(buts))]
        res = scipy.optimize.linprog(c, A_eq=A, b_eq=jolts, integrality=1)

        if not res.success:
            print("Couldn't find optimal solution")
            return -1

        ans += sum(res.x)
    return ans


print("Part 1:", pt1())
print("Part 2:", pt2())