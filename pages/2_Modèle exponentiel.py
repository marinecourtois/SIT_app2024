import numpy as np
import streamlit as st

from utils.funEXPapp import *

st.set_page_config(layout="wide", page_title = "Simulations", page_icon = "📈")

st.sidebar.header("Simulations")


col2, col3 = st.columns([5, 15], gap = "large")

with col2:
    st.image("https://forgemia.inra.fr/ludovic.mailleret/figures/-/raw/master/ceratitis_capitata/ceratitis_small.png", width=250)
with col3:
    st.markdown("$~$")
    st.markdown("# Modèle de croissance exponentielle")


col121, col131 = st.columns([11, 10], gap = "large")

with col121:
    st.markdown("### Calculs et simulations")
    st.markdown("Saisissez les paramètres")

col22, col23, col24 = st.columns([7, 7, 7], gap = "large")
with col22:
    N0 = st.slider(' Densité initiale', min_value = 0, max_value = 100, value = 10, step=1, disabled = False)  

with col23:
    r = st.slider(' Taux de natalité', min_value = 0, max_value = 1, value = 0.5, step=0.05) 

with col24:
    μ =  st.slider(' Taux de mortalité', min_value = 0, max_value = 1, value = 0.5, step = 0.05)

### plots

col32, col33 = st.columns([10, 15],gap = "large")
with col32:
    plotChoice = st.selectbox("Que voulez vous tracer ?",
                ("Dynamiques"), index=0)

with col33:
    if plotChoice == "Dynamiques":
        fig_sim = plotSim(N0 = np.array([N0]), r = r, μ = μ)
        st.pyplot(fig_sim)

