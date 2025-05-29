import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Turístico Finca Luna Nueva Lodge Miami", layout="wide")
st.title("Dashboard Turístico: Expansión Finca Luna Nueva Lodge Miami")
st.markdown("Visualización de datos clave para el análisis del mercado turístico y hospedaje en Miami.")

data_files = {
    "Demografía y Mercado": "Demografía y Mercado.csv",
    "Turismo y Hospedaje": "Turismo y Hospedaje.csv",
    "Alquileres Vacacionales": "Alquileres Vacacionales.csv",
    "Segmentos de Mercado": "Segmentos de Mercado.csv",
    "Eventos Turísticos": "Eventos Turísticos.csv",
    "Campañas Redes Sociales": "Campañas Redes Sociales.csv",
    "Evaluación Anuncios": "Evaluación Anuncios.csv",
    "Permisos y Licencias": "Permisos y Licencias.csv"
}

for title, filename in data_files.items():
    try:
        df = pd.read_csv(filename)
        st.header(title)
        st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error(f"No se pudo cargar el archivo {filename}: {e}")
