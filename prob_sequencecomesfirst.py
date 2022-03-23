'''
Penney's Game Simulation
given two sequences of heads and tails, what is the probability that each comes first when
flipping a coin?
'''

import random
from tqdm import tqdm
from numpy import mean
from collections import deque


sequence_1 = ['tails', 'tails', 'heads']
sequence_2 = ['heads', 'tails', 'tails']

results = []
num_trials = 1000000

for trial in tqdm(range(num_trials)):
    sequence = []
    while True:
        flip = random.choice(['heads','tails'])
        sequence.append(flip)

        if sequence[-len(sequence_1):] == sequence_1:
            results.append(1)
            break
        if sequence[-len(sequence_2):] == sequence_2:
            results.append(0)
            break

prob = mean(results)

print('Probability {} comes first = {}'.format(list(sequence_1),prob))
print('Probability {} comes first = {}'.format(list(sequence_2),1-prob))

