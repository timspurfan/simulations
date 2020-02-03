'''
https://fivethirtyeight.com/features/can-you-track-the-delirious-ducks/
'''
import typing
from tqdm import tqdm
import random
from numpy import mean


## SETUP
num_trials = 10**5
results = []

#is there a cleaner way to do this?
adjacencty_dict = {
    (0,0): [(-1,0),(0,1),(1,0),(0,-1)],
    (1,0): [(0,0),(1,1),(1,-1)],
    (0,1): [(0,0),(1,1),(-1,1)],
    (-1,0): [(0,0),(-1,1),(-1,-1)],
    (0,-1): [(0,0),(1,-1),(-1,-1)],
    (1,1): [(1,0),(0,1)],
    (1,-1): [(1,0),(0,-1)],
    (-1,-1): [(-1,0),(0,-1)],
    (-1,1): [(-1,0),(0,1)],    
    }


def jump(current_pos):
    new_pos = random.choice(adjacencty_dict[current_pos])
    return new_pos

for trial in tqdm(range(num_trials)):

    a_pos = (0,0)
    b_pos = (0,0)
    num_jumps = 0

    a_pos = jump(a_pos)
    b_pos = jump(b_pos)
    num_jumps += 1

    while a_pos != b_pos:
        a_pos = jump(a_pos)
        b_pos = jump(b_pos)
        num_jumps += 1

    results.append(num_jumps)

print(mean(results))
    