from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

class DayConsumptionVisualizer:
    def __init__(self):
        super().__init__()
        self.source = ColumnDataSource(data=self._get_empty_source())

    def _get_empty_source(self):
        return {
            'consumption': [],
            'weekday': [],
        }

    def get_plot(self):

        p = figure(
            title="Gráfica de Consumo",
            x_axis_label='Día de la semana',
            y_axis_label='Consumo (KWh)',
            sizing_mode="stretch_width"
        )

        #p.line(x='weekday', y='consumption', source=self.source)
        p.vbar(x='weekday', top='consumption', source=self.source)

        return p

    def update_source(self, new_data):
        print(new_data)
        self.source.data = {
            'consumption': new_data['consumo'],
            'weekday': new_data['datetime']
        }
