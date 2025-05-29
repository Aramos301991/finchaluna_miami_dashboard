import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Lista de archivos CSV y sus títulos
archivos = {
    "Demografía y Mercado": "Datos-Demograficos-y-de-Mercado-de-Miami.csv",
    "Turismo y Hospedaje": "Turismo-y-Hospedaje-en-Miami.csv",
    "Alquileres Vacacionales": "Alquileres-Vacacionales-y-Plataformas.csv",
    "Segmentos de Mercado": "Segmentos-de-Mercado-y-Caracteristicas.csv",
    "Eventos Turísticos": "Eventos-Turisticos-Relevantes-en-Miami.csv",
    "Campañas Redes Sociales": "Campañas-de-Redes-Sociales-Simulador.csv",
    "Evaluación Anuncios": "Evaluacion-de-Anuncios-Promocionales.csv",
    "Permisos y Licencias": "Permisos-y-Licencias-Requeridas.csv"
}

# Cargar todos los dataframes
dataframes = {}
for titulo, archivo in archivos.items():
    try:
        dataframes[titulo] = pd.read_csv(archivo)
    except Exception as e:
        st.error(f"No se pudo cargar el archivo {archivo}: {e}")

# Título del Dashboard
st.title("Dashboard Turístico: Expansión Finca Luna Nueva Lodge Miami")

# Selector de tabla
opcion = st.selectbox("Selecciona la tabla que deseas ver", list(archivos.keys()))

# Mostrar la tabla seleccionada
st.subheader(opcion)
df = dataframes[opcion]
st.dataframe(df, use_container_width=True)

# Gráficos de ejemplo para algunas tablas
if opcion == "Turismo y Hospedaje":
    st.subheader("Indicadores Clave de Turismo y Hospedaje")
    # Preparamos los datos para el gráfico
    # Ejemplo: Mostrar solo los indicadores numéricos (puedes adaptar según tu interés)
    try:
        df_numericos = df[df["Valor/Dato"].apply(lambda x: isinstance(x, (int, float)) or (isinstance(x, str) and x.replace('.', '', 1).isdigit()))].copy()
        df_n
