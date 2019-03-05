'''
https://www.glassdoor.com/Interview/Play-a-game-with-an-urn-75-blue-balls-25-red-balls-1-yellow-ball-you-get-a-dollar-for-every-red-and-if-you-select-the-y-QTN_424510.htm
'''

from tqdm import tqdm
import random
from numpy import mean

payouts = [[] for i in range(26)]
payouts[0] = 0
num_trials = 10**5

for trial in tqdm(range(num_trials)):
    urn = [i for i in range(1,27)] #1 is yellow, 2-26 are red
    payout = 0 #equal to red balls drawn
    while 1 in urn:
        draw = random.choice(urn)
        urn.remove(draw)
        if draw != 1:
            payout +=1
    for strategy in range(1, len(payouts)):
        if payout >= strategy:
            payouts[strategy].append(strategy)
        else:
            payouts[strategy].append(0)

expected_values = [mean(strat) for strat in payouts]
print(expected_values)
print('Max is at {}'.format(expected_values.index(max(expected_values))))

#
#
#
#
#

payouts = [[] for i in range(26)]
payouts[0] = 0
num_trials = 10**4

for trial in tqdm(range(num_trials)):
    urn = [i for i in range(1,102)] #1 is yellow, 2-26 are red, 27-101 are blue
    payout = 0 #equal to red balls drawn
    while 1 in urn:
        draw = random.choice(urn)
        urn.remove(draw)
        if 1<draw<27:
            payout +=1
    for strategy in range(1, len(payouts)):
        if payout >= strategy:
            payouts[strategy].append(strategy)
        else:
            payouts[strategy].append(0)

expected_values = [mean(strat) for strat in payouts]
print(expected_values)
print('Max is at {}'.format(expected_values.index(max(expected_values))))