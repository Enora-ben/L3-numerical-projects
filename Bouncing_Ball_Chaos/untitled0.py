# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 10:46:13 2025

@author: enora
"""

import numpy as np
import matplotlib.pyplot as plt

# Paramètres du système
g = 10          # Gravité (m/s^2)
F = 10         # Fréquence du plateau (Hz)
mu = 0.53       # Coefficient d'amortissement
A = 0.01        # Amplitude du plateau (m)
omega = 2 * np.pi * F
k = 10          # Raideur du ressort (N/m)
L0 = 0.05       # Longueur au repos du ressort (m)
m = 0.2         # Masse des billes (kg)

# Temps de simulation
t_max = 10
dt = 0.005
t_vals = np.arange(0, t_max, dt)

# Position et vitesse du plateau
def y_plateau(t):
    return A * np.sin(omega * t)

def v_plateau(t):
    return A * omega * np.cos(omega * t)

# Conditions initiales
y1_0, v1_0 = 0, 0.2
y2_0, v2_0 = 0, 0.25
state = np.array([y1_0, v1_0, y2_0, v2_0])

# Stockage des résultats
positions_1 = []
positions_2 = []
times = []

# Boucle de simulation
for t in t_vals:
    y1, v1, y2, v2 = state

    # Distance et force du ressort
    dy = y2 - y1
    distance = abs(dy)
    F_ressort1 = -k * (distance - L0)   # Force sur bille 1
    F_ressort2 = k * (distance - L0)    # Force sur bille 2

    # Accélérations avec ressort
    a1 = -g + F_ressort1 / m    # accélaration bille 1
    a2 = -g + F_ressort2 / m    #acceleration bille 2

    # Intégration (nouvelles vitesses et positions)
    v1_new = v1 + a1 * dt
    v2_new = v2 + a2 * dt
    y1_new = y1 + v1 * dt
    y2_new = y2 + v2 * dt

    # Plateau à l'instant t
    y_p = y_plateau(t)
    v_p = v_plateau(t)

    # Collision bille 1
    if y1_new <= y_p:# and v1 < v_p:
        v1_new = (1 + mu) * v_p - mu * v1
        y1_new = y_p

    # Collision bille 2
    if y2_new <= y_p:# and v2 < v_p:
        v2_new = (1 + mu) * v_p - mu * v2
        y2_new = y_p

    # Mise à jour de l'état
    state = np.array([y1_new, v1_new, y2_new, v2_new])
    positions_1.append(y1)
    positions_2.append(y2)
    times.append(t)

# Affichage des résultats
plt.figure(figsize=(10, 6))
plt.plot(times, positions_1, label='Bille 1')
plt.plot(times, positions_2, label='Bille 2')
plt.plot(times, [y_plateau(ti) for ti in times], label='Plateau')
plt.xlabel('Temps (s)')
plt.ylabel('Hauteur (m)')
plt.title('Simulation : Deux billes reliées par un ressort rebondissant sur un plateau oscillant')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
