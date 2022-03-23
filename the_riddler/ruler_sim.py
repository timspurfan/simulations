'''
A 1ft ruler is broken up into 4 pieces (the cuts being done uniform randomly).
Find the expected size of the piece containing the 6inch mark.
'''

from tqdm import tqdm
import random
from numpy import mean

num_trials = 10**6
results = []

for trial in tqdm(range(num_trials)):
    cuts = sorted([0,.5,1]+[random.random() for i in range(3)])
    #print(cuts)
    size = cuts[cuts.index(.5)+1]-cuts[cuts.index(.5)-1]
    #print(size)
    results.append(size)

print(mean(results))