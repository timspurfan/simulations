import random
from tqdm import tqdm
from numpy import mean

num_trails = 100000
results = []
num_flips = 4

for trial in tqdm(range(num_trails)):
    num_heads_1 = 0
    for i in range(num_flips):
        flip = random.randint(0,1)
        if flip == 1:
            num_heads_1 +=1
    
    num_heads_2 = 0
    for i in range(num_flips+1):
        flip = random.randint(0,1)
        if flip == 1:
            num_heads_2 +=1
    
    if num_heads_2 > num_heads_1:
        results.append(1)
    else:
        results.append(0)

prob = mean(results)
print(prob)