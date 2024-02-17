# SPDX-FileCopyrightText: 2024 Manuel Corujo
# SPDX-FileCopyrightText: 2024 María López
# SPDX-FileCopyrightText: 2024 Pablo Boo
# SPDX-FileCopyrightText: 2024 Ángel Regueiro
#
# SPDX-License-Identifier: MIT

from monthly_consumption import MonthlyConsumption
from general_bars import GeneralBars
from day_consumption_visualizer import DayConsumptionVisualizer
from day_consumption import consumption_hours
import src.petitions as cost_data
import src.data as consumption_data

from bokeh.models import Div
from bokeh.plotting import curdoc
from bokeh.layouts import column

import pandas as pd
import sys

from top_percentage_consumers import calcular_porcentaje_top
from average_consume import calcular_average_consume

def _mean_consumption_by_day_of_week(df):
    df = pd.DataFrame(df.groupby(df['datetime'].dt.day_of_week)['consumo'].mean())
    df = df.reset_index()
    df = df.rename(columns={"consumo": "consumption", "datetime": "weekday"})
    return df

# Get the arguments

if len(sys.argv) != 3:
    print("Usage: bokeh serve bokeh-vis [--show] --args <csv> <year>")
    print("Your input: ", sys.argv)

csv_path = sys.argv[1]
year = sys.argv[2]

# Load the data

df_consumption = consumption_data.load_data(csv_path)

# check if the year exist in datetime column
if not consumption_data.check_year(df_consumption, year):
    print(f"Year {year} not found in the data")
    sys.exit(1)

df_costs = cost_data.read_costs(f"{year}-01-01", f"{year}-12-31")

df = consumption_data.unify_data(df_consumption, df_costs)
df.dropna(inplace=True) # TODO: esto es temporal para filtrar rapido

df = consumption_data.calculate_expenses(df)

df_monthly = consumption_data.data_to_monthly(df)
df_monthly = df_monthly[df_monthly['month'] < "2023-01"]

df_weekday = _mean_consumption_by_day_of_week(df)

# Use matplotlib to get the consumption by hours
consumption_hours(df)

# Create visualizers

general_bars = GeneralBars()
general_bars.update_source(df_monthly)

consumptions_visualizer = MonthlyConsumption(df)
consumptions_visualizer.update_source()

consumption_vis = DayConsumptionVisualizer()
consumption_vis.update_source(df_weekday)


# Get the plots

bars_plot = general_bars.get_plot()
consumptions_plot = consumptions_visualizer.get_layout()

weekday_plot = consumption_vis.get_plot()

# H2 titles between the plots

style = "style='font-size: 1.5rem;'"

bars_plot_title = Div(text=f"<h2 {style}>Consumo mensual</h2>")
consumptions_plot_title = Div(text=f"<h2 {style}>Consumo mensual</h2>")
weekday_plot_title = Div(text=f"<h2 {style}>Consumo por día de la semana</h2>")

# Create the layout

layout = column(
    bars_plot_title,
    bars_plot,
    consumptions_plot_title,
    consumptions_plot,
    weekday_plot_title,
    weekday_plot,
    sizing_mode="stretch_width")

curdoc().add_root(layout)

# Obtener el porcentaje top del año
porcentaje_top = calcular_porcentaje_top(csv_path, year)
curdoc().template_variables["porcentaje_top"] = porcentaje_top
curdoc().template_variables["year"] = year

# Obtener el consumo medio del año
resultados = calcular_average_consume(df, csv_path, year)
curdoc().template_variables["media_existente"] = resultados["media_existente"]
curdoc().template_variables["consumo_medio_input"] = resultados["consumo_medio_input"]
curdoc().template_variables["comparacion"] = resultados["comparacion"]
curdoc().template_variables["gasto_total"] = resultados["gasto_total"]
curdoc().template_variables["gasto_media"] = resultados["gasto_media"]
