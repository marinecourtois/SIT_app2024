import numpy as np
import streamlit as st

from utils.funTISapp import *

st.set_page_config(layout="wide", page_title = "Modélisation", page_icon = "🌳")

st.sidebar.header("Modélisation")

col2, col3 = st.columns([5, 15], gap = "large")

with col2:
    st.image("https://forgemia.inra.fr/ludovic.mailleret/figures/-/raw/master/ceratitis_capitata/ceratitis_small.png", width=250)
with col3:
    st.markdown("$~$")
    st.markdown("# Présentation des différents modèles")

col12, col13 = st.columns([11, 10],gap = "large")

with col12:
    st.markdown("#### Modèle de croissance exponentielle")
    st.markdown(r"Description des naissances et morts des différents individus. On étudie le nombre d'individus, notée $N(t)$ d'une population donnée au cours du temps, représenté par la variable $t$. En notant $r$ le taux de natalité et $\mu$ le taux de mortalité, ce modèle s'écrit :")
    st.markdown(r"$$\left\{\begin{array}{l}\displaystyle \frac{dN}{dt} = rN - \mu N.\end{array}\right.$$")
    st.markdown("#### Modèle de croissance limitée par la compétition")
    st.markdown("Afin de pallier les limites du modèle exponentiel, on considère un nouveau modèle prenant en compte la compétition entre les individus et empêchant la population de croître indéfiniment. Ce modèle peut s'écrire :")
    st.markdown(r"$$\left\{\begin{array}{l}\displaystyle \frac{dN}{dt} = rc(N)N -\mu N,\end{array}\right.$$")
    st.markdown(r"où $c(N)$ est une fonction décroissante, qui vaut $1$ lorsque $N=0$, et qui représente la compétition entre les individus (par exemple pour la reproduction). Dans le cas le plus simple, on choitit $c(N) = 1 - \alpha N$. On parle alors de modèle logistique, et $\alpha$ désigne l'intensité de la compétition entre les individus. ")

with col13:
    st.markdown("#")
    st.markdown(r"$$\left\{\begin{array}{l}\displaystyle \dot f = r (1-p) f \frac{m}{m+m_s} c(f) - \mu f,\\[.3cm]\displaystyle \dot m = r p f \frac{m}{m+m_s}  c(f) - \mu m.\end{array}\right.$$")
    st.markdown("##### Reproduction et influence des mâles stériles")
    st.markdown("- les accouplements sont considérés non limitants et au hasard")
    st.markdown(r"- en l'absence de mâles stériles ($m_s = 0$), les femelles sauvages pondent des oeufs à un taux $r$, pondéré par la compétition entre femelles. La vitesse de reproduction est donc : $r f\,c(f)$")
    st.markdown(r"- en présence de mâles stériles ($m_s > 0$), seuls les acouplements avec des mâles sauvages, en proportion $\frac{m}{m+m_s}$, produisent des descendants. La vitesse de reproduction est donc : $r f \frac{m}{m+m_s}\,c(f)$")
