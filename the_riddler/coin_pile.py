import random
from tqdm import tqdm
from numpy import mean

num_trials = 10**4

money = []
turns = []

coins = [1,5,10,25]

for trial in tqdm(range(num_trials)):

    amount = 0
    num_turns = 0
    
    amount += random.choice(coins)
    num_turns +=1

    while amount%100 != 0:
       amount += random.choice(coins)
       num_turns +=1
    
    money.append(amount)
    turns.append(num_turns)

print(mean(money))
print(mean(turns))