import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Dashboard Turístico Finca Luna Nueva Lodge Miami", layout="wide")

# Título y descripción
st.title("Dashboard Turístico: Expansión Finca Luna Nueva Lodge Miami")
st.markdown("""
Visualización de datos clave para el análisis del mercado turístico y hospedaje en Miami.
""")

# Cargar datos desde Excel
@st.cache_data
def load_data():
    return pd.ExcelFile(os.path.join("data", "datos_turisticos.xlsx"))

excel = load_data()

# Listar hojas disponibles
sheet_names = excel.sheet_names

# Mostrar cada hoja como una tabla interactiva
for sheet in sheet_names:
    st.header(sheet)
    df = pd.read_excel(excel, sheet_name=sheet)
    st.dataframe(df)
