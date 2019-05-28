'''

Source: https://fivethirtyeight.com/features/does-your-gift-card-still-have-free-drinks-on-it/

Problem: Lucky you! You’ve won two gift cards, each loaded with 50 free drinks from your 
favorite coffee shop, Riddler Caffei-Nation. The cards look identical, and because you’re 
not one for record-keeping, you randomly pick one of the cards to pay with each time you get 
a drink. One day, the clerk tells you that he can’t accept the card you presented to him 
because it doesn’t have any drink credits left on it.

What is the probability that the other card still has free drinks on it? How many free 
drinks can you expect are still available?

'''

from tqdm import tqdm
from random import choice
from numpy import mean

num_trials = 10**5
num_successes = 0
num_left = [0]*num_trials

for trial in tqdm(range(num_trials)):
    a,b = 50,50
    while True:
        card = choice(['a','b'])
        if card == 'a': #card a
            if a == 0:
                if b != 0: 
                    num_successes += 1
                num_left[trial] = b
                break
            else:
                a -= 1
        else:
            if b == 0:
                if a != 0: 
                    num_successes += 1
                num_left[trial] = a
                break
            else:
                b -= 1

prob = num_successes/num_trials
expected = mean(num_left)

print('prob = {}'.format(prob))
print('expected = {}'.format(expected))
