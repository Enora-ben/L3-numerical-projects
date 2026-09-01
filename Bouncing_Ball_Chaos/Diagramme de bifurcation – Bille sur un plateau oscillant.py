# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 20:11:19 2025

@author: enora
"""

import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# --- Paramètres physiques du système ---
mu = 0.53
A = 0.01
g = 10
z0 = 0
v0 = 0
t_max = 80        # Allongé légèrement pour permettre plus de rebonds
dt = 0.001

omega_list = np.linspace(0, 70, 1000)

omega_values = []
tau_values = []

for omega in omega_list:
    t = 0
    z = z0
    v = v0
    last_bounce_time = 0
    bounces = []

    if A * omega**2 > g:
        try:
            Tc = (1 / omega) * np.arcsin(-g / (A * omega**2))
        except ValueError:
            continue  # arcsin hors domaine
    else:
        continue

    while t < t_max:
        zp = A * np.sin(omega * t)
        vp = A * omega * np.cos(omega * t)

        v -= g * dt
        z += v * dt

        if z <= zp:
            tau = t - last_bounce_time
            if tau >= Tc:
                bounces.append(tau)
                last_bounce_time = t  # Corrigé : MAJ uniquement si rebond valide

            v = vp - mu * (v - vp)
            z = zp

        t += dt

    if len(bounces) > 30:  # 🔧 plus souple ici
        omega_values.extend([omega] * 30)
        tau_values.extend(bounces[-30:])

# --- Affichage ---
plt.figure(figsize=(20, 10))
plt.plot(omega_values, tau_values, '.k', alpha=1)
plt.title("Diagramme de bifurcation – Bille sur un plateau oscillant", fontsize=24)
plt.xlabel("Pulsation $\\omega$ (rad/s)", fontsize=20)
plt.ylabel("Temps entre deux rebonds $\\tau_n$ (s)", fontsize=20)
plt.grid(True)
plt.tight_layout()
plt.show()
