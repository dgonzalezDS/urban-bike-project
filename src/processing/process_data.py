import json
import pandas as pd
import os

# Ruta del archivo JSON
raw_data_path = 'data/raw/citybikes_data.json'

# Cargar los datos del archivo JSON
def load_data():
    try:
        with open(raw_data_path, 'r') as f:
            data = json.load(f)
        print("Datos cargados correctamente.")
        return data
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None

# Procesar los datos (convertir a DataFrame de pandas)
def process_data(data):
    # Verificar si los datos existen
    if data is None:
        return None
    
    # Extraer información relevante
    networks = data.get('networks', [])

    # Crear un DataFrame de pandas con las redes de bicicletas
    df = pd.DataFrame(networks)
    return df

# Guardar los datos procesados en un archivo CSV
def save_processed_data(df):
    if df is not None:
        # Asegurarse de que la carpeta 'data/processed' existe
        if not os.path.exists('data/processed'):
            os.makedirs('data/processed')

        # Guardar el DataFrame como CSV
        df.to_csv('data/processed/citybikes_processed.csv', index=False)
        print("Datos procesados y guardados como CSV.")
    else:
        print("No hay datos para guardar.")

# Función principal
def main():
    data = load_data()
    if data:
        df = process_data(data)
        save_processed_data(df)

if __name__ == "__main__":
    main()
