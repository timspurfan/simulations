'''
Source: https://fivethirtyeight.com/features/which-geyser-gushes-first/
'''
from tqdm import tqdm
import random

num_times_first = [0]*3
num_trials = 10**6

for trial in tqdm(range(num_trials)):

    geyser_2 = random.uniform(0,2)
    geyser_4 = random.uniform(0,4)
    geyser_6 = random.uniform(0,6)

    first_geyser = min(geyser_2, geyser_4, geyser_6)

    if geyser_2 == first_geyser:
        num_times_first[0] +=1
    
    if geyser_4 == first_geyser:
        num_times_first[1] +=1
    
    if geyser_6 == first_geyser:
        num_times_first[2] += 1
    
prob_coming_first = [prob/num_trials for prob in num_times_first]
print(prob_coming_first)