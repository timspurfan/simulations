'''
Determine the expected value of a roll in backgammon

Answer: 49/6

Solution:
Rolling two dice gives EV of 7.  Now, if there's doubles (which occur with prob = 1/36),
then we add that amount again.  So, EV = 7 + (1/36)*(2+4+...+12) = 49/6
'''

from random import randint
from tqdm import tqdm

num_trials = 10**5
total_sum = 0

for trial in tqdm(range(num_trials)):
    round_total = 0
    roll1 = randint(1,6)
    roll2 = randint(1,6)
    round_total = roll1 + roll2
    if roll1 == roll2:
        round_total *=2
    total_sum += round_total

ev = total_sum/num_trials
print(ev)