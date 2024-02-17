import os
import pandas as pd

# Lista para almacenar los resultados de cada CUPS
consumo_medio_por_hora = []

# Directorio donde se encuentran los archivos CSV de los CUPS
data_directory = "../data/cups"
total_cups = 11

# Iterar sobre los archivos de datos de cada CUPS (electrodatos_0.csv a electrodatos_9.csv)
for cups_id in range(total_cups):
    # Ruta al archivo CSV correspondiente al CUPS actual
    file_path = os.path.join(data_directory, f"electrodatos_{cups_id}.csv")
    data = pd.read_csv(file_path, parse_dates=["datetime"])
    
    # Calcular el consumo medio por hora
    consumo_medio = data.groupby(data['datetime'].dt.hour)['consumo'].mean()
    
    # Agregar los resultados a la lista
    consumo_medio_por_hora.append(consumo_medio)

# Convertir la lista de resultados en un DataFrame
consumo_medio_por_hora_df = pd.DataFrame(consumo_medio_por_hora)

# Transponer el DataFrame para que los CUPS sean filas y las horas sean columnas
consumo_medio_por_hora_df = consumo_medio_por_hora_df.T

# Asignar nombres de columnas
consumo_medio_por_hora_df.columns = [f"CUPS_{cups_id}" for cups_id in range(total_cups)]

# Mostrar el DataFrame con los resultados
print("\n\nConsumos medios:\n")
print(consumo_medio_por_hora_df)
