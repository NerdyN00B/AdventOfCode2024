import numpy as np
import pandas as pd

def part_one():
    with open('day_2/input.txt', 'r') as f:
        data = f.readlines()
    stripped = [line.strip('\n') for line in data]
    data = sorted(stripped, key=lambda x: len(x), reverse=True)
    
    with open('day_2/workaround.txt', 'w') as f:
        for item in data:
            f.write("%s\n" % item)
    
    data = pd.read_csv('day_2/workaround.txt', sep=' ', header=None,
                       engine='python')
    # print(data)
    diff = np.diff(data, axis=-1)
    nsafe = 0
    for i in range(len(diff)):
        if np.nanmin(diff[i]) < -3:
            continue
        elif np.nanmax(diff[i]) > 3:
            continue
        elif np.nanmin(diff[i]) < 0:
            if np.nanmax(diff[i]) >= 0:
                continue
            else:
                nsafe += 1
                continue
        elif np.nanmax(diff[i]) > 0:
            if np.nanmin(diff[i]) <= 0:
                continue
            else:
                nsafe += 1
                continue
    
    return nsafe

def part_two():
    with open('day_2/test.txt', 'r') as f:
        data = f.readlines()
    stripped = [line.strip('\n') for line in data]
    data = sorted(stripped, key=lambda x: len(x), reverse=True)
    
    with open('day_2/workaround.txt', 'w') as f:
        for item in data:
            f.write("%s\n" % item)
    
    data = pd.read_csv('day_2/workaround.txt', sep=' ', header=None,
                       engine='python', dtype=float)
    print(data)
    diff = np.diff(data, axis=-1)
    for i in range(len(diff)):
        if np.nanmin(diff[i]) < -3:
            data[i, np.nanargmin(diff[i])] = np.nan
        elif np.nanmax(diff[i]) > 3:
            data[i, np.nanargmax(diff[i])] = np.nan
        elif np.nanmin(diff[i]) < 0:
            if np.nanmax(diff[i]) >= 0:
                data[i, np.nanargmax(diff[i])] = np.nan
            else:
                continue
        elif np.nanmax(diff[i]) > 0:
            if np.nanmin(diff[i]) <= 0:
                data[i, np.nanargmin(diff[i])] = np.nan
            else:
                continue
    
    diff = np.diff(data, axis=-1)
    print(diff)
    nsafe = 0
    for i in range(len(diff)):
        if np.nanmin(diff[i]) < -3:
            continue
        elif np.nanmax(diff[i]) > 3:
            continue
        elif np.nanmin(diff[i]) < 0:
            if np.nanmax(diff[i]) >= 0:
                continue
            else:
                nsafe += 1
                continue
        elif np.nanmax(diff[i]) > 0:
            if np.nanmin(diff[i]) <= 0:
                continue
            else:
                nsafe += 1
                continue
    return nsafe
    #FUUUUUUCK

print(part_one())
print(part_two())