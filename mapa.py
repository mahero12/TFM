import pandas as pd

# Leer los datos climáticos desde el archivo Excel
datos_climaticos = pd.read_excel("prueba.xlsx")

# Crear un diccionario para mapear los estados a los datos climáticos
clima_estados = {}
for index, row in datos_climaticos.iterrows():
    estado = row["Estado"]
    clima_estados[estado] = {
        "Temperatura": row["Temperatura"],
        "Viento": row["Viento"],
        "Precipitaciones": row["Precipitaciones"]
    }
