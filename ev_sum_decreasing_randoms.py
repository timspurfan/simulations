import random
from tqdm import tqdm
from numpy import mean

'''
pick decreasing random numbers (starting at random 0 to 1)
does the sum converge, and if so, to what value?
'''

num_trials = 10**5
results = []

for trial in tqdm(range(num_trials)):
    current_sum = 0
    rand_decreasing = 1
    while rand_decreasing > .00001:
        rand_decreasing = random.uniform(0,rand_decreasing)
        current_sum += rand_decreasing
    results.append(current_sum)

print(mean(results))