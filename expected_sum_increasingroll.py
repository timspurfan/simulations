from tqdm import tqdm
from numpy import mean
import random

num_trials = 200000
sum_results = []
num_rolls_results = []

for trial in tqdm(range(num_trials)):
    game_rolls = []
    roll = random.randint(1,6)
    game_rolls.append(roll)

    while True:
        roll = random.randint(1,6)
        if roll <= game_rolls[-1]:
            sum_results.append(sum(game_rolls))
            num_rolls_results.append(len(game_rolls))
            break
        else:
            game_rolls.append(roll)
    
expected_sum = mean(sum_results)
print('expected sum = {}'.format(expected_sum))
expected_num_rolls = mean(num_rolls_results)
print('expected rolls = {}'.format(expected_num_rolls))




        
