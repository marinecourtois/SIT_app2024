import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import streamlit as st
import matplotlib.image as image
from numpy.linalg import eig

# nickname for Polynomial function
P = np.polynomial.Polynomial

#########################################################
# partie intégration du modèle / dynamiques

# définition d'un vecteur tspan 
t_0 = 0             # temps initial
t_fin = 30.0        # temps final
pas_t = 0.01        # pas de temps de récupération des variables entre t_0 et t_fin
tspan = np.arange(t_0, t_fin, pas_t)

# modele de croissance exponentielle
def model_exp(etat, t, params):
    N = etat
    r, μ = params
    Ndot = [(r-μ)*N[0]]
    return Ndot    

# fonction pour intégration et plot des dynamiques
def plotSim(N0, r, μ, tspan = tspan):
    params = np.array([r, μ])
    
    int_exp = odeint(model_exp, N0, tspan, args=(params,), hmax=pas_t)
    
    # figure
    fig1, ax1 = plt.subplots(figsize=(8, 6))  

    # tracé des simulations par rapport au temps
    ax1.plot(tspan, int_exp[:,0], color='C0', label='Taille de la population (N)', linewidth = 2)
    
    ax1.legend(fontsize='10', loc = 'upper right')
    ax1.set_xlabel('temps', fontsize='12')
    ax1.set_ylabel('densité', fontsize='12')
    fig1.suptitle(r'Dynamiques de populations', va='top', fontsize='18')
    ax1.set_ylim(bottom = -.25, top=K)
    ax1.grid()

    # returns the figure object
    return fig1
