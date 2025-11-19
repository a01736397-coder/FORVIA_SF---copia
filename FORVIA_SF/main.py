import streamlit as st 

st.set_page_config(
    page_title="Dashboard multi-pagina",
    layout="wide",
    initial_sidebar_state="expanded" #se puede usar "collapsed"
)

#Definir las páginas 
home_page = st.Page(
    "paginas/home.py",
    title="Home",
    icon=":material/home:"
)

projects_page = st.Page(
    "paginas/project_analysis.py",
    title="Analisis de proyectos",
    icon=":material/analytics:"
)

percentage_page = st.Page(
    "paginas/percentage_analysis.py",
    title="Analisis de porcentajes",
    icon=":material/table_chart_view:"

)

mapa_page = st.Page(
    "paginas/mapa.py",
    title="Analisis del mapa",
    icon=":material/map_search:"
)

#Crear navegación

pg= st.navigation([home_page, projects_page, percentage_page])

pg= st.navigation({
    "Inicio": [home_page],
    "Analisis": [projects_page, percentage_page],
    "Visualización": [mapa_page]
})

#Ejecutar ala pagina seleccionada 
pg.run()