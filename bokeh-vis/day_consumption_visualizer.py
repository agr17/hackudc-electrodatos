from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure
from bokeh.transform import dodge

class DayConsumptionVisualizer:
    def __init__(self):
        super().__init__()
        self.source = ColumnDataSource(data=self._get_empty_source())
        self.factors = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    def _get_empty_source(self):
        return {
            'consumption': [],
            'weekday': [],
        }

    def get_plot(self):

        p = figure(
            title="Consumo por día de la semana",
            x_axis_label='Día de la semana',
            y_axis_label='Consumo (KWh)',
            sizing_mode="stretch_width",
            x_range=FactorRange(*self.factors)
        )

        p.vbar(x=dodge('weekday', 0.50, range=p.x_range), top='consumption', source=self.source, width=0.5)


        return p

    def update_source(self, new_data):
        self.source.data = {
            'consumption': new_data['consumption'],
            'weekday': new_data['weekday']
        }
