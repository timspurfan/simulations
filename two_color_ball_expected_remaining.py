'''
Problem: You have a bin containing 2n balls, n of which are blue and n of which are red.
You randomly select a ball from the bin and then remove a ball of the opposite color
(and place the ball you selected back in the bin).

Find the expected amount of balls in the bin when there is only one color reminaing.
'''

import random
from tqdm import tqdm
from numpy import mean
from matplotlib import pyplot as plt

num_trials = 10**3
#num_of_each = 100

nums = []
means = []

for num_of_each in tqdm(range(1,501, 5)):

    num_balls_remaining = []

    for trial in tqdm(range(num_trials)):

        num_blue, num_red = num_of_each, num_of_each
        
        while num_blue >0 and num_red >0:

            choice = random.randint(1,num_blue+num_red)
            if choice<=num_blue:
                num_red -= 1
            else:
                num_blue -= 1
        
        num_balls_remaining.append(num_blue+num_red)

    nums.append(num_of_each)
    means.append(mean(num_balls_remaining))

#print(mean(num_balls_remaining))

plt.plot(nums, means, 'r')
f = [x**(3/4) for x in nums]
plt.plot(nums, f, 'b')
ratio = [x/y for x,y in zip(means,f)]
plt.show()
plt.plot(nums, ratio, 'g')
plt.show()