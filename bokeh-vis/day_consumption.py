# SPDX-FileCopyrightText: 2024 Manuel Corujo
# SPDX-FileCopyrightText: 2024 María López
# SPDX-FileCopyrightText: 2024 Pablo Boo
# SPDX-FileCopyrightText: 2024 Ángel Regueiro
#
# SPDX-License-Identifier: MIT

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.constants import *

# Consumo medio por día de la semana
def _mean_consumption_by_day_of_week(df):
    df = pd.DataFrame(df.groupby(df['datetime'].dt.day_of_week)['consumo'].mean())
    df = df.reset_index()
    return df

# Día de la semana con mayor/menor consumo
def _week_day_most_least_consumption(df):
    df_mean_consumption = _mean_consumption_by_day_of_week(df)
    max_consumption = df_mean_consumption.loc[df_mean_consumption['consumo'].idxmax()]
    min_consumption = df_mean_consumption.loc[df_mean_consumption['consumo'].idxmin()]
    return WEEK_DAYS_DICT[max_consumption.name], WEEK_DAYS_DICT[min_consumption.name]

def _day_of_year_most_least_consumption(df):
    df0_sum_day_consumption = pd.DataFrame(df.groupby([df['datetime'].dt.year,
                                                       df['datetime'].dt.month,
                                                       df['datetime'].dt.day])['consumo'].sum())
    max_day = df0_sum_day_consumption.loc[df0_sum_day_consumption['consumo'].idxmax()]
    min_day = df0_sum_day_consumption.loc[df0_sum_day_consumption['consumo'].idxmin()]
    max_day.name = max_day.name[::-1]
    min_day.name = min_day.name[::-1]
    return max_day, min_day

# Consumo medio por horas
def _consumption_hours(df):
    df_mean_hour_consumption = pd.DataFrame(df.groupby(df['datetime'].dt.hour)['consumo'].mean())
    df_mean_hour_consumption = df_mean_hour_consumption.reset_index()
    df_mean_hour_consumption = df_mean_hour_consumption.rename(columns={"consumo": "consumption", "datetime": "hour"})

    lowerLimit = 0

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    max = df_mean_hour_consumption['hour'].max()
    slope = (max - lowerLimit) / max
    heights = slope * df_mean_hour_consumption.consumption + lowerLimit

    # Compute angle for each category
    labels = ['{:02d}:00'.format(hours) for hours in df_mean_hour_consumption["hour"]]
    labels = [str(x) for x in labels]
    width = (2*np.pi / len(df_mean_hour_consumption.index))
    indexes = list(range(0, len(labels)))
    angles = [element * width for element in indexes]

    # Plot data
    ax.bar(x=angles,
        height=heights,
        width=width,
        color=CONSUMPTION_COLOR,
        bottom=lowerLimit,
        linewidth=2,
        edgecolor="white"
        )

    # Add labels
    ax.set_xticks(angles)
    ax.set_xticklabels(labels)
    ax.set_yticklabels([])

    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)

    # legend with label Consumo
    ax.bar(0, 0, color='skyblue', label='Consumo')
    # legend in the max upper right corner
    # plt.legend(loc='upper right')
    # plt.title(label="Consumo total por horas")

    # Save plot
    plt.savefig('bokeh-vis/static/images/circular_barplot_hours.png')
