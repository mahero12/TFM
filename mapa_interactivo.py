pip install folium
import folium

# Crea un mapa centrado en Estados Unidos
mapa = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

# Guarda el mapa en un archivo HTML
mapa.save('mapa_interactivo.html')
