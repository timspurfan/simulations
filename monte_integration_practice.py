'''
monte carlo for integration
'''
from math import sin, pi
import random
from tqdm import tqdm
from numpy import mean

x_min, x_max = 0, 2*pi

def f(x):
    return sin(x)

num_steps = 10000

y_min = f(x_min)
y_max = f(x_min)
current = x_min
jump = (x_max-x_min)/num_steps

for step in tqdm(range(num_steps)):
    current += jump
    y = f(current)
    if y<y_min:
        y_min = y
    if y>y_max:
        y_max = y
# we now now max and min of function on the interval
# can use this to create rectangle we will randomly sample from

rectangle_area = (x_max-x_min)*(y_max-y_min)

num_points = 1000000
counter = 0 #could use list with numpy mean instead

for point in tqdm(range(num_points)):
    x = random.uniform(x_min,x_max)
    y = random.uniform(y_min,y_max)
    if 0<y<f(x):
        counter+=1
    if 0>y>f(x):
        counter-=1

integral = (counter/num_points) * rectangle_area #fraction of the total area
print(integral)