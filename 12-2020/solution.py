import math


def getValidNum(num, percent, range):
    low = math.floor(num * percent)
    high = math.ceil(num * percent)

    result = []
    if low >= num * range[0] and low <= num * range[1]:
        result.append([low, num])
    if high >= num * range[0] and high <= num * range[1]:
        result.append([high, num])
    if len(result) == 0:
        return False
    return result


for num in range(500, 751):
    isValid = getValidNum(num, 0.71781305, [0.717813045, 0.71781306])
    if isValid != False:
        print(isValid)

collection = []


def getPossibleArray(total, electors, result=[]):
    if total <= 0:
        return
    if len(electors) == 0:
        return
    if total in electors:
        result.append(total)
        print("*****************************************************")
        print("Group A:", result, ",Sum :", sum(result))
        copyOfElectors = numOfElectorsForEachState[:]
        for el in result:
            copyOfElectors.remove(el)
        print("Group B:", copyOfElectors, ",Sum :", sum(copyOfElectors))
        return

    copy = electors[:]
    last = copy.pop()
    # count out
    getPossibleArray(total, copy, result[:])

    result.append(last)
    # count in
    getPossibleArray(total - last, copy, result[:])


numOfElectorsForEachState = [
    9, 3, 11, 6, 55, 9, 7, 3, 3, 29, 16, 4, 4, 20, 11, 6, 6, 8, 8, 4, 10, 11,
    16, 10, 6, 10, 3, 5, 6, 4, 14, 5, 29, 15, 3, 18, 7, 7, 20, 4, 9, 3, 11, 38,
    6, 3, 13, 12, 5, 10, 3
]
# 270 - 268
getPossibleArray(270, numOfElectorsForEachState, [])

