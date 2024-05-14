pip install folium
import folium
from folium.plugins import MarkerCluster
import pandas as pd
import requests

# URL de descarga directa del archivo CSV en Google Drive
file_url = "https://drive.google.com/uc?export=download&id=1cIur-I2blbheoWd6fcLxt9WX-19HY9oG"

# Descargar el archivo CSV desde Google Drive
response = requests.get(file_url)

# Guardar el archivo CSV en el disco
with open("US_Accidents.csv", "wb") as f:
    f.write(response.content)

# Leer el archivo CSV en un DataFrame de Pandas
df = pd.read_csv("US_Accidents.csv")


# Filtrar datos y crear el mapa
df_loc = df.loc[(~df.Start_Lat.isna()) & (~df.Start_Lng.isna())]

def create_map(df_loc, latitude, longitude, zoom, tiles='OpenStreetMap'):
    """
    Generate a Folium Map with clustered markers of accident locations.
    """
    world_map = folium.Map(location=[latitude, longitude], zoom_start=zoom, tiles=tiles)
    marker_cluster = MarkerCluster().add_to(world_map)

    # Iterar sobre las filas del DataFrame y añadir cada marcador al clúster
    for idx, row in df_loc.iterrows():
        folium.Marker(
            location=[row['Start_Lat'], row['Start_Lng']],
            # Puedes añadir más atributos a tu marcador aquí, como un popup
            popup=f"Lat, Lng: {row['Start_Lat']}, {row['Start_Lng']}"
        ).add_to(marker_cluster)

    return world_map

# Coordenadas para centrar el mapa
latitude = 39.50
longitude = -98.35

# Crear el mapa
map_us = create_map(df_loc, latitude, longitude, 4)

# Guardar el HTML en un archivo
map_us.save("mapa.html")
