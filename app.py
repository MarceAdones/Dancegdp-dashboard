import streamlit as st

st.set_page_config(
    page_title="DanceManager",
    page_icon="💃"
)

st.title("💃 DanceManager")
st.subheader("Sistema de Gestión para Academia de Baile")

st.success("¡La aplicación funciona correctamente!")

curso = st.selectbox(
    "Selecciona un curso",
    [
        "Ballet",
        "Salsa",
        "Bachata",
        "Danza Urbana",
        "Kpop",
        "Contemporáneo"
    ]
)

st.write("Curso seleccionado:", curso)
