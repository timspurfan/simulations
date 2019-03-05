'''
http://www.cseblog.com/2013/04/100-sided-die-probability-problem.html

Problem:
You are given a 100 sided die. After you roll once, you can choose to either get paid 
the dollar amount of that roll OR pay one dollar for one more roll. 
What is the expected value of the game?
(There is no limit on the number of rolls.)

Answer:
87
(continuous solution gives 86.6ish...suppose game has EV = E...then will roll again if 
roll is less than E-1)
'''

'''
Simulate all strategies and show that this is highest expected value.
'''

import random
from numpy import mean
from tqdm import tqdm

people = [i for i in range(1,101)]
results = [] #going to be 