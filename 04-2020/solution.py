import numpy as np
import random

def calculateProbability(AdjacentMatrix, days):
    dimension = len(AdjacentMatrix)
    state = np.zeros((2**dimension), dtype=int)
    state[1] = 1

    EvolutionMatrix = np.ones((2**dimension, 2**dimension))
    for x in range(2**dimension):
        for y in range(2**dimension):
            row = [(x // 2**k) % 2 for k in range(dimension)]
            col = [(y // 2**k) % 2 for k in range(dimension)]
            factor = 1
            for d in range(dimension):
                #infection status from 1 => 0
                if row[d] == 1 and col[d] == 0:
                    f = 0
                #infection status from 1 => 1
                elif row[d] == 1 and col[d] == 1:
                    f = 1
                #infection status from 0 => 1
                elif row[d] == 0 and col[d] == 1:
                    #get the counts of connected lines with infetced people
                    f = 1 - (1 - p)**np.dot(AdjacentMatrix[d], row)
                #infection status from 0 => 0
                elif row[d] == 0 and col[d] == 0:
                    f = (1 - p)**np.dot(AdjacentMatrix[d], row)

                factor = factor * f
            EvolutionMatrix[y][x] = EvolutionMatrix[y][x] * factor

    for d in range(days):
        state = np.dot(EvolutionMatrix, state)

    return state[-1]


# aj = [[0, 1, 1, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 1, 0, 0],
#       [1, 1, 0, 1, 0, 0, 1, 1], [1, 1, 1, 0, 1, 0, 1, 1],
#       [1, 1, 0, 1, 0, 1, 1, 1], [1, 1, 0, 0, 1, 0, 1, 1],
#       [0, 0, 1, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1, 0]]

p = 0.1
dimension = 8
threshold = 0.5
days = 10

for index in range(100000000):
    adjacent = np.zeros((dimension, dimension), dtype=int)
    for i in range(dimension):
        for j in range(i + 1, dimension):
            dice = random.random()
            if dice < threshold:
                adjacent[i][j] = 1
                adjacent[j][i] = 1
            else:
                adjacent[i][j] = 0
                adjacent[j][i] = 0
    probability = calculateProbability(adjacent, days)
    if 0.701 > probability > 0.69999:
        print('*' * 100)
        print(probability, threshold)
    threshold = threshold * (1 - (probability - 0.7) * 0.01)
    print(threshold)
