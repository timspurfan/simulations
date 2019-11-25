'''
https://fivethirtyeight.com/features/who-will-win-the-lucky-derby/

200 meters, 20 horses (52,54,...90 percent of taking step right)
Find the odds
'''

import random
from tqdm import tqdm

horse_probs = [52+2*i for i in range(20)]
assert (horse_probs[0]==52 and horse_probs[-1]==90)

num_wins = [0 for i in range(20)]

num_trials = 10**3
finish_line = 200

for trial in tqdm(range(num_trials)):
    horse_positions = [0 for i in num_wins]
    while max(horse_positions) != finish_line:
        for i, position in enumerate(horse_positions):
            if random.randint(1,100) <= horse_probs[i]:
                horse_positions[i] += 1
            else:
                horse_positions[i] -= 1

    num_wins[horse_positions.index(200)] += 1

prob_winning = [val/num_trials for val in num_wins]
#print(prob_winning)
print(num_wins)