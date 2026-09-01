# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 20:43:41 2025

@author: enora
"""

import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# --- PARAMÈTRES PHYSIQUES ---
mu = 0.53
A = 0.01
g = 10
z0 = 0
v0 = 0
dt = 0.001
t_max = 40
tau_min = 1e-5  # Pour éliminer les parasites numériques à τ = 0

# --- PLAGE DE PULSATION ---
omega_list = np.linspace(10, 80, 1000)

# --- STOCKAGE ---
omega_values = []
tau_values = []

for omega in omega_list:
    t = 0
    z = z0
    v = v0
    bounces = []
    last_bounce_time = None

    while t < t_max:
        zp = A * np.sin(omega * t)
        vp = A * omega * np.cos(omega * t)

        # Mise à jour du mouvement libre
        v -= g * dt
        z += v * dt

        # Collision avec le plateau
        if z <= zp:
            if last_bounce_time is not None:
                tau = t - last_bounce_time
                if tau > tau_min:
                    bounces.append(tau)
                    last_bounce_time = t
            else:
                last_bounce_time = t  # Premier rebond

            v = vp - mu * (v - vp)
            z = zp

        t += dt

    # On affiche uniquement les 50 derniers τ (comme dans le logistic map)
    if len(bounces) > 50:
        omega_values.extend([omega] * 50)
        tau_values.extend(bounces[-50:])

# --- AFFICHAGE ---
plt.figure(figsize=(20, 10))
plt.plot(omega_values, tau_values, ',k', markersize=0.5, alpha=0.5)
plt.title("Diagramme de bifurcation – sans seuil de décollage", fontsize=24)
plt.xlabel("Pulsation $\\omega$ (rad/s)", fontsize=20)
plt.ylabel("Temps entre deux rebonds $\\tau_n$ (s)", fontsize=20)
plt.grid(True, linestyle=':', alpha=0.4)
plt.tight_layout()
plt.show()
