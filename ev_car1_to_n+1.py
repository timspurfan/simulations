from tqdm import tqdm
from random import randint
from numpy import mean
#from matplotlib import pyplot as plt

num_trials = 10**2
sizes = [i for i in range(50,301,50)]
results = []

def car_move_procedure(cars):

    #if cars[-1]==1:
    #    raise IndexError
    
    for i in range(len(cars)-2,-1,-1):
        if cars[i]==1 and cars[i+1]==0:
            #then we flip
            if randint(0,1)==1:
                cars[i] = 0
                cars[i+1] = 1
    
    return cars

for n in tqdm(sizes):
    temp_results = []
    for trial in tqdm(range(num_trials)):
        cars = [1 if i<n else 0 for i in range(0,2*n)]
        num_moves = 0
        while cars.index(1) != n:
            cars = car_move_procedure(cars)
            num_moves += 1
        temp_results.append(num_moves)
    results.append(mean(temp_results))

'''
for n in tqdm(sizes):
    temp_results = []
    for trial in tqdm(range(num_trials)):
        cars = [1 if i<n else 0 for i in range(0,2*n)]
        num_moves = 0
        while cars[::-1].index(1) != 0:
            cars = car_move_procedure(cars)
            num_moves += 1
        temp_results.append(num_moves)
    results.append(mean(temp_results))
'''

#plt.plot(sizes, results)
#plt.show()
for i in range(len(sizes)):
    #print(f'{sizes[i]}, {results[i]}')
    print(results[i]/sizes[i])