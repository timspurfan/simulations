'''
Source:
https://fivethirtyeight.com/features/pick-a-card-any-card/
'''

'''
Compute probability that this card is highest and if it is >.5 then accept it
'''

import random
from tqdm import tqdm
#from numpy import mean
from itertools import combinations

deck = [i for i in range(1,101)]
num_trials = 10**4
num_successes = 0

for trial in tqdm(range(num_trials)):

    ten_cards = random.sample(deck, 10)
    seen_so_far = [0]

    def prob(card):
        num_cards_left = 10-len(seen_so_far)
        prob = 1
 #       for card_left in range(num_cards_left):
 #           prob*=(card-len(seen_so_far))/
        

    for card in ten_cards:
        if card>max(seen_so_far) and prob(card)>.5:
            selected = card
            break
    
    if selected == max(ten_cards):
        num_successes += 1

print(num_successes/num_trials)

        