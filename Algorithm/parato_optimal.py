import numpy as np

scores = np.array([[97, 23],
                  [55, 77],
                  [34, 76],
                  [80, 60],
                  [99,  4],
                  [81,  5],
                  [ 5, 81],
                  [30, 79],
                  [15, 80],
                  [70, 65],
                  [90, 40],
                  [40, 30],
                  [30, 40],
                  [20, 60],
                  [60, 50],
                  [20, 20],
                  [30,  1],
                  [60, 40],
                  [70, 25],
                  [44, 62],
                  [55, 55],
                  [55, 10],
                  [15, 45],
                  [83, 22],
                  [76, 46],
                  [56, 32],
                  [45, 55],
                  [10, 70],
                  [10, 30],
                  [79, 50]])

def identify_pareto(scores):
    # Count number of items
    population_size = scores.shape[0]
    print(population_size)
    # Create a NumPy index for scores on the pareto front (zero indexed)
    population_ids = np.arange(population_size)
    # Create a starting list of items on the Pareto front
    # All items start off as being labelled as on the Parteo front
    pareto_front = np.ones(population_size, dtype=bool)
    # Loop through each item. This will then be compared with all other items
    for i in range(population_size):
        # Loop through all other items
        for j in range(population_size):
            # Check if our 'i' pint is dominated by out 'j' point
            if all(scores[j] >= scores[i]) and any(scores[j] > scores[i]):
                # j dominates i. Label 'i' point as not on Pareto front
                pareto_front[i] = 0
                # Stop further comparisons with 'i' (no more comparisons needed)
                break
    # Return ids of scenarios on pareto front
    return population_ids[pareto_front]


pareto = identify_pareto(scores)
print ('Pareto front index vales')
print ('Points on Pareto front: \n',pareto)

pareto_front = scores[pareto]
print ('\nPareto front scores')
print (pareto_front)