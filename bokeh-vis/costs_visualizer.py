from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

class CostsVisualizer:
    def __init__(self):
        super().__init__()
        self.source = ColumnDataSource(data=self._get_empty_source())

    def _get_empty_source(self):
        return {
            'cost': [],
            'time': [],
        }

    def get_plot(self):

        tooltips = [
            ("Día", "@formatted_date"),
            ("Hora", "@formatted_time"),
            ("Gasto ", "$y €"),
        ]

        p = figure(
            title="Gráfica de Gasto",
            x_axis_label='Día',
            y_axis_label='Gasto (€)',
            sizing_mode="stretch_width",
            x_axis_type="datetime",
            tooltips=tooltips
        )

        p.line(x='time', y='cost', source=self.source)

        return p

    def update_source(self, new_data):
        self.source.data = {
            'cost': new_data['price'],
            'time': new_data['datetime'],
            'formatted_date': new_data['datetime'].dt.strftime('%d-%m-%Y'),
            'formatted_time': new_data['datetime'].dt.strftime('%H:%M')
        }
