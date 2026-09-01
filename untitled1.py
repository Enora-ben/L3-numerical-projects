# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 11:47:51 2025

@author: enora
"""

#Digramme de bifurcation sans condition sur t 
import numpy as np
import matplotlib.pyplot as plt
import math

# Paramètres constants
mu = 0.53           # Coefficient d'amortissement
A = 0.01             # Amplitude du plateau (en m)
g = 10               # Gravité
v0 = 0               # Vitesse initiale de la bille
z0 = 0               # Hauteur initiale de la bille
F = 25               # Fréquence de base

# Liste des pulsations
omega_list = np.linspace(0, 2 * F * np.pi, 1000)

# Durée maximale de simulation en secondes
t_max = 60
dt = 0.01

# Stocker les tau en fonction de omega
omega_values = []
tau_values = []

for omega in omega_list:
    t = 0
    z = z0
    v = v0
    last_bounce_time = 0
    Tc=(1/omega)*np.arcsin(g/(A*omega**2))

    while t < t_max:
        # Position et vitesse du plateau
        zp = A * np.sin(omega * t)
        vp = A * omega * np.cos(omega * t)

        # Mise à jour de la position et de la vitesse de la bille
        v -= g * dt
        z += v * dt

        # Détection du choc
        if z <= zp:
            v = vp - mu * (v - vp)  # vitesse bille après choc
            z = zp  # Repositionner la bille à la surface du plateau
            tau = t - last_bounce_time
            if tau > Tc : 
                omega_values.append(omega)
                tau_values.append(tau)

            last_bounce_time = t
                 
        t += dt        
       
       
   
# Tracé du diagramme de bifurcation
plt.figure(figsize=(10, 5))
plt.scatter(omega_values, tau_values, s=1, color="black")
plt.title(f"Diagramme de bifurcation (mu= {mu:.2f})")
plt.xlabel("Pulsation ω (rad/s)")
plt.ylabel("Temps entre les rebonds τ (s)")
plt.grid()
plt.show()