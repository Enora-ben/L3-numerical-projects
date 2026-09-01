# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 20:21:16 2025

@author: enora
"""

import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

#PARAMÈTRES
mu = 0.53          # Coefficient d'amortissement (0 < mu < 1)
A = 0.01           # Amplitude du plateau (m)
g = 10             # Gravité terrestre (m/s²)
z0 = 0             # Position initiale de la bille (m)
v0 = 0             # Vitesse initiale (m/s)
dt = 0.001         # Pas de temps (s)
t_max = 40         # Durée de la simulation (s)
tau_min = 1e-3     # Seuil strict pour exclure tau trop petits

# --- VALEURS DE PULSATION ω À EXPLORER ---
omega_list = np.linspace(13, 160, 1000)  # ω en rad/s

# --- STOCKAGE DES RÉSULTATS ---
omega_values = []  # Liste des ω associés à chaque τ
tau_values = []    # Liste des τ 


# Etablissement de la boucle et conditionnement 

for omega in omega_list:
    # Seuil analytique de décollage
    omega_crit = np.sqrt(g / A)
    if omega <= omega_crit:
        continue  # Le plateau ne peut pas soulever la bille

    # Calcul de Tc
    try:
        Tc = (1 / omega) * np.arcsin(-g / (A * omega**2))
    except ValueError:
        continue  

    # Initialisation du système
    t = 0
    z = z0
    v = v0
    last_bounce_time = None
    bounces = []

    while t < t_max:
        zp = A * np.sin(omega * t)
        vp = A * omega * np.cos(omega * t)

        v -= g * dt
        z += v * dt

        if z <= zp:
            if last_bounce_time is not None:
                tau = t - last_bounce_time
                if tau >= Tc and tau > tau_min:
                    bounces.append(tau)
                    last_bounce_time = t
            else:
                last_bounce_time = t  # premier rebond

            v = vp - mu * (v - vp)
            z = zp

        t += dt

    # On stocke tous les τ 
    if len(bounces) > 0:
        omega_values.extend([omega] * len(bounces))
        tau_values.extend(bounces)

        
#Arrangement=np.array([np.histogram(tau_values)]) 


plt.figure(figsize=(20, 10))
plt.imshow(Arrangement.T[::-1,:],aspect='auto',extent=[13,160,0.09])
#plt.plot(omega_values, tau_values, ',k', markersize=0.5, alpha=0.7)  
plt.title("Diagramme de bifurcation – Temps entre les rebonds $\\tau_n$ en fonction de $\\omega$", fontsize=24)
plt.xlabel("Pulsation $\\omega$ (rad/s)", fontsize=20)
plt.ylabel("Temps entre deux rebonds $\\tau_n$ (s)", fontsize=20)
plt.axvline(np.sqrt(g/A), color='red', linestyle='--', linewidth=1, label="Seuil de décollage $\\omega_c$")
plt.legend(fontsize=16)
plt.grid(True, linestyle=':', alpha=0.4)
plt.tight_layout()
plt.show()
