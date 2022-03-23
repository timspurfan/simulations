from tqdm import tqdm
from numpy import mean
import random

num_two = 0
num_rolls = 200000

for roll in tqdm(range(num_rolls)):
    roll = random.randint(1,6)
    if roll == 6:
        num_six +=1

prob_six = num_six/num_rolls
print(prob_six)