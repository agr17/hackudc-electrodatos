import pandas as pd
import os

# Directorio donde se encuentran los archivos CSV de los CUPS
data_directory = "../data/cups"
numero_total_cups = 10

# Lista para almacenar los consumos totales de los primeros 10 CUPS
consumos_totales_10_cups = []

# Iterar sobre los archivos de datos de los primeros 10 CUPS (electrodatos_0.csv a electrodatos_9.csv)
for cups_id in range(numero_total_cups):
    # Ruta al archivo CSV correspondiente al CUPS actual
    file_path = os.path.join(data_directory, f"electrodatos_{cups_id}.csv")
    data = pd.read_csv(file_path)
    
    # Sumar el consumo total del CUPS actual y agregarlo a la lista
    consumos_totales_10_cups.append(data['consumo'].sum())

# Calcular el consumo total del CUPS 11
file_path_11 = os.path.join(data_directory, "electrodatos_10.csv")
data_11 = pd.read_csv(file_path_11)
consumo_total_11 = data_11['consumo'].sum()

# Determinar en qué puesto de la lista estaría el consumo total del décimo CUPS
# Suma 1 puesto si el consumo total de un elemento de la lista es mayor que el que estamos inputando
# puesto_cups_11 = sum(1 for consumo_total in consumos_totales_10_cups if consumo_total > consumo_total_11) + 1
# Mostrar el puesto del CUPS 10 en la lista
#print(f"El CUPS 11 está en el puesto {puesto_cups_11} en la lista de consumos totales de los primeros 10 CUPS")

## Porcentaje
# Contar cuántos consumos totales de los primeros 10 CUPS son menores que el consumo total del décimo CUPS
consumos_superados = sum(1 for consumo_total in consumos_totales_10_cups if consumo_total < consumo_total_11)

# Calcular el porcentaje de usuarios superados
porcentaje_superado = (consumos_superados / numero_total_cups) * 100
porcentaje_top = 100-porcentaje_superado

# Mostrar el porcentaje de usuarios superados
print(f"Estás en el top {porcentaje_top:.2f}% de los consumidores")