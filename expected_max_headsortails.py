'''
Find the expected number of max(heads, tails) in 100 (n) flips
'''

from numpy import mean
from tqdm import tqdm
import random

num_trials = 10**6
num_flips = 100

results = []

for trail in tqdm(range(num_flips)):

    flips = random.choices([0,1], k=100)
    num_heads = sum(flips)
    num_tails = 100 - num_heads
    results.append(max(num_heads, num_tails))

ev = mean(results)
print(ev) #53.8ish