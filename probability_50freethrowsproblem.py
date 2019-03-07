'''
A person shoots two free throws, making the first and missing the second.
For every subsequent free throw, the probability of making the i'th free throw is
#madefreethrows/(i-1).  For example, there is a 1/2 chance of making the third freethrow.

What is the probability of making exactly 50 free throwsafter 100 freethrows?
Source: Practical Guide to Quant Interviews

A: 1/99
Solution:

#TODO: Random: Isn't this similar to reservoir sampling?
'''
from tqdm import tqdm
import random
from matplotlib import pyplot as plt

results = [[0 for j in range(i+1)] for i in range(101)]
num_trials = 10**5

for trial in tqdm(range(num_trials)):
    made = 1
    taken = 2
    while taken<100:
        shot = random.randint(1,taken)
        if shot <= made:
            made += 1
        taken += 1
        results[taken][made] +=1
    
print(len(results[100]))
hundredth_shot = [freq/num_trials for freq in results[100]]
print(hundredth_shot)

plt.plot(hundredth_shot[1:100])
plt.show()