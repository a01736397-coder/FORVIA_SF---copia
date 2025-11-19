import streamlit as st
import pandas as pd
from utils.data_loader import load_project_data
from utils.analysis_functions import filter_projects

st.title("Analisis de proyectos")

# df=pd.read_csv('data/proyectos.csv', encoding='latin1')
# df= df.iloc[:-2].copy()

# df['Percent complete'] = pd.to_numeric(df['Percent complete'], errors='coerce')

df = load_project_data()

with st.sidebar:
    st.markdown("### Filtros proyectos")

    estados= df['State'].dropna().unique().tolist()
    estado_filtro = st.multiselect("Region", estados, default=estados)

    areas = df['Geographical scope'].dropna().unique().tolist()
    area_filtro = st.selectbox("Area geografico", ["Todas"] + areas)

    avance_min = st.slider("Avance mínimo (%)", 0, 100, 0)


df_filtrado, avg_progress = filter_projects(df, estado_filtro, area_filtro, avance_min)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric('Proyectos filtrados', len(df_filtrado))

with col2:
    st.metric('Avance promedio', f'{avg_progress:.1f}%')
    
with col3:
    st.metric('Project managers', df_filtrado['Project manager'].nunique())

with col4:
    st.metric('Ubicaciones', df_filtrado['Geographical scope'].nunique())