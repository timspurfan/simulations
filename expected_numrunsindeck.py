'''
problem: given a shuffled deck of cards, find the expected amount of 
"runs" of black and red cards total.

answer: 27
solution: 
let y_i = 1 if y_i != y_(i-1) and 0 otherwise.  y_0 = 1
we want to find EV(summation y_i for all i).  
note that by symmetry ev(y_j) = ev(y_k) for all (except 0)
ev(y_i) = 2 * (2n-2 choose n-1) ) / (2n choose n) = n/(2n-1)

So EV = 1 + 51*(26/51) = 27
'''

from tqdm import tqdm
from numpy import mean
import random

results = []
num_trials = 100000
deck = ['red' for i in range(26)] + ['black' for j in range(26)]

for trial in tqdm(range(num_trials)):
    shuffle = deck
    random.shuffle(shuffle)
    num_runs = 1
    for i in range(1,52):
        if shuffle[i] != shuffle[i-1]:
            num_runs+=1
    results.append(num_runs)

ev_numruns = mean(results)
print(ev_numruns)