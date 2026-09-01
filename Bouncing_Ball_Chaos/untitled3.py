# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 12:10:55 2025

@author: enora
"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.animation as animation

# ignore warnings
import warnings
warnings.filterwarnings("ignore")

def logistic(r, x):
    """Implementation of the logistic map
    
    Args:
        x (float): previous value from 0 to 1
        r (float): the R paremter
    """
    return r * x * (1 - x)

n = 1000000  # total number of points
r = np.linspace(0.0, 10, n)
iterations = 100

x = np.random.uniform(0.0, 1.0, n)  # initial value
for _ in range(iterations):  # iterate
    x = logistic(r, x)

fig = plt.figure(figsize=(20, 10))
ax = plt.axes()

ax.set_title(f"Bifurcation Diagram for $x^{{(r)}}_{{n + 1}} = rx^{{(r)}}_{{n}}(1 - x^{{(r)}}_{{n}})$ for $n=${iterations}", fontsize=24)
ax.set_xlabel('r', fontsize=24)
ax.set_ylabel('$x^{(r)}_{n}$', fontsize=24)
ax.tick_params(axis='both', which='major', labelsize=18)
ax.set_xlim(0.0, 4.0)
ax.set_ylim(0.0, 1.0)
plt.gcf().text(0.13, 0.15, 'by Vladimir Ilievski', fontsize=22, fontfamily='Verdana')

ax.plot(r, x, ',b', alpha=.5)
plt.savefig('bifurcation.png', bbox_inches='tight')