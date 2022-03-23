'''
Problem: There is a big line of people waiting outside a theater for buying tickets. 
The theater owner comes out and announces that the first person to have a birthday 
same as someone standing before him in the line gets a free ticket. Where will you 
stand to maximize your chance.

Source: Zhou pg.77 (also http://www.cseblog.com/2011/01/birthday-game.html)

Answer: 20th

Solution: Let p(n) be the probability 

'''
#insert random comment

from tqdm import tqdm
import random

num_wins_at_position = [0]*365

num_trials = 1*10**6

for trial in tqdm(range(num_trials)):

    bdays = set()
    num_people = 0

    while True:
        bday = random.randint(1,365)
        num_people += 1
        if bday in bdays:
            num_wins_at_position[num_people] += 1
            break
        else:
            bdays.add(bday)

best_spot = num_wins_at_position.index(max(num_wins_at_position))

print(num_wins_at_position[0])
print(num_wins_at_position[1])
print(num_wins_at_position[2])

print('Best spot to be is: {}'.format(best_spot))