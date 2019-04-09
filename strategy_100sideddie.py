'''
http://www.cseblog.com/2013/04/100-sided-die-probability-problem.html

Problem:
You are given a 100 sided die. After you roll once, you can choose to either get paid 
the dollar amount of that roll OR pay one dollar for one more roll. 
What is the expected value of the game?
(There is no limit on the number of rolls.)

Answer:
87
(continuous solution gives 86.6ish)

Solution:
Suppose game has EV = E.  Then will roll again if roll is less than E-1.  For simplicty, rather than drawing from the discrete distribution, let's suppose that our die gives a uniform distribution between [0,100].  Thus, the probability our roll is less than E-1 is
(E-1)/100.  So, we have the following relation: 
E = (E-1)/(100) * (E-1) + (100-E+1)/(100) * (100+E-1/2).
The first case is the probability of rolling a number below E-1, which would cause us to
re-roll, and then resulting in an EV of E-1 (Since you're playing the same game but now down $1).
The second case 
re-rolling * ev of re-rolling and the second is the prob of not re
Solving for E in (0,100) gives 86.86ish.
'''

'''
Simulate all strategies and show that this is highest expected value.
'''

import random
from numpy import mean
from tqdm import tqdm

people = [i for i in range(1,101)]
results = [] #going to be 