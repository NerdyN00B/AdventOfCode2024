import numpy as np

array = np.loadtxt('day_1/input.txt', dtype=int)

array = np.sort(array, axis=0)
array_1 = array[:, 0]
array_2 = array[:, -1]

distance = np.sum(np.abs(array_2 - array_1))

print(distance)