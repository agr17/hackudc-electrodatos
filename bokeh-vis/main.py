from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure

class ConsumptionsVisualization:
    def __init__(self):
        super().__init__()
        self.source = ColumnDataSource(data=self._get_empty_source())

    def _get_empty_source(self):
        return {
            'consumption': [],
            'time': [],
        }

    def get_plot(self):

        tooltips = [
            ("Día", "@formatted_date"),
            ("Hora", "@formatted_time"),
            ("Consumo ", "$y KWh"),
        ]

        p = figure(
            title="Gráfica de Consumo",
            x_axis_label='Día',
            y_axis_label='Consumo (KWh)',
            sizing_mode="stretch_width",
            x_axis_type="datetime",
            tooltips=tooltips
        )

        p.line(x='time', y='consumption', source=self.source)

        return p

    def update_source(self, new_data):
        self.source.data = {
            'consumption': new_data['consumo'],
            'time': new_data['datetime'],
            'formatted_date': new_data['datetime'].dt.strftime('%d-%m-%Y'),
            'formatted_time': new_data['datetime'].dt.strftime('%H:%M') # Add this line
        }

####################################################################################################

from bokeh.plotting import curdoc
from bokeh.layouts import column
import pandas as pd
import sys

def load_data(csv_path):
    df = pd.read_csv(csv_path)
    df['fecha'] = df['fecha'].apply(lambda x: pd.Timestamp(x))
    df['datetime'] = pd.to_datetime(df['datetime'])

    return df

# Get the arguments
if len(sys.argv) != 2:
    print("Usage: bokeh serve bokeh-vis [--show] --args <csv>")
    print("Your input: ", sys.argv)

csv_path = sys.argv[1]

df = load_data(csv_path)

consumption_vis = ConsumptionsVisualization()
consumption_vis.update_source(df)

plot = consumption_vis.get_plot()

layout = column(plot, sizing_mode="stretch_width")
curdoc().add_root(layout)

