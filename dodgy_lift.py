'''

Source: https://brilliant.org/problems/dodgy-lift-1/

You are on the 2nd/top floor of a building and you wish to ride the elevator to the 
0th/ground floor. Unfortunately the elevator is dodgy, and regardless of what buttons 
are pressed always carries out the following actions that are possible, after every 10 seconds, 
with equal probability: (eg after the first 10 seconds, you move down or open the doors 
with probability 0.5).

    Move up 1 floor.
    Move down 1 floor.
    Open the doors.

Let  be the probability that the first time the doors open you are on the ground floor.

The doors end up opening first on the ground floor.

Let  be the expected amount of time taken in minutes.

'''

from tqdm import tqdm
import random
from numpy import mean


num_trials = 10**5
num_successes = 0
time_per_success = []


for trial in tqdm(range(num_trials)):
    #print(trial)
    currrent_door = 2
    doors_open = False
    time = 0
    while not doors_open:

        if currrent_door == 2:
            choice = random.choice([-1,0])

        if currrent_door == 1:
            choice = random.choice([-1,0,1])
        
        if currrent_door == 0:
            choice = random.choice([0,1])

        if choice == 0:
            doors_open = True
        else:
            currrent_door += choice
        time += 10
    
    if currrent_door == 0:
        num_successes += 1
        time_per_success.append(time)


prob = num_successes/num_trials
print(prob)
expected = mean(time_per_success)
print(expected)
