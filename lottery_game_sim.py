'''
pick two numbers from 1 - 100 and receive the minimum.  how much should u pay to play
'''

import random
import numpy as np
from tqdm import tqdm

nums = [i for i in range(1,1001)]

trials = 100000
results = []

for trial in tqdm(range(trials)):
    picks = random.sample(nums,2)
    results.append(min(picks))

price = np.mean(results)

print(price)