from tqdm import tqdm
import random
from numpy import mean

num_trials = 10**5
results = []

def is_waiting_for_Tiffany():
    return random.randint(1,4) == 1

def time_left():
    times = []
    for _ in range(4):
        times.append(15*random.random())
    return times

for trial in tqdm(range(num_trials)):

    wait_time = 0.0
    barber_times = time_left()
    #print(barber_times)

    if is_waiting_for_Tiffany():
        #print("Is Waiting")
        wait_time = barber_times[0]+15

    else:
        if barber_times[0] == min(barber_times):
            wait_time = barber_times[0]+15
        
        else:
            wait_time = barber_times[0]

    #print(wait_time)
    results.append(wait_time)

print(mean(results))