import random
from collections import deque
from queue import Queue
from tqdm import tqdm
from numpy import mean

'''
given a sequence of heads and tails, find the expected number of flips until that sequence comes

math solution:
consider the markov chain.
'''

results=[]
goal = deque(['tails','tails','heads'])
goal_2 = deque(['heads','tails','tails'])
num_trails = 100000

for trial in tqdm(range(num_trails)):
    sequence = deque()
    num_flips = 0

    for i in range(len(goal)):
        flip = random.choice(['heads', 'tails'])
        num_flips +=1
        sequence.append(flip)

    while sequence != goal and sequence != goal_2:
        sequence.popleft()
        flip = random.choice(['heads', 'tails'])
        num_flips +=1
        sequence.append(flip)

    results.append(num_flips)

expected = mean(results)
print(expected)