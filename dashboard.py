import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Turístico Finca Luna Nueva Lodge Miami", layout="wide")
st.title("Dashboard Turístico: Expansión Finca Luna Nueva Lodge Miami")
st.markdown("Visualización de datos clave para el análisis del mercado turístico y hospedaje en Miami.")

archivos = {
    "Demografía y Mercado": "Datos-Demograficos-y-de-Mercado-de-Miami.csv",
    "Turismo y Hospedaje": "Turismo-y-Hospedaje-en-Miami.csv",
    "Alquileres Vacacionales": "Alquileres-Vacacionales-y-Plataformas.csv",
    "Segmentos de Mercado": "Segmentos-de-Mercado-y-Caracteristicas.csv",
    "Eventos Turísticos": "Eventos-Turisticos-Relevantes-en-Miami.csv",
    "Campañas Redes Sociales": "Campanas-de-Redes-Sociales-Simulador.csv",
    "Evaluación Anuncios": "Evaluacion-de-Anuncios-Promocionales.csv",
    "Permisos y Licencias": "Permisos-y-Licencias-Requeridas.csv"
}

# Seleccionar archivo para mostrar
selected = st.selectbox("Selecciona la tabla que deseas ver:", list(archivos.keys()))

try:
    df = pd.read_csv(archivos[selected])
    st.header(selected)
    st.dataframe(df, use_container_width=True)
except Exception as e:
    st.error(f"No se pudo cargar el archivo {archivos[selected]}: {e}")

# Mostrar todas las tablas
st.header("Todas las tablas disponibles")
for titulo, archivo in archivos.items():
    st.subheader(titulo)
    try:
        df = pd.read_csv(archivo)
        st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error(f"No se pudo cargar el archivo {archivo}: {e}")
