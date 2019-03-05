'''
N_1 = 10^100.
N_2 = random number picked from 1 to N_1.
...
N_k = random number picked from 1 to N_(k-1).

For what k do you expect to see N_k = 1?

Seems like each time we cut the search space in half so should be nearish log(N_1)+1
perhaps a little less since when it gets smaller there's a decent chance we will randomly
select 1.
'''

from tqdm import tqdm
from numpy import mean
import random

num_trials = 100000
results = []
power = 7

for trial in tqdm(range(num_trials)):
    selection = 10**power
    k = 0
    while selection != 1:
        selection = random.randint(1,selection)
        k += 1
    results.append(k)

expected = mean(results)
print(expected)