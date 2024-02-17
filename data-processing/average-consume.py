import pandas as pd
import os

# Directorio donde se encuentran los archivos CSV de los CUPS
data_directory = "../data/cups"

# Lista para almacenar los resultados de cada CUPS
consumo_medio_por_cups = []

# Iterar sobre los archivos de datos de cada CUPS (electrodatos_0.csv a electrodatos_9.csv)
for cups_id in range(10):
    # Ruta al archivo CSV correspondiente al CUPS actual
    file_path = os.path.join(data_directory, f"electrodatos_{cups_id}.csv")
    data = pd.read_csv(file_path, parse_dates=["datetime"])
    
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


# Calculo media del archivo del usuario (en este caso el número 10)
file_path_10 = os.path.join(data_directory, "electrodatos_10.csv")
data_10 = pd.read_csv(file_path_10, parse_dates=["datetime"])
consumo_medio_10 = data_10['consumo'].mean()

# Comparamos el consumo medio del fichero CSV 10 con la media anterior
if consumo_medio_10 > media_final:
    comparacion = "superior"
elif consumo_medio_10 < media_final:
    comparacion = "inferior"
else:
    comparacion = "igual"

print("\n\nMÉTRICA WRAPPED:\n")
print(f"De media el resto de usuarios ha consumido: {media_final:.2f} kWh/h")
print(f"Tu consumo medio es {comparacion} a la media ({consumo_medio_10:.2f} kWh/h).")