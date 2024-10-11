import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# Botón para construir el histograma
hist_button = st.button('Construir histograma')

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig_hist = px.histogram(car_data, x="odometer")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para construir el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Gráfico de dispersión: Odometer vs Price")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)
