import pandas as pd
import folium
import os

# Cargar datos con latitud y longitud
data_path = 'data/processed/citybikes_location.csv'
df = pd.read_csv(data_path)

# Eliminar filas sin coordenadas
df = df.dropna(subset=['latitude', 'longitude'])

# Crear mapa centrado en coordenadas medias
avg_lat = df['latitude'].mean()
avg_lon = df['longitude'].mean()
m = folium.Map(location=[avg_lat, avg_lon], zoom_start=2, tiles='CartoDB dark_matter' ,no_wrap =True)



# Añadir marcadores al mapa
for _, row in df.iterrows():
    tooltip = f"{row['name']} ({row['country']})"
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=row['name'],
        tooltip=tooltip,
        icon=folium.Icon(color='lightblue', icon='bicycle', prefix='fa')
    ).add_to(m)

# Guardar el mapa
output_path = 'src/visualization/world_bike_map.html'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
m.save(output_path)

print(f"Mapa guardado como: {output_path}")
