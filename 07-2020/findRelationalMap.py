import numpy as np
import random
import math
from validation import getFibonacciList, getGoldenRectangleNumber, validation


def getAssignableIndexes(state, value):
    verticalMerge = np.sum(state, axis=0)
    return [
        idx for idx, item in enumerate(verticalMerge)
        if item == 0 and value[idx] > 0
    ]


def randomAssign(state, value, assignableCountLeft, assignableIndexes):
    copyState = np.array(state, copy=True)
    indexLength = len(assignableIndexes)
    #randomly assign 1 to each col
    for x in range(indexLength):
        y = random.randint(0, dimension - 1)
        copyState[y][assignableIndexes[x]] += 1

    if (assignableCountLeft == 0): return copyState

    #randomly assign count left
    for t in range(10):
        results = []
        left = assignableCountLeft
        for index in assignableIndexes:
            coe = random.randint(0, math.floor(left / value[index]))
            left = left - coe * value[index]
            if (left < 0): break
            if (left == 0):
                results.append(coe)
                break
            if (left > 0):
                results.append(coe)
        if (left == 0 and len(results) != 0):
            for idx, result in enumerate(results):
                for time in range(result):
                    copyState[random.randint(0, dimension - 1)][assignableIndexes[idx]] += 1
            return copyState
    return []


# print(getAssignableIndexes([[0,0],[0,0]],[1,1]))
def findSolution(state, value, n):
    assignableIndexes = getAssignableIndexes(state, value)
    verticalMerge = np.sum(state, axis=0)
    currentCount = np.dot(verticalMerge, value)
    assignableCount = getGoldenRectangleNumber(n + 2) - currentCount

    if (assignableCount < 0): return
    if (assignableCount == 0):
        if (len(assignableIndexes) > 0): return
        if (len(assignableIndexes) == 0):
            initValue = np.zeros(dimension, dtype=int)
            initValue[0] = 1
            if (validation(state, initValue, 40) == True):
                print('Solution found111111111111111111111:', state)

    if (assignableCount > 0):
        if (len(assignableIndexes) > assignableCount): return
        #assignable count left after 1 is assigned to each col
        assignableCountLeft = assignableCount - value[assignableIndexes].sum()
        if (assignableCountLeft < 0): return
        if (len(assignableIndexes) == 0): return
        if (len(assignableIndexes) > 0):
            for x in range(10):
                assignedState = randomAssign(state, value, assignableCountLeft,
                                             assignableIndexes)
                if (len(assignedState) != 0):
                    findSolution(assignedState, np.dot(assignedState, value),
                                 n + 1)


for d in [4,5,6,7,8,9,10]:
  dimension = d
  value = np.zeros(dimension, dtype=int)
  value[0] = 1
  state = np.zeros((dimension, dimension), dtype=int)
  findSolution(state, value, 0)


