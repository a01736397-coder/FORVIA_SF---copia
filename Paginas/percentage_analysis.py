import streamlit as st
import pandas as pd
from utils.data_loader import load_percentage_data
from utils.analysis_functions import filter_percentage

st.title('analisis de porcentaje')

# df = pd.read_csv("data/percentage_not_completed.csv")
df = load_percentage_data()

with st.sidebar:
    st.markdown("### Filtros")
    
    regiones = df['Region'].unique().tolist()
    region_filtro = st.multiselect('Region', regiones, default=regiones)
    
    grupos = df['Group'].unique().tolist()
    grupo_filtro = st.selectbox('Grupo',['Todos'] + grupos)
    
    st.markdown('---')
    st.info(f'Registros: {len(df)}')

df_filtrado = filter_percentage(df, region_filtro, grupo_filtro)

colu1, colu2 = st.columns([0.4,0.6])

with colu1:
    
    st.header('Resultados de los filtros seleccionados')

with colu2:
    
    colu1, colu2, colu3 = st.columns(3)

with colu1:
    st.metric('Registros filtrados', len(df_filtrado), border=True)

with colu2:
    st.metric('Promedio valor', f'{df_filtrado['valor'].mean():.2%}',border=True, delta= '1.2 % desde la ultima semana')

with colu3:
    st.metric('Semanas (CW)', df_filtrado['CW'].nunique(), border=True)