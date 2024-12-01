import numpy as np

array = np.loadtxt('day_1/input.txt', dtype=int)

array = np.sort(array, axis=0)
array_1 = array[:, 0]
array_2 = array[:, -1]

uniques, counts = np.unique(array_2, return_counts=True)

last_number = 0
last_multiplier = 0
simscore = 0
for number in array_1:
    if number == last_number:
        simscore += last_number * last_multiplier
        continue
    else:
        last_number = number
        if last_number in uniques:
            last_multiplier = counts[np.where(uniques == last_number)][0]
            simscore += last_number * last_multiplier
        else:
            last_multiplier = 0

print(simscore)