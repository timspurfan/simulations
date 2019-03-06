'''
Simulate a six sided die with a coin flip (/random number generator)

Source: https://www.glassdoor.com/Interview/Simulate-a-6-sided-die-with-a-coin-QTN_152964.htm

Solution:
TODO: Solution+Documentation of functions
'''
import random
from tqdm import tqdm

def coin_flip():
    return random.choice(['Heads','Tails'])

def map_flip(flip):
    return int(flip == 'Heads') #1 if heads, 0 if tails

def three_flips():
    results = []
    for _ in range(3):
        results.append(coin_flip())
    return results

def flips_to_num(results):
    num_results = [str(map_flip(flip)) for flip in results]
    num_string = ''.join(num_results)
    flip_val = int(num_string,2)+1
    return flip_val

def simulate_die():
    roll = 7
    while roll > 6:
        roll = flips_to_num(three_flips())
    return roll

if __name__ == "__main__":
    
    frequency = [0 for i in range(6)]
    num_trials = 10**5

    for trial in tqdm(range(num_trials)):
        roll = simulate_die()
        frequency[roll-1] +=1

    frequency_prob = [i/num_trials for i in frequency]
    print(frequency_prob)

'''
Bonus: https://connect2ppl.wordpress.com/2009/11/21/probability-question-2/#comments
'''