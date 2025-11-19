import streamlit as st
from utils.data_loader import load_project_data
from utils.analysis_functions import assign_coords_to_projects
from streamlit_folium import st_folium
import folium
import pydeck as pdk


df = load_project_data()

df_coords = assign_coords_to_projects(df, 'Geographical scope')
st.map(df_coords[['lat', 'lon']], color='#38303086', zoom= 1, size=300000)

map_center = [df_coords['lat'].mean(), df_coords['lon'].mean()]
m= folium.Map(location=map_center, zoom_start= 2) 

for _, row in df_coords.iterrows():
    folium.Marker(
        [row['lat'], row['lon']],
        popup = f"{row['Project Name']}     {row['Geographical scope']}"
    ).add_to(m)

st_folium(m, width = 800, height= 500)

#pip install streamlit folium streamlit-folium 
st.markdown("<hr style='border: 2px solid #C81A2D; background-color: #F5F5F5;height: 5px; width: 100%;'></hr>", unsafe_allow_html=True)

st.pydeck_chart(
    pdk.Deck(
        map_style= 'mapbox://styles/mapbox/dark-v10', 
        initial_view_state=pdk.ViewState(
            latitude=df_coords['lat'].mean(),
            longitude=df_coords['lon'].mean(),
            zoom=1,
            pitch=30
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=df_coords,
                get_position = "[lon, lat]", 
                radius = 300000,
                pickable= True,
                extruded = True

            )
        ]
    )
)