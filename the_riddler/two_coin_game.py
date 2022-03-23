'''
DP Problem

2 point vs 1 point coin
'''
#from tqdm import tqdm
#from numpy import mean
#import random

dp = {} #(flips_left,score)

for score in range(-200,201):
    if score > 0 :
        dp[(0,score)] = 1
    else:
        dp[(0,score)] = 0

for flips_left in range(1,101):
    for score in range(-200+2*flips_left,201-2*flips_left):
        dp[(flips_left,score)] = max(
            ((1/2)*dp[flips_left-1,score+2]+(1/2)*dp[flips_left-1,score-2]),
            ((1/2)*dp[flips_left-1,score+1]+(1/2)*dp[flips_left-1,score-1]))

print(dp[(100,0)])