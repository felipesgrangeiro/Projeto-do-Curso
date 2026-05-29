import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("vehicles_us.csv")

st.header("Dashboard de veículos usados")

build_histogram = st.checkbox("Criar histograma")

if build_histogram:
    st.write("Criando um histograma para a coluna odometer")

    fig = px.histogram(
        car_data,
        x="odometer"
    )

    st.plotly_chart(fig, use_container_width=True)


build_scatter = st.checkbox("Criar gráfico de dispersão")

if build_scatter:
    st.write("Criando um gráfico de dispersão entre odometer e price")

    fig = px.scatter(
        car_data,
        x="odometer",
        y="price"
    )

    st.plotly_chart(fig, use_container_width=True)