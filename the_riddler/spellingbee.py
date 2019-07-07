'''

Link:
https://fivethirtyeight.com/features/can-you-win-a-spelling-bee-if-you-know-99-percent-of-the-words/

'''

from tqdm import tqdm
from random import randint
from matplotlib import pyplot as plot

num_trials = 10**5
num_wins = [0 for i in range(10)]

def spell_word(player:int):
    return randint(1, 100) <= (player)

for trial in tqdm(range(num_trials)):
    players = [99-i for i in range(10)]
    #players = list(reversed(a))
    current_index = 0
    while len(players) > 1:
        if not spell_word(players[current_index]):
            del(players[current_index])
        current_index = (current_index + 1)%len(players)

    winner = players[0]
    num_wins[99-winner] += 1

print(num_wins)
print(num_wins[0]/num_trials)
plot.plot(num_wins)
plot.yscale('log')
plot.show()