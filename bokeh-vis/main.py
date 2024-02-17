from consumptions_visualizer import ConsumptionsVisualizer
from utils.data import load_data

from bokeh.plotting import curdoc
from bokeh.layouts import column

import sys

from top_percentage_consumers import calcular_porcentaje_top

# Get the arguments
if len(sys.argv) != 2:
    print("Usage: bokeh serve bokeh-vis [--show] --args <csv>")
    print("Your input: ", sys.argv)

csv_path = sys.argv[1]

df = load_data(csv_path)

consumption_vis = ConsumptionsVisualizer()
consumption_vis.update_source(df)

plot = consumption_vis.get_plot()

layout = column(plot, sizing_mode="stretch_width")
curdoc().add_root(layout)

# Obtener el porcentaje top
year = "2021"
porcentaje_top = calcular_porcentaje_top(csv_path, year)
curdoc().template_variables["porcentaje_top"] = porcentaje_top
curdoc().template_variables["year"] = year