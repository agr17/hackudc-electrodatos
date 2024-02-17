from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

class ConsumptionsVisualizer:
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
            'formatted_time': new_data['datetime'].dt.strftime('%H:%M')
        }
