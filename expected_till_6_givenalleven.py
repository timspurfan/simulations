'''
Find the expected number of rolls of die until a 6 appears given that all rolls prior were even.

'''

from tqdm import tqdm
from numpy import mean
import random

num_trials = 10**5
results = []

for trial in tqdm(range(num_trials)):
    num_rolls = 0
    while True:
        roll = random.randint(1,6)
        num_rolls += 1
        if roll == 6:
            results.append(num_rolls)
            break
        if roll%2 == 1:
            break

expected = mean(results)
print(expected)



