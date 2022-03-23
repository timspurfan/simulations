from tqdm import tqdm
from numpy import mean

'''
n_bullet problem simulation for even n
'''

even_n = [2*i for i in range(1,6)]
num_trials_per_n = 10**3

results = []

for n in even_n:
    results_per_n = []
    for trial in tqdm(range(num_trials_per_n)):


        results_per_n = []

return