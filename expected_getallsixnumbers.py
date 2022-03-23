import random
from tqdm import tqdm
from numpy import mean

'''
this is really just the coupon collecter problem
'''

num_trails = 100000
results = []
done = set([1,2,3,4,5,6])

for trial in tqdm(range(num_trails)):
    so_far = set()
    num_rolls = 0
    while so_far != done:
        roll = random.randint(1,6)
        num_rolls +=1
        so_far.add(roll)
    results.append(num_rolls)

expected = mean(results)
print(expected)
