'''
take a stick and cut it into three smaller sticks randomly
what is the probability these form a triangle?
'''

import random
from tqdm import tqdm
from numpy import mean

num_trials = 1000000
results = []

for trial in tqdm(range(num_trials)):
    temp1 = random.random()
    temp2 = random.random()
    a = min(temp1,temp2)
    b = max(temp1,temp2) - a
    c = 1-max(temp1,temp2)
    a,b,c = sorted([a,b,c])
    if a+b>c:
        results.append(1)
    else:
        results.append(0)

prob = mean(results)
print(prob)
#.25 (1/4)