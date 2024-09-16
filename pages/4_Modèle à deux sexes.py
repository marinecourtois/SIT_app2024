import numpy as np
import streamlit as st

from utils.funTWOapp import *

st.set_page_config(layout="wide", page_title = "Simulations", page_icon = "📈")

st.sidebar.header("Simulations")

col2, col3 = st.columns([5, 15], gap = "large")

with col2:
    st.image("https://forgemia.inra.fr/ludovic.mailleret/figures/-/raw/master/ceratitis_capitata/ceratitis_small.png", width=250)
with col3:
    st.markdown("$~$")
    st.markdown("# Modèle à deux sexes")


col121, col131 = st.columns([11, 10],gap = "large")

with col121:
    st.markdown("### Calculs et simulations")
    st.markdown("Saisissez les paramètres")

col22, col23 = st.columns([10, 10], gap = "large")
with col22:
    f0 = st.slider(r' Densité de femelles sauvages initiale ($F_0$)', min_value = 0.1, max_value = K, value = 3., step=0.1, disabled = False)  

with col23:
    m0 = st.slider(r' Densité de mâles sauvages initiale ($M_0$)', min_value = 0.1, max_value = K, value = K/2, step=0.1) 

# intial condition
etat0 = np.array([f0, m0])

### plots

col32, col33 = st.columns([10, 15],gap = "large")
with col32:
    plotChoice = st.selectbox("Que voulez vous tracer ?",
                ("Dynamiques"), index=0)

with col33:
    if plotChoice == "Dynamiques":
        fig_sim = plotSim(etat0 = etat0, params_sim = params_sim)
        st.pyplot(fig_sim)





