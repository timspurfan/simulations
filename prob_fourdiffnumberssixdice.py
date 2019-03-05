'''
roll 6 dice, for n=0 (n=0 impossible) to 6, determine prob of rolling n different numbers
'''

from tqdm import tqdm
import random

results = [0 for i in range(7)]
num_trials = 10**5

for trial in tqdm(range(num_trials)):
    dice_rolls = random.choices(range(1,7),k=6)
    num_diff = len(set(dice_rolls))
    results[num_diff] += 1

probabilities = [i/num_trials for i in results]
print(probabilities)
