Este proyecto implementa una aplicación web interactiva utilizando Streamlit, Pandas y Plotly Express para realizar un análisis exploratorio de un conjunto de datos de anuncios de venta de vehículos (vehicles_us.csv).

La aplicación permite al usuario visualizar, filtrar y analizar información relevante como el precio, el kilometraje, el año del modelo, el tipo de vehículo y su condición, mediante gráficos dinámicos e interactivos.

-Funcionamiento del programa

Carga de datos

El programa carga un archivo CSV que contiene información sobre vehículos en venta, incluyendo variables como:

price (precio)
model_year (año del modelo)
model (marca/modelo)
condition (condición del vehículo)
odometer (kilometraje)
type (tipo de vehículo)

Visualización del conjunto de datos

La aplicación muestra una vista previa del DataFrame completo, permitiendo al usuario inspeccionar los registros originales directamente desde la interfaz web.

Filtros interactivos

En la barra lateral se incluyen controles interactivos que permiten al usuario reducir el conjunto de datos según criterios específicos:

Control deslizante (slider) para seleccionar un rango de años (model_year).
Lista desplegable (selectbox) para seleccionar un tipo de vehículo (type).

Estos filtros se aplican dinámicamente al DataFrame, generando un subconjunto de datos (filtered_data) que se utiliza en las visualizaciones.

Selección de visualizaciones mediante checkbox

El usuario puede elegir qué gráficos desea mostrar mediante casillas de verificación (checkbox):

Histograma del kilometraje (odometer).
Diagrama de dispersión entre precio y kilometraje (price vs odometer).
Boxplot del precio según el tipo de vehículo (price por type).
Boxplot del precio según la condición del vehículo (price por condition).

Cada gráfico se genera únicamente cuando su checkbox correspondiente está activado, evitando sobrecargar la interfaz.

Gráficos interactivos

Las visualizaciones se generan con la biblioteca Plotly Express, lo que permite:

Explorar valores al pasar el cursor sobre los puntos (hover).
Hacer zoom sobre regiones específicas.
Identificar valores atípicos (outliers).
Comparar distribuciones entre categorías.

Visualizaciones incluidas

Histograma del odómetro
Permite observar la distribución del kilometraje de los vehículos.

Diagrama de dispersión (precio vs odómetro)
Permite analizar la relación entre el precio del vehículo y su uso (kilometraje), diferenciando por condición.

Boxplot del precio por tipo de vehículo
Permite comparar la distribución de precios entre diferentes tipos (SUV, sedan, pickup, etc.).

Boxplot del precio por condición del vehículo
Permite evaluar cómo influye el estado del vehículo (excellent, good, fair, like new) en el precio.