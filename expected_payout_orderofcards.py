'''
Problem: (http://www.cseblog.com/2010/12/order-of-cards.html)

I have ten cards, Ace,2,3,4,5,6,7,8,9,10. The value of the Ace is 1.

They’re shuffled, then dealt one by one, face up. For the first card, 
you automatically win $10. For the next 9 cards, if the card face-up is 
greater than every previous card, you win $10 more.

What is the expected winning amount?

Clarification:
1) Game does not end when you draw a card that is not a winning card. ie, if 
I pick a 5 first, then a 6, then a 4, the game is not over. I keep drawing 
until all of the cards are gone
2) It might be useful to know that the chance of winning $100 is 1/10!, 
because the cards will have to be drawn in the order: {A, 2, 3, 4 … , 9, 10}.

Answer: 10*(H(10)) where H(10) is the 10th harmonic number

Solution: 


'''
from tqdm import tqdm
import random
from numpy import mean

num_trials = 10**5
#results = []
total_earnings = 0

for trial in tqdm(range(num_trials)):
    deck = [i for i in range(1,11)]
    shuffled = deck
    random.shuffle(shuffled)
    temp_max = 0
    earnings = 0
    for card in shuffled:
        if card > temp_max:
            earnings += 1
            temp_max = card
    total_earnings += earnings

expected_earnings = total_earnings/num_trials
print('expected earnings: {}'.format(expected_earnings))

