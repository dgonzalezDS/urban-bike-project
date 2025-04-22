import pandas as pd

# Cargar los datos procesados
data = pd.read_csv('data/processed/citybikes_processed.csv')

# Análisis básico
print(data.describe())  # Estadísticas descriptivas
print(data.info())  # Información sobre el dataframe
print(data.head())  # Primeras filas del dataframe