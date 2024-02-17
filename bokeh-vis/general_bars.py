from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure
import datetime

class GeneralBars:
    def __init__(self):
        super().__init__()
        self.source = ColumnDataSource(data=self._get_empty_source())
        self.factors = [
            ("Q1", "jan"), ("Q1", "feb"), ("Q1", "mar"),
            ("Q2", "apr"), ("Q2", "may"), ("Q2", "jun"),
            ("Q3", "jul"), ("Q3", "aug"), ("Q3", "sep"),
            ("Q4", "oct"), ("Q4", "nov"), ("Q4", "dec"),
        ]

    def _get_empty_source(self):
        return {
            'consumption': [],
            'cost': [],
            'time': [],
        }

    def get_plot(self):
        p = figure(
            title="Gráfica de Gasto",
            x_axis_label='Mes',
            y_axis_label='Gasto (€)',
            sizing_mode="stretch_width",
            x_range=FactorRange(*self.factors)
        )

        p.vbar(x='time', top='consumption', width=0.5, source=self.source)
        p.line(x='time', y='cost', line_width=2, color="red", source=self.source)

        return p

    def update_source(self, new_data):

        self.source.data = {
            'consumption': new_data['consumo'],
            'cost': new_data['price'],
            'time': self.factors,
        }
