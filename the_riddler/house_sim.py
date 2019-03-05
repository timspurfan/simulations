'''
ANSWER = .432(7ish)
'''

'''
simulation plan:

we have a road of n people (say 1000)

every iteration, a new creature will look at all of the houses which do not have a neighbor and
select randomly among those houses.

this process continues untill there are no more such houses (i.e. all houses now have neighbors)

we then want to compute the fraction of houses lived in...
'''

'''
implementation plan:

create a list with numbers from 1 through 1000
each iteration randomly select a number, delete it, and then delete the number above and below
it if they are still there.  add one to the counter
continue while len(list) != 0
return counter

'''

import random
import typing
from tqdm import tqdm

houses_to_choose_from = []
results = []

num_houses = 1000

for trial in tqdm(range(0,1000)):
    
    counter = 0
    
    for i in range(1,num_houses+1):
        houses_to_choose_from.append(i)
        
    while len(houses_to_choose_from) != 0:
        
        house = random.choice((houses_to_choose_from))

        houses_to_choose_from.remove(house)

        if house-1 in houses_to_choose_from:
            houses_to_choose_from.remove(house-1)

        if house+1 in houses_to_choose_from:
            houses_to_choose_from.remove(house+1)
    
        counter += 1
        #print(1-len(houses_to_choose_from))

    fraction = counter / num_houses
    results.append(fraction)
    
answer = (sum(results)/len(results))
print(answer)