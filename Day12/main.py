HEIGHT = 3
WIDTH = 3


def parseInput(filename):
    with open(filename) as inputFile:
        rawData = inputFile.read().split("\n\n")
    regions = [parseRegion(region) for region in rawData[-1].split("\n")]
    presents = [line.count("#") for line in rawData[:-1]]
    return presents, regions


def parseRegion(region):
    dimensionsRaw, * countRaw = region.split()
    dimensions = (int(dimensionsRaw[:2]), int(dimensionsRaw[3:5]))
    count = [int(num) for num in countRaw]
    return dimensions, count


def checkRegion(presents, region):
    (width, height), count = region
    total = sum(p * c for p, c in zip(presents, count))
    if total > width * height:
        return -1
    if (width // WIDTH) * (height // HEIGHT) >= sum(count):
        return 1
    return 0


def solve(presents, regions):
    return [checkRegion(presents, region) for region in regions]


presents, regions = parseInput("input.txt")
results = solve(presents, regions)

print(f"{'Fit:':<15}{results.count(1)}")
print(f"{'Cannot fit:':<15}{results.count(-1)}")
print(f"{'Inconclusive:':<15}{results.count(0)}")
