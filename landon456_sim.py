import random 
from tqdm import tqdm
from numpy import mean

'''
find probability of rolling a die on 1 and getting an eventual sum of 4,5, or 6
'''

num_trials = 100000
results = []
for trial in tqdm(range(num_trials)):
    current = 0
    while current <= 6:
        roll = random.randint(1,6)
        current += roll

        if current == 4 or current == 5 or current==6:
            results.append(1)
            break
    else:
        results.append(0)

prob = sum(results)/num_trials
same_prob = mean(results)
print(prob)
print(same_prob)