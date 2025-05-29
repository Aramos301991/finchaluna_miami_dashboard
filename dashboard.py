import streamlit as st
import pandas as pd
import os

# Configuración de la página
st.set_page_config(page_title="Dashboard Turístico Finca Luna Nueva Lodge Miami", layout="wide")
st.title("Dashboard Turístico: Expansión Finca Luna Nueva Lodge Miami")
st.markdown("Visualización de datos clave para el análisis del mercado turístico y hospedaje en Miami.")

# Ruta a la carpeta donde están los archivos CSV
folder_path = "data"

# Listar archivos CSV en la carpeta
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
file_names = [os.path.splitext(f)[0] for f in csv_files]

if not csv_files:
    st.error("No se encontraron archivos CSV en la carpeta 'data'.")
    st.stop()

# Seleccionar archivo para mostrar
selected_file = st.selectbox("Selecciona la tabla que deseas ver:", file_names)

# Mostrar el dataframe seleccionado
selected_csv = csv_files[file_names.index(selected_file)]
df = pd.read_csv(os.path.join(folder_path, selected_csv))
st.header(selected_file)
st.dataframe(df, use_container_width=True)

# Opcional: Mostrar todas las tablas
st.header("Todas las tablas disponibles")
for file_name, csv_file in zip(file_names, csv_files):
    st.subheader(file_name)
    st.dataframe(pd.read_csv(os.path.join(folder_path, csv_file
