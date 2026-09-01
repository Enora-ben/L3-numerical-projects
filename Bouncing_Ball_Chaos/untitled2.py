# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 12:05:28 2025

@author: enora
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

plt.figure(figsize=(45, 25))

t=range(1,101)
p = [0] * 200
r = [0] * 5000

p[0]=0.4
for m in range(5000):
    r[m]=m*0.001
for q in range(5000):
    temp=[r[q]]*100
    temp2=[0]*100
    for i in range(1,200):
        p[i]=r[q]*p[i-1]*(1-p[i-1])
        if(i>99):
            temp2[i-100]=p[i]
    plt.scatter(temp, temp2,color = 'black',s=1)
            
# Plot
plt.title(label="Bifurcation Diagram",fontsize=40,)
plt.xlim([0.7, 4])
plt.ylim([0, 1])
plt.show()