'''
https://fivethirtyeight.com/features/how-low-can-you-roll/

10 sided die, (0-9)
Roll it until rolling a 0
Only keep rolls that are less than or equal to last kept roll
Each kept roll gets appended to end of number as decimal

Example: Suppose you roll the following: 6, 2, 5, 1, 8, 1, 0. 
After your first roll, your score would be 0.6, After the second, it’s 0.62. 
You ignore the third roll, since 5 is greater than the current last digit, 2. 
After the fourth roll, your score is 0.621. You ignore the fifth roll, 
since 8 is greater than the current last digit, 1. 
After the sixth roll, your score is 0.6211. 
And after the seventh roll, the game is over — 0.6211 is your final score.
'''

import random
from numpy import mean
from tqdm import tqdm

num_trials = 10**5
results = []

for trial in tqdm(range(num_trials)):

    num_rolls = 0.0
    current_number = 0
    last_kept = 10

    while True:
        roll = random.randint(0,9)
        num_rolls += 1
        if roll == 0:
            break
        if roll <= last_kept:
            last_kept = roll
            current_number += roll/(10**num_rolls)

    results.append(current_number)

ev = mean(results)
print(ev)

#.467
