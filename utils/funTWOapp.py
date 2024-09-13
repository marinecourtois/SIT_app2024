
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import streamlit as st
import matplotlib.image as image
from numpy.linalg import eig

# nickname for Polynomial function
P = np.polynomial.Polynomial

#######################################
# parameters
r = 2.0
p = .4
K = 10.
μ = .5

params_sim = np.array([r, p, K, μ])


#########################################################
# partie intégration du modèle / dynamiques

# définition d'un vecteur tspan 
t_0 = 0             # temps initial
t_fin = 30.0        # temps final
pas_t = 0.01        # pas de temps de récupération des variables entre t_0 et t_fin
tspan = np.arange(t_0, t_fin, pas_t)

# modele TIS
def model_SIT(etat, t, params):
    f, m = etat
    r, p, K, μ= params
    etatdot = [r*(1-p)*f*(1-f/K) - μ*f,
               r*p*f*(1-f/K) - μ*m]
    
    return etatdot    

# definition du modèle TIS en temps inverse pour separatrice
def model_SITinv(etat, t, params):
    f, m = etat
    r, p, K, μ = params
    etatdot = [-r*(1-p)*f*(1-f/K) + μ*f,
               -r*p*f*(1-f/K) + μ*m]
    
    return etatdot   

# fonction pour intégration et plot des dynamiques
#@st.experimental_singleton
def plotSim(etat0, params_sim, tspan = tspan):
    params = params_sim
    
    int_SIT = odeint(model_SIT, etat0, tspan, args=(params,), hmax=pas_t)
    
    # figure
    fig1, ax1 = plt.subplots(figsize=(8, 6))  

    # tracé des simulations par rapport au temps
    ax1.plot(tspan, int_SIT[:,0], color='orange', label='femelles', linewidth = 2)
    ax1.plot(tspan, int_SIT[:,1], color='blue', label='mâles', alpha = .4, linewidth = 2)
    
    ax1.legend(fontsize='10', loc = 'upper right')
    ax1.set_xlabel('temps', fontsize='12')
    ax1.set_ylabel('densités', fontsize='12')
    fig1.suptitle(r'Dynamiques de populations TIS', va='top', fontsize='18')
    ax1.set_ylim(bottom = -.25, top=K)
    ax1.grid()

    # returns the figure object
    return fig1
