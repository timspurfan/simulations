import random
from tqdm import tqdm

num_trials = 10**5

num_people = 13
results = [0 for i in range(num_people)]

for trial in tqdm(range(num_trials)):
    visited = set()
    current_person = 0
    visited.add(current_person)
    while visited != set(range(num_people)):
        to_do = random.choice([-1,1])
        current_person = (current_person + to_do)%num_people
        visited.add(current_person)
    results[current_person] += 1
    

prob = [i/num_trials for i in results]
print(prob)