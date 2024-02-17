from bokeh.models import ColumnDataSource, FactorRange, Range1d
from bokeh.palettes import Bright7
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

        tooltips = [
            ("Consumo", "@consumption{0.00} kWh"),
            ("Día", "@weekday_name")
        ]

        p = figure(
            title="Media de consumo por día de la semana",
            x_axis_label='Día de la semana',
            y_axis_label='Media de consumo (KWh)',
            sizing_mode="stretch_width",
            x_range=FactorRange(*self.factors),
            tooltips=tooltips,
            toolbar_location=None,
        )

        p.vbar(x=dodge('weekday', 0.50, range=p.x_range), top='consumption', source=self.source, width=0.5, color='color', legend_field="weekday_name")

        p.xgrid.grid_line_color = None
        p.legend.orientation = "horizontal"
        p.legend.location = "top_center"

        # Y range + 20 % max
        p.y_range = Range1d(start=0, end=max(self.source.data['consumption']) * 1.20)

        return p

    def update_source(self, new_data):
        self.source.data = {
            'consumption': new_data['consumption'],
            'weekday': new_data['weekday'],
            'weekday_name': self.factors,
            'color': Bright7
        }
