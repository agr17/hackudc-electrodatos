import pandas as pd
from src.data import load_data
from calendar import day_name
import numpy as np
import matplotlib.pyplot as plt


def _mean_consumption_by_day_of_week(df):
    df = pd.DataFrame(df.groupby(df['datetime'].dt.day_of_week)['consumo'].mean())
    df = df.reset_index()
    df = df.rename(columns={"consumo": "consumption", "datetime": "weekday"})
    return df

csv_path = "data/cups/electrodatos_0.csv"
df = load_data(csv_path)

# Media de consumo total
df_mean = df['consumo'].mean()
print("\n\nMedia de consumo total:\n")
print(df_mean)


# Media de consumo por día de la semana
print("\n\nMedia de consumo por día de la semana:\n")

df_mean_by_day_of_week = pd.DataFrame(df.groupby(df['datetime'].dt.day_of_week)['consumo'].mean())
print(df_mean_by_day_of_week)

# Día de la semana de más consumo de media
print("\n\nDía de la semana de más consumo de media:\n")
max_consumption = df_mean_by_day_of_week.loc[df_mean_by_day_of_week['consumo'].idxmax()]

print(day_name[max_consumption.name])


# Día de la semana de menos consumo de media
print("\n\nDía de la semana de menos consumo de media:\n")
min_consumption = df_mean_by_day_of_week.loc[df_mean_by_day_of_week['consumo'].idxmin()]

print(day_name[min_consumption.name])


# Día de mayor/menor consumo
print("\n\nDía de mayor consumo total:\n")
df0_sum_day_consumption = pd.DataFrame(df.groupby([df['datetime'].dt.year, 
                   df['datetime'].dt.month, 
                  df['datetime'].dt.day])['consumo'].sum())

max_day = df0_sum_day_consumption.loc[df0_sum_day_consumption['consumo'].idxmax()]

print("El día ", max_day.name[2], "/", max_day.name[1], "/", max_day.name[0], " el consumo fue ", max_day.max(), " KW/h")

print("\n\nDía de menor consumo total:\n")

min_day = df0_sum_day_consumption.loc[df0_sum_day_consumption['consumo'].idxmin()]

print("El día ", min_day.name[2], "/", min_day.name[1], "/", min_day.name[0], " el consumo fue ", min_day.min(), " KW/h")


# Consumo por horas
def consumption_hours(df):

    df_hora_mas_consumido = pd.DataFrame(df.groupby(df['datetime'].dt.hour)['consumo'].mean())
    df_hora_mas_consumido = df_hora_mas_consumido.reset_index()
    df_hora_mas_consumido = df_hora_mas_consumido.rename(columns={"consumo": "consumption", "datetime": "hour"})

    lowerLimit = 0

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    labels = ['{:02d}:00'.format(hours) for hours in df_hora_mas_consumido["hour"]]
    labels = [str(x) for x in labels]

    width = (2*np.pi / len(df_hora_mas_consumido.index))

    max = df_hora_mas_consumido['hour'].max()
    slope = (max - lowerLimit) / max
    heights = slope * df_hora_mas_consumido.consumption + lowerLimit

    # Compute angle for each category
    indexes = list(range(0, len(labels)))
    angles = [element * width for element in indexes]


    # Plot data
    ax.bar(x=angles,
        height=heights,
        width=width,
        color='skyblue',
        bottom=lowerLimit,
        linewidth=2,
        edgecolor="white"
        )

    # Add labels
    ax.set_xticks(angles)
    ax.set_xticklabels(labels)

    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_yticklabels([])

    plt.title(label="Consumo total por horas")


    # Show the plot
    #plt.show()
    plt.savefig('bokeh-vis/static/images/circular_barplot_hours.png')
