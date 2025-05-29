import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Dashboard Turístico Finca Luna Nueva Lodge Miami", layout="wide")
st.title("Dashboard Turístico: Expansión Finca Luna Nueva Lodge Miami")
st.markdown("Visualización de datos clave para el análisis del mercado turístico y hospedaje en Miami.")

# Ruta al archivo Excel (se asume que el archivo está en data/datos_turisticos.xlsx)
excel_path = "data/datos_turisticos.xlsx"

# Cargar todas las hojas del Excel
@st.cache_data
def load_all_sheets(path):
    return pd.read_excel(path, sheet_name=None)

sheets = load_all_sheets(excel_path)

# Mostrar selector de hoja
sheet_names = list(sheets.keys())
selected_sheet = st.selectbox("Selecciona la hoja del Excel:", sheet_names)

# Mostrar la hoja seleccionada
st.header(selected_sheet)
df = sheets[selected_sheet]
st.dataframe(df, use_container_width=True)

# Mostrar todas las hojas (opcional, puedes comentar o eliminar si solo quieres una)
st.header("Todas las hojas del Excel")
for sheet in sheet_names:
    st.subheader(sheet)
    st.dataframe(sheets[sheet], use_container_width=True)
