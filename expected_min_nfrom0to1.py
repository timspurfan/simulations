'''
pick n random numbers from 0 to 1.  find the expected value of the minimum. (and max)

bonus: expected value of smallest "stick"
'''
from tqdm import tqdm
import numpy as np
import random
from matplotlib import pyplot as plt

number_of_n = 10
number_of_trials_per_n = 10**5

expectedmin_n=[0 for i in range(1,number_of_n)]

for n in tqdm(range(1,number_of_n)):
    results_for_this_n = []
    for trial in tqdm(range(number_of_trials_per_n)):
            n_choices = np.random.random(n)
            results_for_this_n.append(min(n_choices))
    expectedmin_n[n-1] = np.mean(results_for_this_n)

'''
#answer should be 1/(n+1)
plt.plot(range(1,10),expectedmin_n)

plt.plot(x,y)
plt.show()
'''
x=[i for i in range(1,10)]
y=[1/(n+1) for n in x]
differences = [a-b for a,b in zip(expectedmin_n,y)]
print(differences)