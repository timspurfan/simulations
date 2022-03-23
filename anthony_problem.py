'''
Find the expected value of the following game:

You roll a die.  You may choose to either be paid the amount of the roll or
roll again.  If you roll again, you must accept the second roll amount.

Answer: $4.25

Solution:
If you roll the second time, your expected value is 3.5.  Thus, if your 
first roll is greater than 3.5, you will keep it.  Else, if it is below, 
you will re-roll.  This gives the following relation:
EV = (1/2)(5) + (1/2)(3.5) = 4.25
The first part is because there is a 1/2 chance of rolling a 4, 5, or 6
(greater than 3.5).  In this case, your EV is 5.  The second is from the
1/2 chance of rolling a 1, 2, or 3 and rerolling, giving an EV of 3.5.
'''

import random
from tqdm import tqdm
from numpy import mean

strategies = [i for i in range(1,7)] #stop if u get 1, 2, 3, 4, 5, 6
num_trials = 1000000
results = [[] for i in range(6)]

for trial in tqdm(range(num_trials)):
    playing = [True for i in range(6)]
    roll_1 = random.randint(1,6)
    for strategy in strategies:
        if roll_1>=strategy:
            results[strategy-1].append(roll_1)
            playing[strategy-1]=False
    roll_2 = random.randint(1,6)
    for strategy in strategies:
        if playing[strategy-1]==True:
            results[strategy-1].append(roll_2)

ev = [mean(result) for result in results]
print(ev)

ev = max(ev)
print('Expected Value is {}'.format(ev))