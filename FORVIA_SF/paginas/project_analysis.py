import streamlit as st 
import pandas as pd
from utils.dataloader import load_project_data
from utils.analysis_function import filter_projects


st.title("Analisis de proyectos")
df = load_project_data()
with st.sidebar:
    st.markdown("### Filtros proyectos")

    estados= df['State'].unique().tolist()
    estado_filtro = st.multiselect("Region", estados, default=estados)

    areas = df['Geographical scope'].dropna().unique().tolist()
    area_filtro = st.selectbox("Area geografico", ["Todos"] + areas)

    avance_min = st.slider("Avance mínimo (%)", 0, 100, 0)

df_filtrado, avg_progress = filter_projects(df, estado_filtro, area_filtro, avance_min)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Proyectos filtraods", len(df_filtrado))
with col2:
    st.metric("Avance promedio", f"{avg_progress:1f}%")
with col3:
    st.metric("Project managers", df_filtrado['Project manager'].nunique())
with col4:
    st.metric("Ubicaciones", df_filtrado['Geographical scope'].nunique())