'''
Problem: Select random numbers uniformly from 0 to 1 until the sum is greater than 1
What is the EV of the number that set the sum greater than 1?

Source: https://mindyourdecisions.com/blog/2014/04/07/monday-puzzle-the-straw-that-broke-the-camels-back/
'''

from tqdm import tqdm
import random
from math import e
from numpy import mean

numbers_to_set_over = []
num_trials = 10**5

for trial in tqdm(range(num_trials)):
    sum = 0
    while sum<1:
        num = random.random()
        sum += num
    numbers_to_set_over.append(num)

expected = mean(numbers_to_set_over)

assert abs(expected - (2-e/2)) < .01

print(expected)
