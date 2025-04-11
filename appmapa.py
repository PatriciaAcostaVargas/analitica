import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el archivo CSV
@st.cache
def load_data():
    df = pd.read_csv('/path/to/tu/archivo.csv')  # Reemplaza con la ruta correcta de tu archivo
    return df

# Cargar y mostrar los datos
df = load_data()

st.title('Visualización de Datos con Gráfico de Calor')

st.write('Datos cargados desde el archivo CSV:')
st.write(df.head())  # Muestra las primeras filas de los datos

# Crear un gráfico de calor
st.subheader('Gráfico de Calor')
corr_matrix = df.corr()  # Calcula la matriz de correlación
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
st.pyplot()  # Muestra el gráfico en Streamlit
