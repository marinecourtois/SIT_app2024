import numpy as np
import streamlit as st

from utils.funTISapp import *

st.set_page_config(layout="wide", page_title = "Simulations", page_icon = "📈")

st.sidebar.header("Simulations")

col2, col3 = st.columns([5, 15], gap = "large")

with col2:
    st.image("https://forgemia.inra.fr/ludovic.mailleret/figures/-/raw/master/ceratitis_capitata/ceratitis_small.png", width=250)
with col3:
    st.markdown("$~$")
    st.markdown("# Technique de l'Insecte Stérile et point de bascule")


col121, col131 = st.columns([11, 10],gap = "large")

with col121:
    st.markdown("### Calculs et simulations")
    st.markdown("Saisissez les paramètres")

col22, col23, col24 = st.columns([7, 7, 7], gap = "large")
with col22:
    f0 = st.slider(r' Densité de femelles sauvages initiale ($F_0$)', min_value = 0.1, max_value = K, value = 3., step=0.1, disabled = False)  

with col23:
    m0 = st.slider(r' Densité de mâles sauvages initiale ($M_0$)', min_value = 0.1, max_value = K, value = K/2, step=0.1) 

with col24:
    mS =  st.slider(r' Densité de mâles stériles ($M_S$)', min_value = 1., max_value = 20., value = 5., step = 0.1)  

# intial condition
etat0 = np.array([f0, m0])

### plots

col32, col33 = st.columns([10, 15],gap = "large")
with col32:
    plotChoice = st.selectbox("Que voulez vous tracer ?",
                ("Dynamiques", "Synthèse des dynamiques", "Plan de phase", "Bifurcations / mâles stériles"), index=0)

with col33:
    if plotChoice == "Dynamiques":
        fig_sim = plotSim(etat0 = etat0, mS = mS, params_sim = params_sim)
        st.pyplot(fig_sim)
    elif plotChoice == "Synthèse des dynamiques":
        fig_all = plotSimAll(mS = mS, params_sim = params_sim)
        st.pyplot(fig_all)
    elif plotChoice == "Plan de phase":
        fig_plane = plotPlane(mS = mS, params_sim = params_sim)
        st.pyplot(fig_plane)
    elif plotChoice == "Bifurcations / mâles stériles":
        fig_bif = plotBif(params_sim = params_sim)
        st.pyplot(fig_bif)
