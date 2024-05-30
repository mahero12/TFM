import folium
from folium.plugins import MarkerCluster
import pandas as pd

# Coordenadas y descripciones de los estados de EE.UU.
us_states_coords = {
    "Alabama": {"lat": 32.8067, "lon": -86.7911, "desc": "Conocido por su papel en la Guerra Civil y el Movimiento por los Derechos Civiles."},
    "Alaska": {"lat": 61.3707, "lon": -152.4044, "desc": "El estado más grande de EE.UU., famoso por su naturaleza y vida salvaje."},
    "Arizona": {"lat": 33.7298, "lon": -111.4312, "desc": "Hogar del Gran Cañón y conocido por su clima desértico."},
    "Arkansas": {"lat": 34.9697, "lon": -92.3731, "desc": "Famoso por sus parques y áreas naturales, incluyendo Hot Springs."},
    "California": {"lat": 36.1162, "lon": -119.6816, "desc": "Conocido por Hollywood, Silicon Valley y sus diversas geografías."},
    "Colorado": {"lat": 39.0598, "lon": -105.3111, "desc": "Hogar de las Montañas Rocosas y famoso por su industria de esquí."},
    "Connecticut": {"lat": 41.5978, "lon": -72.7554, "desc": "Uno de los trece estados originales, conocido por sus instituciones educativas."},
    "Delaware": {"lat": 39.3185, "lon": -75.5071, "desc": "El primer estado en ratificar la Constitución de EE.UU."},
    "Florida": {"lat": 27.7663, "lon": -81.6868, "desc": "Famoso por sus playas, parques temáticos y clima cálido."},
    "Georgia": {"lat": 33.0406, "lon": -83.6431, "desc": "Conocido por su historia en la Guerra Civil y su industria del melocotón."},
    "Hawaii": {"lat": 21.0943, "lon": -157.4983, "desc": "Un archipiélago en el Pacífico, famoso por sus paisajes y cultura única."},
    "Idaho": {"lat": 44.2405, "lon": -114.4788, "desc": "Conocido por sus vastas áreas naturales y producción de papas."},
    "Illinois": {"lat": 40.3495, "lon": -88.9861, "desc": "Hogar de Chicago, una de las ciudades más grandes de EE.UU."},
    "Indiana": {"lat": 39.8494, "lon": -86.2583, "desc": "Conocido por la carrera de autos Indianápolis 500."},
    "Iowa": {"lat": 42.0115, "lon": -93.2105, "desc": "Un estado agrícola, conocido por su producción de maíz."},
    "Kansas": {"lat": 38.5266, "lon": -96.7265, "desc": "Famoso por sus vastas llanuras y paisajes agrícolas."},
    "Kentucky": {"lat": 37.6681, "lon": -84.6701, "desc": "Conocido por el Derby de Kentucky y su bourbon."},
    "Louisiana": {"lat": 31.1695, "lon": -91.8678, "desc": "Famoso por Nueva Orleans, el jazz y su cocina cajún y criolla."},
    "Maine": {"lat": 44.6939, "lon": -69.3819, "desc": "Conocido por sus costas rocosas y mariscos, especialmente la langosta."},
    "Maryland": {"lat": 39.0639, "lon": -76.8021, "desc": "Hogar del puerto de Baltimore y conocido por su historia colonial."},
    "Massachusetts": {"lat": 42.2302, "lon": -71.5301, "desc": "Uno de los trece estados originales, conocido por Boston y su historia revolucionaria."},
    "Michigan": {"lat": 43.3266, "lon": -84.5361, "desc": "Rodeado por los Grandes Lagos, conocido por su industria automotriz."},
    "Minnesota": {"lat": 45.6945, "lon": -93.9002, "desc": "Conocido por sus lagos y parques naturales, y como la tierra de los 10,000 lagos."},
    "Mississippi": {"lat": 32.7416, "lon": -89.6787, "desc": "Famoso por su música blues y su historia en la Guerra Civil."},
    "Missouri": {"lat": 38.4561, "lon": -92.2884, "desc": "Hogar de Gateway Arch en St. Louis y conocido por su música y barbacoa."},
    "Montana": {"lat": 46.9219, "lon": -110.4544, "desc": "Conocido por sus paisajes montañosos y áreas naturales como el Parque Nacional de Yellowstone."},
    "Nebraska": {"lat": 41.1254, "lon": -98.2681, "desc": "Conocido por sus vastas llanuras y paisajes agrícolas."},
    "Nevada": {"lat": 38.3135, "lon": -117.0554, "desc": "Hogar de Las Vegas, conocida por su industria de casinos y entretenimiento."},
    "New Hampshire": {"lat": 43.4525, "lon": -71.5639, "desc": "Conocido por sus paisajes naturales y la primera primaria en el ciclo electoral presidencial."},
    "New Jersey": {"lat": 40.2989, "lon": -74.521, "desc": "Conocido por su industria y playas en la costa del Atlántico."},
    "New Mexico": {"lat": 34.8405, "lon": -106.2485, "desc": "Famoso por su cultura nativa americana y paisajes desérticos."},
    "New York": {"lat": 42.1657, "lon": -74.9481, "desc": "Hogar de la ciudad de Nueva York, un centro mundial de cultura y finanzas."},
    "North Carolina": {"lat": 35.6301, "lon": -79.8064, "desc": "Conocido por sus playas en el Atlántico y su industria tecnológica en Research Triangle."},
    "North Dakota": {"lat": 47.5289, "lon": -99.784, "desc": "Famoso por sus paisajes de pradera y la producción de petróleo."},
    "Ohio": {"lat": 40.3888, "lon": -82.7649, "desc": "Conocido por su industria y el Salón de la Fama del Rock and Roll en Cleveland."},
    "Oklahoma": {"lat": 35.5653, "lon": -96.9289, "desc": "Conocido por su historia nativa americana y su industria petrolera."},
    "Oregon": {"lat": 44.572, "lon": -122.0709, "desc": "Famoso por sus paisajes naturales, incluyendo bosques, montañas y la costa del Pacífico."},
    "Pennsylvania": {"lat": 40.5908, "lon": -77.2098, "desc": "Uno de los trece estados originales, conocido por Filadelfia y su historia revolucionaria."},
    "Rhode Island": {"lat": 41.6809, "lon": -71.5118, "desc": "El estado más pequeño de EE.UU., conocido por sus costas y arquitectura colonial."},
    "South Carolina": {"lat": 33.8569, "lon": -80.945, "desc": "Conocido por su historia en la Guerra Civil y sus playas en Myrtle Beach."},
    "South Dakota": {"lat": 44.2998, "lon": -99.4388, "desc": "Hogar del Monte Rushmore y conocido por sus paisajes de pradera."},
    "Tennessee": {"lat": 35.7478, "lon": -86.6923, "desc": "Famoso por su música country y el Parque Nacional Great Smoky Mountains."},
    "Texas": {"lat": 31.0545, "lon": -97.5635, "desc": "El segundo estado más grande de EE.UU., conocido por su cultura y economía diversa."},
    "Utah": {"lat": 40.15, "lon": -111.8624, "desc": "Conocido por sus parques nacionales y la sede de la Iglesia de Jesucristo de los Santos de los Últimos Días."},
    "Vermont": {"lat": 44.0459, "lon": -72.7107, "desc": "Famoso por sus paisajes rurales y producción de jarabe de arce."},
    "Virginia": {"lat": 37.7693, "lon": -78.1699, "desc": "Uno de los trece estados originales, conocido por su historia colonial y revolucionaria."},
    "Washington": {"lat": 47.4009, "lon": -121.4905, "desc": "Hogar de Seattle y conocido por su industria tecnológica y paisajes naturales."},
    "West Virginia": {"lat": 38.4912, "lon": -80.9545, "desc": "Conocido por sus montañas y actividades al aire libre como el senderismo y la escalada."},
    "Wisconsin": {"lat": 44.2685, "lon": -89.6165, "desc": "Famoso por su industria lechera y producción de queso."},
    "Wyoming": {"lat": 42.756, "lon": -107.3025, "desc": "Conocido por sus paisajes naturales y el Parque Nacional de Yellowstone."},
}

datos_climaticos = pd.read_excel("prueba.xlsx")

def show_weather(state):
    # Obtener los datos climáticos para el estado seleccionado y el mes seleccionado
    clima_estado_mes = clima_por_estado[state]
    # Mostrar el clima en una ventana emergente
    print(f"Clima en {state}: {clima_estado_mes}")

# Crear un diccionario para mapear los estados a los datos climáticos
clima_por_estado = {}
for index, row in datos_climaticos.iterrows():
    estado = row["Estado"]
    clima_por_estado[estado] = {
        "Temperatura": row["Temperatura"],
        "Viento": row["Viento"],
        "Precipitaciones": row["Precipitaciones"]
    }

def create_map(coords, latitude, longitude, zoom, tiles='OpenStreetMap'):
    """
    Generate a Folium Map with clustered markers of the provided coordinates.
    """
    world_map = folium.Map(location=[latitude, longitude], zoom_start=zoom, tiles=tiles, 
                           control_scale=True, zoom_control=True, box_zoom=False)
    marker_cluster = MarkerCluster().add_to(world_map)

    # Add a marker for each state
    for state, loc in coords.items():
        html = f"""
        <h4>{state}</h4>
        <p>{loc['desc']}</p>
        <label for='month_{state}'>Selecciona un mes:</label>
        <select id='month_{state}' name='month' onchange='showWeather("{state}", this.value)'>            
            <option value='agosto'>Agosto 2022</option>
            <option value='septiembre'>Septiembre 2022</option>
            <option value='octubre'>Octubre 2022</option>
            <option value='noviembre'>Noviembre 2022</option>
            <option value='diciembre'>Diciembre 2022</option>
            <option value='enero'>Enero 2023</option>
            <option value='febrero'>Febrero 2023</option>
        </select>
        """
        iframe = folium.IFrame(html=html, width=250, height=200)
        popup = folium.Popup(iframe, max_width=300)
        folium.Marker(
            location=[loc['lat'], loc['lon']],
            popup=popup
        ).add_to(marker_cluster)

    return world_map

# Crear el mapa centrado en el centro geográfico de los EE.UU.
map_us = create_map(us_states_coords, 39.50, -98.35, 4)

# Obtener el HTML del mapa generado
index_html = map_us.get_root().render()

# Guardar el HTML en un archivo
with open('mapa.html', 'w') as f:
    f.write(index_html)
