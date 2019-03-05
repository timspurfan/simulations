'''
q: in 5 flips of a coin, what is the expected amount of heads given there are more than two heads?
'''

import random

trials = 1000000
total_heads = 0
num_scenarios = 0

for i in range(trials):
    condition = False
    num_heads = 0
    for j in range(5):
        a = random.random()
        if a < .5:
            num_heads = num_heads + 1
    if num_heads >2:
        total_heads = total_heads + num_heads
        num_scenarios = num_scenarios + 1


conditional_prob = (total_heads/num_scenarios)

print(conditional_prob)
#3.47

#%%
print('jupyter test')