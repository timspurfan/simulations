import random
from tqdm import tqdm
from numpy import mean

num_trials = 1000
results = []

for trial in tqdm(range(num_trials)):

    sum = 0
    counter = 0
    while sum < 1:
        counter +=1
        sum += random.random()
    results.append(counter)

expected = mean(results)
print(expected)