import streamlit as st
from PIL import Image
import src.manage_data as dat
import plotly.express as px
import pandas as pd
import folium

import codecs
import streamlit.components.v1 as components

st.write("""
# NY AIRBNB 
""")

imagen = Image.open("Output/mapa.jpg")

st.image(imagen)

datos = dat.carga_data()

#st.dataframe visualiza un dataframe
st.dataframe(datos)

datos_grafico = dat.grafico_barras_st()
st.dataframe(datos_grafico)

st.bar_chart(datos_grafico)
lista = dat.lista_bh()

neighbourhood_g = st.selectbox("Select a neighbourhood group", lista)
st.write("You have chosen", neighbourhood_g)

datagraf = dat.grafico(neighbourhood_g)

fig = px.line(datagraf, y="price", title=f"Price evolution in {neighbourhood_g}")

fig.show()
