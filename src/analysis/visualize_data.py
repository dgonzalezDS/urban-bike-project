import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos procesados
data = pd.read_csv('data/processed/citybikes_processed.csv')

# Crear un gráfico de barras para una columna específica
plt.figure(figsize=(10, 6))
sns.countplot(x='company', data=data)
plt.title('Distribución de company')
plt.savefig('src/visualization/company_distribution.png')
plt.show()
