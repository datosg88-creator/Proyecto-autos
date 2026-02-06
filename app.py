import pandas as pd
import plotly.express as px
import streamlit as st

# Leer datos
car_data = pd.read_csv("vehicles_us.csv")

st.title("Dashboard interactivo de vehículos 🚗 🚙 🚓 🚒 🚐 🚚 🏎️")

# Mostrar datos
st.subheader("Vista previa del DataFrame")
st.dataframe(car_data)

# ------------------ FILTROS ------------------

st.sidebar.header("Filtros")

# Slider de años
min_year = int(car_data["model_year"].min())
max_year = int(car_data["model_year"].max())

year_range = st.sidebar.slider(
    "Selecciona rango de año",
    min_year,
    max_year,
    (min_year, max_year)
)

# Selectbox por tipo
type_selected = st.sidebar.selectbox(
    "Selecciona tipo de vehículo",
    ["Todos"] + sorted(car_data["type"].dropna().unique().tolist())
)

# Aplicar filtros
filtered_data = car_data[
    (car_data["model_year"] >= year_range[0]) &
    (car_data["model_year"] <= year_range[1])
]

if type_selected != "Todos":
    filtered_data = filtered_data[filtered_data["type"] == type_selected]

st.write(f"Registros después de filtrar: {filtered_data.shape[0]}")

# ------------------ CHECKBOX ------------------

st.subheader("Visualizaciones")

show_hist = st.checkbox("Mostrar histograma del odómetro")
show_scatter = st.checkbox("Mostrar dispersión Precio vs Odómetro")
show_box_type = st.checkbox("Mostrar boxplot de Precio por Tipo")
show_box_condition = st.checkbox("Mostrar boxplot de Precio por Condición")

# ------------------ GRÁFICAS ------------------

if show_hist:
    st.write("Distribución del kilometraje")
    fig1 = px.histogram(filtered_data, x="odometer", nbins=40)
    st.plotly_chart(fig1, use_container_width=True)

if show_scatter:
    st.write("Relación Precio - Kilometraje")
    fig2 = px.scatter(
        filtered_data,
        x="odometer",
        y="price",
        color="condition",
        hover_data=["model", "model_year", "type"]
    )
    st.plotly_chart(fig2, use_container_width=True)

if show_box_type:
    st.write("Distribución de precios por tipo de vehículo")
    fig3 = px.box(
        filtered_data,
        x="type",
        y="price",
        color="type"
    )
    st.plotly_chart(fig3, use_container_width=True)

if show_box_condition:
    st.write("Distribución de precios por condición del vehículo")
    fig4 = px.box(
        filtered_data,
        x="condition",
        y="price",
        color="condition"
    )
    st.plotly_chart(fig4, use_container_width=True)