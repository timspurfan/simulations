'''
use a die to estimate the value
of pi
'''

'''
use two rolls of the die to give us coordinates within square from (0,0) to (1,1) which we can check
whether would fall in circle of radius one centered at origin.
'''

import random
from numpy import mean
from tqdm import tqdm

num_trials = 100000
results = []
n=5

def coordinate_from_die(n):
    coord = 0
    for i in range(1,n+1):
        coord += (random.randint(1,6)-1)/(6**i)
    return coord

for trial in tqdm(range(num_trials)):
    x_coordinate = coordinate_from_die(n)
    y_coordinate = coordinate_from_die(n)
    if x_coordinate**2+y_coordinate**2 <= 1:
        results.append(1)
    else:
        results.append(0)

prob = 4 * mean(results)
print(prob)