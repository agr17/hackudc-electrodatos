import pandas as pd
import os
from pathlib import Path

def calcular_porcentaje_top(csv_path, year):
    # Directorio donde se encuentran los archivos CSV de los CUPS
    data_directory = Path("./data/cups")

    # Obtener la lista de archivos en el directorio
    archivos_cups = os.listdir(data_directory)
    # Contar el número de archivos en el directorio
    numero_total_cups = len(archivos_cups)

    # Lista para almacenar los consumos totales de los CUPS
    consumos_totales_cups = []

    # Iterar sobre los archivos de datos de CUPS (electrodatos_cups_id.csv)
    for cups_id in range(numero_total_cups):
        # Ruta al archivo CSV correspondiente al CUPS actual
        file_path = os.path.join(data_directory, f"electrodatos_{cups_id}.csv")
        
        # Verificar si el archivo es diferente al proporcionado por el usuario
        if file_path != csv_path:
            data = pd.read_csv(file_path)
            
            # Filtrar los datos por año
            data = data[data['datetime'].str.startswith(year)]
            # Sumar el consumo total del CUPS actual y agregarlo a la lista
            consumos_totales_cups.append(data['consumo'].sum())
        else:
            # Si el fichero está entre los datos no contabilizarlo
            numero_total_cups=numero_total_cups-1

    # Calcular el consumo total del CUPS del input
    file_path_input = os.path.join(csv_path)
    data_input = pd.read_csv(file_path_input)
    data_input = data_input[data_input['datetime'].str.startswith(year)]
    consumo_total_input = data_input['consumo'].sum()

    # Cálculo Porcentaje
    # Contar cuántos consumos totales de los primeros 10 CUPS son menores que el consumo total del décimo CUPS
    consumos_superados = sum(1 for consumo_total in consumos_totales_cups if consumo_total < consumo_total_input)

    # Calcular el porcentaje de usuarios superados
    porcentaje_superado = (consumos_superados / numero_total_cups) * 100
    porcentaje_top = 100 - porcentaje_superado

    # Mostrar el porcentaje de usuarios superados
    # print(f"Estás en el top {porcentaje_top:.2f}% de los consumidores")
    return porcentaje_top