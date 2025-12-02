with open("input.txt") as f:
    idRanges = [tuple(int(x) for x in part.split("-")) for part in f.read().split(",")]

invalidIds = []

for start, end in idRanges:
    for num in range(start, end + 1):
        strId = str(num)
        if len(strId) % 2 == 0:
            half = len(strId) // 2
            if strId[:half] == strId[half:]:
                invalidIds.append(num)

pt1 = sum(invalidIds)

invalidIds = []

for start, end in idRanges:
    for num in range(start, end + 1):
        invalidIdsNum = set()
        strId = str(num)
        for partLen in range(1, len(strId)//2 + 1):
            part = strId[:partLen]
            if len(strId) % partLen == 0:
                if part * (len(strId) // partLen) == strId:
                    invalidIdsNum.add(num)
        for invalidId in invalidIdsNum:
                invalidIds.append(invalidId)
pt2 = sum(invalidIds)

print("Part 1:", pt1)
print("Part 2:", pt2)