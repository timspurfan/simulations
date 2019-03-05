import random

def prob_acquitted(n, p):
    num_trials = 1000
    results = []
    for trial in range(num_trials):
        count = 0
        for person in range(n):
            a = random.random()
            if a<p:
                count +=1
            
        if count<n and count>n/2:
            results.append(1)
    prob = sum(results)/num_trials
    return prob

print(prob_acquitted(3,2/3))