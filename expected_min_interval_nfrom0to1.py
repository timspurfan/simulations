'''
Problem: pick n random numbers from 0 to 1.  
find the expected value of the minimum interval length

Answer: 1/(n+1)^2

TODO: ADD SOLUTION
'''

from tqdm import tqdm
import numpy as np
import random

number_of_n = 10
number_of_trials_per_n = 10**5

expectedmin_interval_n=[0 for i in range(1,number_of_n)]

for n in tqdm(range(1,number_of_n)):
    results_for_this_n = []
    for trial in tqdm(range(number_of_trials_per_n)):
            n_choices = np.random.random(n)
            n_choices = np.append(n_choices, [0,1])
            n_choices = np.sort(n_choices) #sort numbers
            interval_lengths = np.array([i-j for i,j in zip(n_choices[1:],n_choices)])
            results_for_this_n.append(min(interval_lengths))
    expectedmin_interval_n[n-1] = np.mean(results_for_this_n)

print(expectedmin_interval_n)