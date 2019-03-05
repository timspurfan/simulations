'''
draw random elements from 0 to 1 as long as they continue to appear in decreasing
order.  return the smallest once there is one which is not less than the previous

question: what is the expected value of the min?
answer: 3-e

solution:
the probablilty there are n numbers selected and x is the smallest is:
(1-x)^n-1 --- (the n-1 nums before are all x are all greater than x)
*
(1/n!) --- (the n nums including x are in decreasing order)
*
(1-x) --- (the number after x is greater than x)

so the pdf is (1-x)^n / n! --- this is just e^(1-x)
and ev = integral from 0 to 1 of x*e^(1-x)
'''


from tqdm import tqdm
from numpy import mean
import random

results = []
num_trials = 100000

'''
for trial in tqdm(range(num_trials)):

    draws = []
    draw = random.random()
    draws.append(draw)

    while True:
        draw = random.random()
        if draw > draws[-1]:
            results.append(draws[-1])
            break
        else:
            draws.append(draw)
'''

for trial in tqdm(range(num_trials)):
    prev = random.random()
    current = random.random()
    while current < prev:
        prev = current
        current = random.random()
    results.append(prev)

ev_min = mean(results)
print(ev_min)