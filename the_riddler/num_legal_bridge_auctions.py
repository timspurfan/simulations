'''
Source: https://fivethirtyeight.com/features/youre-home-alone-you-can-buy-zillions-of-video-game-cigarettes-or-beat-yourself-at-bananagrams/

Problem: Bridge is played with a deck of 35 cards (for our sake numbered 1-35)
An auction is started and completed when someone bets and everyone else passes (or everyone 
passes at the beggining).  How many auctions are possible.

A: 1,574,122,160,956,548,404,565

There's a reasonable counting argument.

This is my attempt at a DP solution.
'''

num_actions_at_n = [0 for i in range(36)]
num_actions_at_n[35] = 1
for n in range(34,-1,-1):
    actions_for_this_n = 1
    for sub_n in range(n+1,36):
        actions_for_this_n += 3*num_actions_at_n[sub_n]
    num_actions_at_n[n] = actions_for_this_n
#num_actions_at_n[0] += num_actions_at_n[1]

#print(num_actions_at_n[0])
#print(num_actions_at_n[0]-1574122160956548404565)
#print(num_actions_at_n)
ans = (4/3)*(num_actions_at_n[0]-1)+1
print(ans)
assert ans - 1574122160956548404565 < 1