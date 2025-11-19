import streamlit as st

st.set_page_config(
    page_title='Dashboard multi-pagina',
    layout='wide',
    initial_sidebar_state='expanded'
)

#definir las paginas
home_page = st.Page(
    'Paginas/home.py',
    title='home',
    icon=':material/home:' #materialsymbols google para saber los nombres
)

#definir las paginas
projects_page = st.Page(
    'Paginas/project_analysis.py',
    title='analisis de proyectos',
    icon=':material/analytics:'
)

#definir las paginas
percentage_page = st.Page(
    'Paginas/percentage_analysis.py',
    title='analisis de porcentaje',
    icon=':material/table_chart_view:'
)

mapa_page = st.Page(
    'Paginas/mapa.py',
    title='Mapas',
    icon=':material/map_search:'
)


#Crear navegacion
# pg = st.navigation([home_page,projects_page,percentage_page])

pg = st.navigation({
    'Inicio':[home_page],
    'Analisis':[projects_page,percentage_page],
    'Visualizacion':[mapa_page]
})



#ejecutar pagina seleccionada
pg.run()