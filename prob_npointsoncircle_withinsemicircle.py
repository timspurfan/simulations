'''
Problem: Given n points drawn randomly on the circumference of a circle, 
what is the probability they will all be within any common semicircle?

A: n/2^(n-1)
'''

from tqdm import tqdm
import random
import numpy as np
from math import pi

num_successes = [0 for i in range(9)]
num_trials = 10**5
num_n = 10

for n in tqdm(range(1, num_n)):
    for trial in tqdm(range(num_trials)):
        points = np.random.random(n)*2*pi
        points.sort()
        for index, val in enumerate(points):
            if (points[index-1]-val)%(2*pi)<pi:
                num_successes[n-1] += 1
                break

print(num_successes)

prob = [freq/num_trials for freq in num_successes]
actual = [i/2**(i-1) for i in range(1,10)]

print('Estimated prob: {}'.format(prob))
print(actual)