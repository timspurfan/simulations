'''
Source: http://www.cseblog.com/2010/10/random-walk-around-square.html

Problem: Consider a random walk around the edges of a square. From any vertex,
the probability of moving to any adjacent vertex is 0.5. Suppose the walk stops
as soon as after all traversing through all the vertices, you return to your 
starting vertex. What is the expected path length?

Answer: 28/9
Solution:
'''
from tqdm import tqdm
import random
from numpy import mean

results = []
num_trials = 10**6
#states = {'a','b','c','d'}
#we can think of the the vertices as values modulo 4! :)
#clockwise will be adding 1 and counter clockwise subtract one

for trial in tqdm(range(num_trials)):
    current_state = 0
    states_hit = {0}
    num_steps = 0

    while not (current_state == 0 and states_hit == {0,1,2,3}):
        direction_to_go = random.choice([-1,1])
        current_state = (current_state + direction_to_go)%4
        num_steps +=1
        states_hit.add(current_state)
    
    results.append(num_steps)

expected_num_steps = mean(results)
print('Simulated expected number of steps: {}'.format(expected_num_steps))