import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Asegurar que los plots se guarden en el sitio correcto
os.makedirs("reports/figures", exist_ok=True)

# Cargar los datos
data = pd.read_csv('data/processed/citybikes_processed.csv')

# Vista inicial
print("Columnas disponibles:")
print(data.columns)

# Analizar la frecuencia de compañías
# Algunas filas tienen listas o múltiples compañías, convertimos a strings
data['company'] = data['company'].astype(str)

# Contar ocurrencias únicas (esto puede contar strings idénticos, incluso si son listas en string)
company_counts = data['company'].value_counts().head(20)

# Mostrar conteo por consola
print("\nTop 20 compañías más frecuentes:")
print(company_counts)

# Gráfico de barras
plt.figure(figsize=(12, 6))
sns.barplot(x=company_counts.values, y=company_counts.index, palette="viridis")
plt.title("Top 20 compañías de sistemas de bicicletas urbanas")
plt.xlabel("Frecuencia")
plt.ylabel("Compañía")
plt.tight_layout()
plt.savefig("src/visualization/systems_by_company.png")
plt.show()


import ast  # por si location es string que representa un diccionario

# Extraer países desde la columna 'location'
def extract_country(loc):
    try:
        if isinstance(loc, str):
            loc_dict = ast.literal_eval(loc)
        else:
            loc_dict = loc
        return loc_dict.get('country', None)
    except Exception as e:
        print(f"Error procesando: {loc} -> {e}")
        return None

data['country'] = data['location'].apply(extract_country)

# Contar sistemas por país
country_counts = data['country'].value_counts().head(20)

# Mostrar por consola
print("\nTop 20 países por número de sistemas:")
print(country_counts)

# Gráfico de barras
plt.figure(figsize=(12, 6))
sns.barplot(x=country_counts.values, y=country_counts.index, palette="magma")
plt.title("Top 20 países por número de sistemas de bicicletas urbanas")
plt.xlabel("Número de sistemas")
plt.ylabel("País")
plt.tight_layout()
plt.savefig("src/visualization/systems_by_country.png")
plt.show()
