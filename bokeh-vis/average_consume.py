import pandas as pd
import os

def calcular_average_consume(csv_path, year):
    # Directorio donde se encuentran los archivos CSV de los CUPS
    data_directory = ".\data\cups"

    # Obtener la lista de archivos en el directorio
    archivos_cups = os.listdir(data_directory)
    # Contar el número de archivos en el directorio
    numero_total_cups = len(archivos_cups)

    # Lista para almacenar los resultados de cada CUPS
    consumo_medio_por_cups = []

    # Iterar sobre los archivos de datos de cada CUPS (electrodatos_0.csv a electrodatos_9.csv)
    for cups_id in range(numero_total_cups):
        # Ruta al archivo CSV correspondiente al CUPS actual
        file_path = os.path.join(data_directory, f"electrodatos_{cups_id}.csv")
        # Verificar si el archivo es diferente al proporcionado por el usuario
        if file_path != csv_path:
            data = pd.read_csv(file_path)
             # Filtrar los datos por año
            data = data[data['datetime'].str.startswith(year)]

            data = pd.read_csv(file_path)
            # Calcular el consumo medio
            consumo_medio = data['consumo'].mean()
            
            # Agregar el resultado a la lista
            consumo_medio_por_cups.append(consumo_medio)

    # Calcular la media final de todos los CUPS
    media_final = sum(consumo_medio_por_cups) / len(consumo_medio_por_cups)

    # Mostrar el consumo medio por CUPS y la media final
    for cups_id, consumo_medio in enumerate(consumo_medio_por_cups):
        print(f"CUPS {cups_id}: Consumo medio = {consumo_medio:.2f} kWh/h")

    print(f"Media Final de todos los CUPS: {media_final:.2f} kWh/h")


    # Calculo media del archivo del usuario
    file_path_input = os.path.join(csv_path)
    data_input = pd.read_csv(file_path_input)
    data_input = data_input[data_input['datetime'].str.startswith(year)]
    consumo_medio_input = data_input['consumo'].mean()

    # Comparamos el consumo medio del fichero CSV de input con la media anterior
    if consumo_medio_input > media_final:
        comparacion = "superior"
    elif consumo_medio_input < media_final:
        comparacion = "inferior"
    else:
        comparacion = "igual"

    print("\n\nMÉTRICA WRAPPED:\n")
    print(f"De media el resto de usuarios ha consumido: {media_final:.2f} kWh/h")
    print(f"Tu consumo medio es {comparacion} a la media ({consumo_medio_input:.2f} kWh/h).")

    return {
        "media_existente": "{:.2f}".format(media_final),
        "consumo_medio_input": "{:.2f}".format(consumo_medio_input),
        "comparacion": comparacion
    }