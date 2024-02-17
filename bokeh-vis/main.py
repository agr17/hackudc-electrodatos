from monthly_consumption import MonthlyConsumption
from general_bars import GeneralBars
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

def _data_to_monthly(df):
    df_copy = df.copy()
    df_copy['month'] = df_copy['datetime'].dt.to_period('M')
    result = df_copy.groupby('month').agg({'consumo': 'sum', 'price': 'sum'}).reset_index()
    result.columns = ['month', 'consumo', 'price']
    return result

# Get the arguments

if len(sys.argv) != 2:
    print("Usage: bokeh serve bokeh-vis [--show] --args <csv>")
    print("Your input: ", sys.argv)

csv_path = sys.argv[1]

# Load the data

df_consumption = consumption_data.load_data(csv_path)
df_costs = cost_data.read_costs("2022-01-01", "2022-12-31")

df = _unify_data(df_consumption, df_costs)
df.dropna(inplace=True) # TODO: esto es temporal para filtrar rapido

df_monthly = _data_to_monthly(df)
df_monthly = df_monthly[df_monthly['month'] < "2023-01"]

# Create visualizers

general_bars = GeneralBars()
general_bars.update_source(df_monthly)

consumptions_visualizer = MonthlyConsumption(df)
consumptions_visualizer.update_source()

# Get the plots

bars_plot = general_bars.get_plot()
consumptions_plot = consumptions_visualizer.get_layout()

# Create the layout

layout = column(bars_plot, consumptions_plot, sizing_mode="stretch_width")
curdoc().add_root(layout)

