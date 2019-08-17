'''
You have unlimited amounts of pennies, nickels, dimes, and quarters.  Each second you randomly
grab a coin and add it to your pile.  What is the expected amount of time until your pile's
worth an even dollar amount, and what is the EV of the pile?

Source: OMO?
'''
import random
from tqdm import tqdm
from numpy import mean

num_trials = 10**5
times = [0 for i in range(num_trials)]
val = [0 for i in range(num_trials)]
coins = [1,5,10, 25]

for trial in tqdm(range(num_trials)):
    pile = 0
    time = 0
    while pile == 0 or pile%100 != 0:
        pile += random.choice(coins)
        time += 1
    times[trial] = time
    val[trial] = pile

print(mean(times)) #ev = 100
print(mean(coins)) #ev = 10.25
        