'''
n balls n different colors

each time choose one then choose another and paint the second one the color of the first
expected amount of choosings

apparently the answer is (n-1)^2

let's try 8 balls
'''

import random
from numpy import mean
from tqdm import tqdm

num_trails = 10000
bowl_size = 15
results = []

for trial in tqdm(range(num_trails)):
    bowl = [n for n in range(1,bowl_size+1)]
    num_chooses = 0
    while bowl.count(bowl[0]) != bowl_size:
        #first choice
        first, second = random.sample(range(0,bowl_size),2)
        num_chooses += 1
        bowl[second] = bowl[first]

    results.append(num_chooses)

expected = mean(results)

print(expected)