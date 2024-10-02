import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Mi Primera App con Streamlit")

# Texto de bienvenida
st.write("Esta es una aplicación de ejemplo para mostrar un gráfico y una tabla.")

# Cargar datos
data = {
    'Año': [2023, 2024, 2025],
    'Ingresos': [10000, 15000, 20000]
}
df = pd.DataFrame(data)

# Mostrar tabla de datos
st.write("Tabla de Ingresos por Año")
st.dataframe(df)

# Crear gráfico de línea
fig, ax = plt.subplots()
ax.plot(df['Año'], df['Ingresos'])
st.pyplot(fig)