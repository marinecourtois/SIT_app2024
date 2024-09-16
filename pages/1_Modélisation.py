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
    st.markdown("#### Modèle à deux sexes")
    st.markdown(r"Afin de complexifier le modèle, on peut distinguer mâles et femelles au sein de la population. On notera ainsi $N(t) = F(t) + M(t)$, où $F$ désigne le nombre de femelles et $M$ le nombre de mâles. En s'inspirant du modèle précédent, on obtient les équations suivantes :")
    st.markdown(r"$$\left\{\begin{array}{l}\displaystyle \frac{d F}{dt} = r\, (1-p\,) c(F) F - \mu F,\\[.5cm]\displaystyle \frac{d M}{dt} = r\, p\, c(F) F - \mu M.\end{array}\right.$$")
    st.markdown(r"où $p$ représente le sexe-ratio, autrement dit la proportion de mâles dans la population. Nous nous basons ici sur l'exemple d'une population de mouches à fruits en compétition pour les sites de pontes. Le nombre de mâles étant généralement suffisant pour assurer la reproduction, on considère que leur croissance n'est limitée que par le nombre de femelles.")

with col13:
    st.markdown("#### Modèle Technique de l'Insecte Stérile")
    st.markdown(r"En ajoutant l'influence des mâles stériles (notés $M_S$) introduits dans le modèle précédent, on obtient le modèle suivant")
    st.markdown(r"$$\left\{\begin{array}{l}\displaystyle \frac{d F}{dt} = r\, (1-p\,) \frac{M}{M+M_S} c(F) F - \mu F,\\[.5cm]\displaystyle \frac{d M}{dt} = r\, p\,  \frac{M}{M+M_S}  c(F) F - \mu M.\end{array}\right.$$")
    st.markdown(r"où $F$ et $M$ représentent les densités des individus femelles et mâles (sauvages); $M_S$ représente la densité de mâles stériles, supposée constante par simplicité. $r$ est le nombre moyen de descendants par femelle accouplée, $p$ la proportion de mâles dans la descendance et $\mu$ le taux de mortalité de l'espèce. $c(F)$ est une fonction qui vaut 1 lorsque $F=0$ et est décroissante de $F$; elle représente la compétition entre les femelles pour accéder aux sites de pontes.")
    
