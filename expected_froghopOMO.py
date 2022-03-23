'''
A frog starts at the origin.  Each minute it jumps either 1 or 2 steps to the left or right.
The frog stops jumping when it lands on a negative number or a number it has previously
landed on.  Find the expected number of jumps the frog will take.

Source: OMO
'''
from random import choice
from tqdm import tqdm
from numpy import mean

num_trials = 10**6
jumps = [0 for i in range(num_trials)]
possibilities = [-2,-1,1,2]

for trial in tqdm(range(num_trials)):

    location = 0
    num_jumps = 0
    visited = set()

    visited.add(0)
    location += choice(possibilities)
    num_jumps += 1 

    while location >= 0 and location not in visited:
        visited.add(location)
        location += choice(possibilities)
        num_jumps += 1
    
    jumps[trial] = num_jumps #ev = 2.235ish

print(mean(jumps))
