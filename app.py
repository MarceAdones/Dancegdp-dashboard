import streamlit as st
import pandas as pd
import os

# Configuración de la página
st.set_page_config(
    page_title="DanceManager",
    page_icon="💃",
    layout="wide"
)

CARPETA = "cursos"

# Crear carpeta si no existe
if not os.path.exists(CARPETA):
    os.makedirs(CARPETA)

# Cursos iniciales
cursos_base = [
    "Ballet",
    "Salsa",
    "Bachata",
    "Danza Urbana",
    "Kpop",
    "Contemporaneo"
]

st
