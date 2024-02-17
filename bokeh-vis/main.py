from consumptions_visualizer import ConsumptionsVisualizer
from costs_visualizer import CostsVisualizer
import src.petitions as cost_data
import src.data as consumption_data

from bokeh.models import Div
from bokeh.plotting import curdoc
from bokeh.layouts import column

import sys

def _unify_data(df_consumption, df_costs):
        df = df_consumption.set_index('datetime').join(df_costs.set_index('datetime'))
        df.reset_index(inplace=True)
        return df

# Get the arguments

if len(sys.argv) != 2:
    print("Usage: bokeh serve bokeh-vis [--show] --args <csv>")
    print("Your input: ", sys.argv)

csv_path = sys.argv[1]

# Load the data

df_consumption = consumption_data.load_data(csv_path)
df_costs = cost_data.read_data("2022-01-01", "2022-06-01")

df = _unify_data(df_consumption, df_costs)
df.dropna(inplace=True) # TODO: esto es temporal para filtrar rapido

# Create visualizers

consumption_vis = ConsumptionsVisualizer()
consumption_vis.update_source(df_consumption)

cost_div = Div(text="<h2>Coste por día y hora</h2>")

costs_vis = CostsVisualizer()
costs_vis.update_source(df)

# Get the plots

plot = consumption_vis.get_plot()
p_cost = costs_vis.get_plot()

# Create the layout

layout = column(plot, cost_div, p_cost, sizing_mode="stretch_width")
curdoc().add_root(layout)

