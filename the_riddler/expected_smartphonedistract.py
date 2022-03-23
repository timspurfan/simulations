'''
Source: https://fivethirtyeight.com/features/how-long-will-your-smartphone-distract-you-from-family-dinner/#solution
'''

from tqdm import tqdm
import random
from numpy import mean


num_trials = 10**5
results = []

for trial in tqdm(range(num_trials)):
    minutes = 0
    task_a = random.randint(1,5)
    task_b = random.randint(1,5)
    while True:
        minutes +=1
        task_a -=1
        task_b -=1
        if task_a ==0:
            if task_b ==0:
                break
            task_a = random.randint(1,5)
        if task_b ==0:
            task_b = random.randint(1,5)
    
    results.append(minutes)

expected_time = mean(results)
print('Expected time on phone: {}'.format(expected_time))