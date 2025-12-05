with open("input.txt") as f:
    content = f.read().split("\n\n")
    validRanges = [tuple(int(num) for num in line.split("-")) for line in content[0].split("\n")]
    ingredients = [int(line) for line in content[1].strip().split("\n")]

def inRanges(ingredients, ranges):
    for start, end in validRanges:
        if ingredients >= start and ingredients <= end:
            return True
    return False

freshIngredients = 0
for ingredient in ingredients:
    if inRanges(ingredient, validRanges):
        freshIngredients += 1

print("Part 1: ", freshIngredients)

def mergeRanges(ranges):
    if not ranges:
        return []
    sortedRanges = sorted(ranges, key=lambda x: x[0])
    merged = [sortedRanges[0]]
    for s, e in sortedRanges[1:]:
        lastS, lastE = merged[-1]
        if s <= lastE + 1:
            if e > lastE:
                merged[-1] = (lastS, e)
        else:
            merged.append((s, e))
    return merged
mergedRanges = mergeRanges(validRanges)

validIDs = 0
for start, end in mergedRanges:
    validIDs += end - start + 1

print("Part 2: ", validIDs)