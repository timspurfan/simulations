import random
from tqdm import tqdm
from numpy import mean

strategies = [i for i in range(1,7)] #stop if u get 1, 2, 3, 4, 5, 6
num_trials = 1000000
results = [[] for i in range(6)]

for trial in tqdm(range(num_trials)):
    playing = [True for i in range(6)]
    roll_1 = random.randint(1,6)
    for strategy in strategies:
        if roll_1>=strategy:
            results[strategy-1].append(roll_1)
            playing[strategy-1]=False
    roll_2 = random.randint(1,6)
    for strategy in strategies:
        if playing[strategy-1]==True:
            results[strategy-1].append(roll_2)

ev = [mean(result) for result in results]
print(ev)