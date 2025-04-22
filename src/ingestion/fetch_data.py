import requests 
import json
import os

# Definir la URL de la API de CityBikes
API_URL = "https://api.citybik.es/v2/networks"

# Función para obtener los datos de la API
def fetch_bike_data():
    try:
        # Realizar la solicitud a la API
        response = requests.get(API_URL)
        response.raise_for_status()  # Verificar que la solicitud fue exitosa (código 200)

        # Obtener el contenido en formato JSON
        data = response.json()

        # Guardar los datos crudos en un archivo JSON en la carpeta 'data/raw'
        if not os.path.exists('data/raw'):
            os.makedirs('data/raw')
        
        with open('data/raw/citybikes_data.json', 'w') as f:
            json.dump(data, f, indent=4)
        
        print("Datos obtenidos y guardados correctamente.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener los datos: {e}")

# Llamar a la función para obtener los datos
if __name__ == "__main__":
    fetch_bike_data()
