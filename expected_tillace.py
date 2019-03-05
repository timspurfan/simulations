import random
from tqdm import tqdm
from numpy import mean


'''
expected amount of cards until first ace
'''

num_trails = 1000000
results = []

for trial in tqdm(range(num_trails)):
    locations = random.sample(range(1,53), 4)
    first_ace = min(locations)
    results.append(first_ace)

expected = mean(results)
print(expected)