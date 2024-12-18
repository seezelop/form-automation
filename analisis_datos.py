import pandas as pd
import matplotlib.pyplot as plt

# Archivos generados en el paso 1
archivos = ["Empleados.xlsx", "Inventario.xlsx", "Ventas.xlsx"]

# Lista para guardar DataFrames
dataframes = []

# Leer cada archivo y cargarlo en un DataFrame
for archivo in archivos:
    df = pd.read_excel(archivo)
    dataframes.append(df)

# Concatenar los tres archivos en un solo DataFrame
datos_combinados = pd.concat(dataframes, ignore_index=True)

# Análisis de métricas clave
print("Análisis de KPIs:")
print("Promedio de valores numéricos:")
print(datos_combinados.mean(numeric_only=True))

print("\nMáximos por columna:")
print(datos_combinados.max(numeric_only=True))

print("\nTotales por columna:")
print(datos_combinados.sum(numeric_only=True))

# Visualización: gráfico de barras para totales
totales = datos_combinados.sum(numeric_only=True)
totales.plot(kind='bar', title='Totales por Métrica', ylabel='Total', xlabel='Métricas')
plt.show()

# Guardar resultados en un nuevo archivo Excel
resultado = pd.DataFrame({
    "Promedio": datos_combinados.mean(numeric_only=True),
    "Máximo": datos_combinados.max(numeric_only=True),
    "Total": datos_combinados.sum(numeric_only=True)
})
resultado.to_excel("resultado_analisis.xlsx", index_label="Métrica")

print("¡Análisis completo! Resultados guardados en 'resultado_analisis.xlsx'.")
