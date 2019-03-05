'''
Now suppose the two players are flipping seperate coins
Find probability each players respective sequence comes up first.
'''

import random
from numpy import mean, array
from tqdm import tqdm
import typing

sequence_1 = ['heads','heads','heads']
sequence_2 = ['heads', 'heads']

results = array([0,0,0])


num_trial = 1000000

for trial in tqdm(range(num_trial)):
    
    actual_sequence_1 = []
    actual_sequence_2 = []

    while True:

        flip_1 = random.choice(['heads', 'tails'])
        flip_2 = random.choice(['heads', 'tails'])
        #alternative flip_1, flip_1 = random.choices((['heads', 'tails'], k=2)

        actual_sequence_1.append(flip_1)
        actual_sequence_2.append(flip_2)

        if actual_sequence_1[-len(sequence_1):] == sequence_1:
            if actual_sequence_2[-len(sequence_2):] == sequence_2:
                results[2] += 1
                break
            else:
                results[0] += 1
                break
        if actual_sequence_2[-len(sequence_2):] == sequence_2:
            results[1] += 1
            break

probability = results/num_trial
print(probability)