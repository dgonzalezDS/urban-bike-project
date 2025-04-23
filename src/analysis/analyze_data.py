import pandas as pd

# Cargar los datos procesados
data = pd.read_csv('data/processed/citybikes_processed.csv')

# Análisis básico
print("Estadísticas descriptivas para las columnas numéricas:")
print(data.describe())  # Estadísticas descriptivas para columnas numéricas

print("\nInformación sobre el DataFrame:")
print(data.info())  # Información sobre el DataFrame (tipos de datos, nulos, etc.)

print("\nPrimeras filas del DataFrame:")
print(data.head())  # Primeras filas para ver una muestra del dataset

# Análisis más detallado
print("\nTipos de datos de cada columna:")
print(data.dtypes)  # Mostrar tipos de datos de cada columna

print("\nNúmero de valores nulos por columna:")
print(data.isna().sum())  # Número de valores nulos por columna

print("\nPorcentaje de valores nulos por columna:")
print(data.isna().mean() * 100)  # Porcentaje de valores nulos por columna

print("\nNúmero de valores únicos por columna:")
print(data.nunique())  # Número de valores únicos por columna

print("\nDistribución de los valores de las columnas categóricas:")
categorical_columns = data.select_dtypes(include=['object']).columns  # Identificar columnas categóricas
for col in categorical_columns:
    print(f"\nDistribución de valores en la columna {col}:")
    print(data[col].value_counts())  # Ver distribución de valores en las columnas categóricas

# Análisis adicional de columnas con demasiados valores nulos
threshold = 0.5  # Umbral del 50% para valores nulos
print("\nColumnas con más del 50% de valores nulos:")
print(data.columns[data.isna().mean() > threshold])  # Mostrar columnas con más del 50% de nulos

# Ver columnas que podrían no ser útiles (como las que tienen demasiados valores nulos o son constantes)
print("\nColumnas que tienen sólo un valor único:")
print(data.columns[data.nunique() == 1])  # Mostrar columnas con un único valor (pueden no ser útiles para el análisis)
