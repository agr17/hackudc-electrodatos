# SPDX-FileCopyrightText: 2024 Manuel Corujo
# SPDX-FileCopyrightText: 2024 María López
# SPDX-FileCopyrightText: 2024 Pablo Boo
# SPDX-FileCopyrightText: 2024 Ángel Regueiro
#
# SPDX-License-Identifier: MIT

from monthly_consumption import MonthlyConsumption
from general_bars import GeneralBars
from day_consumption_visualizer import DayConsumptionVisualizer
from day_consumption import _consumption_hours, _mean_consumption_by_day_of_week, _week_day_most_least_consumption, _day_of_year_most_least_consumption
import src.petitions as cost_data
import src.data as consumption_data
from src.constants import *

from bokeh.models import Div
from bokeh.plotting import curdoc
from bokeh.layouts import column

import sys

from top_percentage_consumers import calcular_porcentaje_top
from average_consume import calcular_average_consume

def _data_to_monthly(df):
    df_copy = df.copy()
    df_copy['month'] = df_copy['datetime'].dt.to_period('M')
    result = df_copy.groupby('month').agg({'consumo': 'sum', 'expenses': 'sum'}).reset_index()
    result.columns = ['month', 'consumo', 'expenses']
    return result

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

df_costs = cost_data.read_costs(f"{year}-06-01" if year == "2021" else f"{year}-01-01", f"{year}-12-31") # TODO: retrive data from 2021 completely

df = consumption_data.unify_data(df_consumption, df_costs)
df.dropna(inplace=True) # TODO: esto es temporal para filtrar rapido

df = consumption_data.calculate_expenses(df)

df_monthly = consumption_data.data_to_monthly(df)

df_weekday = _mean_consumption_by_day_of_week(df)

# Use matplotlib to get the consumption by hours
_consumption_hours(df)

# Create visualizers

general_bars = GeneralBars(df_monthly)

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

# Obtener días más/menos consumo
week_days_most_least_consumption = _week_day_most_least_consumption(df)
curdoc().template_variables["most_consumption"] = week_days_most_least_consumption[0].upper()
curdoc().template_variables["least_consumption"] = week_days_most_least_consumption[1].upper()

# Obtener días del año de mayor/menor consumo
max, min = _day_of_year_most_least_consumption(df)

curdoc().template_variables["max_day"] = max.name[0]
curdoc().template_variables["max_month"] = MONTHS_DICT[max.name[1]]
curdoc().template_variables["max_year"] = max.name[2]
curdoc().template_variables["max_cons"] = max.max()

curdoc().template_variables["min_day"] = min.name[0]
curdoc().template_variables["min_month"] = MONTHS_DICT[min.name[1]]
curdoc().template_variables["min_year"] = min.name[2]
curdoc().template_variables["min_cons"] = min.min()

curdoc().template_variables["gasto_total"] = resultados["gasto_total"]
curdoc().template_variables["gasto_media"] = resultados["gasto_media"]
