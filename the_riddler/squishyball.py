import random
from tqdm import tqdm
from numpy import mean
from matplotlib import pyplot as plt


num_trials = 10**5

#wins_needed = 30

num_wins = 0
games_needed_to_win = []
anytime_num_games = []

amount_of_money_won = [[] for i in range(1,52)]
amount_of_money_won[0].append(0)


for wins_needed in tqdm(range(1, 51)):

    for trial in tqdm(range(num_trials)):
        your_wins = 0
        opp_wins = 0
        while your_wins<wins_needed and opp_wins<wins_needed:
            game = random.random()
            if game <= .6:
                your_wins += 1
            else:
                opp_wins += 1
        
        if your_wins == wins_needed:
            #num_wins += 1
            #games_needed_to_win.append(your_wins+opp_wins)
            amount_of_money_won[wins_needed].append(10**6-(10**4)*(your_wins+opp_wins))
        else:
            amount_of_money_won[wins_needed].append(0)

        #anytime_num_games.append(your_wins+opp_wins)

results = [mean(x) for x in amount_of_money_won]

plt.plot(results)
plt.show()

#print(num_wins/num_trials)
#print(mean(games_needed_to_win))
#print(mean(anytime_num_games))
