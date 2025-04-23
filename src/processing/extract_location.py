import pandas as pd
import ast
import os

# Ruta al dataset procesado
input_path = 'data/processed/citybikes_processed.csv'
output_path = 'data/processed/citybikes_location.csv'

# Cargar los datos
df = pd.read_csv(input_path)

# Convertir la columna location de string a diccionario
def parse_location(location_str):
    try:
        return ast.literal_eval(location_str)
    except (ValueError, SyntaxError):
        return {}

df['location_dict'] = df['location'].apply(parse_location)

# Extraer latitud, longitud y país si existen
df['latitude'] = df['location_dict'].apply(lambda loc: loc.get('latitude'))
df['longitude'] = df['location_dict'].apply(lambda loc: loc.get('longitude'))
df['country'] = df['location_dict'].apply(lambda loc: loc.get('country', 'Desconocido'))

# Eliminar columna auxiliar
df = df.drop(columns=['location_dict'])

# Guardar el nuevo archivo
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)

print(f"Archivo guardado con latitud, longitud y país en: {output_path}")
