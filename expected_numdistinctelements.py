from tqdm import tqdm
from numpy import mean
import random

num_trials = 50000
n = 25
bucket = [i for i in range(n)]
results = []

for trial in tqdm(range(num_trials)):
    draw = random.choices(bucket, k=n)
    num_disctinct = len(set(draw))
    results.append(num_disctinct)

expected_distinct = mean(results)
print(expected_distinct)

actual = n*(1-((n-1)/n)**n)
print(actual)