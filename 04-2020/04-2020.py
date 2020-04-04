import numpy as np


def Denary2Binary(num, digit):
    #returns the binary of integer n, using count number of digits
    return "".join([str((num >> y) & 1) for y in range(digit - 1, -1, -1)])


def generateCombinationList(num):
    list = []
    #generate list of combinations
    for item in range(0, 2**num):
        list.append(Denary2Binary(item, num))
    return list


def initializeMatrix(dimention):
    return np.zeros((dimention, dimention))


def checkPointsConnected(indexs, adjcentMatrix):
    if len(indexs) == 1:
        return True

    for i in indexs:
        copy = indexs.copy()
        copy.remove(i)
        record = []
        for j in copy:
            record.append(adjcentMatrix[i][j])
        if 1 not in record:
            return False
    return True


def checkDiffConnectWithBase(baseIndexs, index, adjcentMatrix):
    baseList = np.array(adjcentMatrix)[:, baseIndexs]
    return True if baseList[index].sum() > 0 else False


# count how many connect line linked with base points
def getConnectedMap(baseIndexs, diffIndexs, adjcentMatrix):
    if len(baseIndexs) == 0:
        raise Exception('base indexs cannot be empty')

    baseList = np.array(adjcentMatrix)[:, baseIndexs]

    if len(diffIndexs) == 0:
        return np.delete(baseList, baseIndexs, axis=0)
    else:
        return baseList[diffIndexs]


# base and compare are string
# return [] or [index]
def checkIsProceedOrEqual(base, compare):
    indexs = []
    for count in range(len(base)):
        result = int(compare[count]) - int(base[count])
        if result < 0:
            return False
        elif result > 0:
            indexs.append(count)
    return indexs


def fillCoefficient(base, diffIndexs, adjcentMatrix):
    allConnectdCount = getConnectedMap(base, [], adjcentMatrix).sum()
    # base dosen't change
    if len(diffIndexs) == 0:
        return (1 - possible)**allConnectdCount

    # check if any diffIndexs connect with any of base indexs
    # each index must have at least one connect line with base indexs
    for diffIndex in diffIndexs:
        if checkDiffConnectWithBase(base, diffIndex, adjcentMatrix) is False:
            return 0

    possibleMap = getConnectedMap(base, diffIndexs, adjcentMatrix)
    otherConnectCount = allConnectdCount - possibleMap.sum()

    result = 1
    for item in possibleMap:
        result = result * (1 - (1 - possible)**item.sum())

    return result * (
        (1 - possible)**(otherConnectCount if otherConnectCount > 0 else 0))


def fillMatrix(emptyMatrix, adjcentMatrix):
    for i in range(len(emptyMatrix)):
        for j in range(len(emptyMatrix[i])):
            row = Denary2Binary(i, len(adjcentMatrix))
            col = Denary2Binary(j, len(adjcentMatrix))

            # check and get diff indexs
            diff = checkIsProceedOrEqual(row, col)
            # base cannot be empty
            base = [index for index, ch in enumerate(row) if int(ch) == 1]
            if diff is not False and 0 in base and checkPointsConnected(
                    base,adjcentMatrix) is True:
                emptyMatrix[j][i] = fillCoefficient(base, diff, adjcentMatrix)

    return emptyMatrix


def calclulateResult(adjcentMatrix, initialState, days):
    matrix = fillMatrix(initializeMatrix(2**len(adjcentMatrix)), adjcentMatrix)
    for i in range(days):
        initialState = np.dot(matrix, initialState)
    return initialState[-1]


def fillAdjacent(adjacent, index, dimention):
    if index > dimention * dimention:
        if np.array(adjacent).sum() > 50:
          stateCopy = state[:]
          percent = calclulateResult(adjacent, stateCopy, days)
        # if percent > 69:
          print(percent)
        return
    else:
        x = (index - 1) // dimention
        y = (index - 1) % dimention
        # print(adjacent[row][col])
        if adjacent[x][y] is not None:
            fillAdjacent(adjacent, index + 1, dimention)
            return

        adjacent_copy_0 = []
        for item in adjacent:
            adjacent_copy_0.append(item[:])
        adjacent_copy_0[x][y] = 0
        adjacent_copy_0[y][x] = 0
        fillAdjacent(adjacent_copy_0, index + 1, dimention)

        adjacent_copy_1 = []
        for item in adjacent:
            adjacent_copy_1.append(item[:])
        adjacent_copy_1 = adjacent[:]
        adjacent_copy_1[x][y] = 1
        adjacent_copy_1[y][x] = 1
        fillAdjacent(adjacent_copy_1, index + 1, dimention)


initAdjacent = [[0, 1, 1, 1, 1, 1, None, None],
                [1, 0, None, None, None, None, None, None],
                [1, None, 0, None, None, None, None, None],
                [1, None, None, 0, None, None, None, None],
                [1, None, None, None, 0, None, None, None],
                [1, None, None, None, None, 0, None, None],
                [None, None, None, None, None, None, 0, None],
                [None, None, None, None, None, None, None, 0]]

possible = 0.1
days = 10


state = []
combinationList = generateCombinationList(len(initAdjacent))
for item in combinationList:
    if item == "10000000":
        state.append(1)
    else:
        state.append(0)

fillAdjacent(initAdjacent, 1, len(initAdjacent))
