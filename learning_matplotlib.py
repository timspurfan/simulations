'''
learning to use basics of matplotlib
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, num=256, endpoint=True)
def f(x):
    return -x

def g(x):
    return x**2

a = np.linspace(-100,100,10**2)

f = f(a)

plt.plot(a,f)
plt.show()

