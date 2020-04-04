import numpy as np


def calEvolutionMatrix(AdjacentMatrix):
    dimension = len(AdjacentMatrix)
    EvolutionMatrix = np.zeros((2**dimension, 2**dimension))
    for i in range(2**dimension):
        for j in range(2**dimension):
            possible = True
            row = []
            col = []
            for k in range(dimension):
                row.append((i // 2**k) % 2)
                col.append((j // 2**k) % 2)
                if row[k] > col[k]:
                    possible = False
                    break
            if possible:
                EvolutionMatrix[j][i] = 1
                for k in range(dimension):
                    if row[k] == 0:
                        x = int(np.dot(AdjacentMatrix[k], row))
                        EvolutionMatrix[j][i] = EvolutionMatrix[j][i] * (
                            (1 - col[k]) + (2 * col[k] - 1) * probability[x])

    return EvolutionMatrix


AdjacentMatrix = [[0, 1, 1, 1, 0], [1, 0, 0, 0, 1], [1, 0, 0, 1, 0],
                  [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]]
p = 0.1
probability = [1 - (1 - p)**i for i in range(len(AdjacentMatrix))]
evolutionMatrix = calEvolutionMatrix(AdjacentMatrix)

InitialState = np.zeros((2**len(AdjacentMatrix)))
InitialState[1] = 1

state = InitialState
for i in range(10):
    state = np.dot(evolutionMatrix, state)

print(state)