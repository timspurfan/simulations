'''

Link:
https://fivethirtyeight.com/features/can-you-win-a-spelling-bee-if-you-know-99-percent-of-the-words/

'''

from tqdm import tqdm
from random import randint

num_trials = 10**5
num_wins = [0 for i in range(10)]

for trial in tqdm(range(num_trials)):
    players = [i for i in range(10)]
    while len(players) > 0:
        pass



def spell_word(player:int):
    return randint(1, 100) < (100 - (player+1))