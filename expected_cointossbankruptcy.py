'''
http://www.cseblog.com/2011/02/coin-toss-bankruptcy.html

Problem: Three people start with integer amounts a,b and c. In each round, 
each one tosses a fair coin. If not all faces are the same, the person with 
the different face gets a rupee from each of the other two. If all faces are 
the same, no money is exchanged. This process is repeated till one of them 
gets bankrupt. What is the expected number of rounds till the game ends?

SOLUTION:
Y(n)= abc+(n)*(3/4)*[a+b+c-2] is a martingale with stopping time when abc = 0 for first time.
E[Y(T)] = 3/4 * E [T] *(a+b+c-2) and E[Y(T)] = Y(0) = abc
so
abc = 3/4 * E [T] *(a+b+c-2) and solve for E[T] = (4/3)*(abc)/(a+b+c-2)
'''

from tqdm import tqdm
from numpy import mean
import random

num_trials = 10**5
results = []

x,y,z = 3,4,5

actual_expected = (4/3)*(x*y*z)/(x+y+z-2)

for trial in tqdm(range(num_trials)):
    a,b,c, = x,y,z
    num_rounds = 0
    while a*b*c != 0:
        num_rounds +=1
        scenario = random.choice(['a','b','c','nothing'])
        if scenario == 'nothing':
            continue
        if scenario == 'a':
            a += 2
            b -= 1
            c -= 1
        if scenario == 'b':
            b += 2
            a -= 1
            c -= 1
        if scenario == 'c':
            c += 2
            a -= 1
            b -= 1
    results.append(num_rounds)

expected_num_rounds = mean(results)
print('Simulated expected number of rounds: {}'.format(expected_num_rounds))
print('Actual expected number of rounds: {}'.format(actual_expected))