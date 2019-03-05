'''
QUESTION
Roll a die.  If the roll is !=6, then the put grows by that much.  Roll a 6 and lose everything
You can either roll again or take your earnings

How much should you pay to play the game?
'''

'''
SOLUTION
You will keep rolling as long as the EV rolling again at $n > $n
EV(n) = 1/6(n+1 + n+2 + ... + n+5) > n
This holds true when n<=14.  So will roll as long as total is less than 14
When n>14, EV(n) = n
'''
#init list
expected_value_list = [0 for i in range(20)]

#When n>14, EV(n) = n
for i in range(15, 20):
    expected_value_list[i] = i

#dynamic programming
for i in range(14,-1,-1):
    expected_value_list[i] = (1/6)*sum(expected_value_list[i+1:i+6])

print(expected_value_list[0])