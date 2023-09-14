import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import pandas as pd

x = random.randint(10, size=(10))
x = x + 3
print(x)
y = random.randint(10, size=(10))
y = y + 3
print(y)

m1x = np.mean(x)
m2x = np.median(x)
print(m1x)
print(m2x)

m1y = np.mean(y)
m2y = np.median(y)
print(m1y)
print(m2y)

plt.style.use('dark_background')
plt.plot(x, y, 'or', ms = 7)
plt.axis([0, 20, 0, 20])
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), linewidth = '5')

plt.show()


'''
x = random.randint(10, size=(9))
y = random.randint(10, size=(9))
plt.scatter(x,y)

x = random.randint(10, size=(9))
y = random.randint(10, size=(9))
plt.scatter(x,y)

plt.show()
'''