import pandas as pd
import plotly.express as px
import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Dashboard de Vehículos", layout="wide") # Define el título que aparece en la pestaña del navegador y usa el modo wide (ancho) para que los gráficos no queden amontonados en el centro.

# Título principal
st.header('Análisis de Mercado de Vehículos ')

# Carga de datos
car_data = pd.read_csv('vehicles_us.csv')

# --- LIMPIEZA RÁPIDA (Opcional pero recomendada para el slider) ---
# Convertimos el año a entero y eliminamos nulos para el slider
car_data['model_year'] = car_data['model_year'].fillna(car_data['model_year'].median())

# --- BARRA LATERAL (SIDEBAR) PARA FILTROS ---
st.sidebar.header("Filtros de Años")

# Slider para filtrar por año del modelo
min_year = int(car_data['model_year'].min())
max_year = int(car_data['model_year'].max())

year_range = st.sidebar.slider(
    "Selecciona el rango de años",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year) # Valor por defecto (todo el rango)
)

# Filtrado de datos basado en el slider
filtered_data = car_data[(car_data['model_year'] >= year_range[0]) & 
                         (car_data['model_year'] <= year_range[1])]

# --- SECCIÓN DE DATOS ---
st.subheader('Vista previa de los datos')
st.dataframe(filtered_data.head(10))

st.divider() # Línea divisoria visual

# --- SECCIÓN DE GRÁFICOS ---
col1, col2 = st.columns(2) # Dividimos la pantalla en dos columnas

with col1:
    st.write("### Distribución del Odómetro")
    show_hist = st.checkbox('Mostrar Histograma de Kilometraje')
    if show_hist:
        fig = px.histogram(filtered_data, x="odometer", 
                           title="Frecuencia de kilometraje en anuncios",
                           color_discrete_sequence=['indianred'])
        st.plotly_chart(fig, use_container_width=True)

with col2:
    st.write("### Relación Precio vs Odómetro")
    show_scatter = st.checkbox('Mostrar Diagrama de Dispersión')
    if show_scatter:
        fig2 = px.scatter(filtered_data, x="odometer", y="price", 
                          color="condition", # Diferencia por condición visualmente
                          title="Precio vs Kilometraje por condición",
                          hover_data=['model_year', 'model'])
        st.plotly_chart(fig2, use_container_width=True)

# --- NUEVA SECCIÓN: COMPARATIVA DE PRECIOS ---
st.divider()
st.write("### Análisis de Precio por Tipo de Vehículo")

# Un gráfico de caja (Boxplot) es excelente para ver rangos de precios
fig3 = px.box(filtered_data, x="type", y="price", color="fuel",
              title="Distribución de precios por tipo de carrocería y combustible")
st.plotly_chart(fig3, use_container_width=True)
