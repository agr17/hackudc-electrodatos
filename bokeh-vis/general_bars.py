from bokeh.models import ColumnDataSource, FactorRange, HoverTool
from bokeh.plotting import figure
from bokeh.transform import dodge
from bokeh.models import LinearAxis
class GeneralBars:
    def __init__(self):
        super().__init__()
        self.source = ColumnDataSource(data=self._get_empty_source())
        self.factors = [
            ("Q1", "Enero"), ("Q1", "Febrero"), ("Q1", "Marzo"),
            ("Q2", "Abril"), ("Q2", "Mayo"), ("Q2", "Junio"),
            ("Q3", "Julio"), ("Q3", "Agosto"), ("Q3", "Septiembre"),
            ("Q4", "Octubre"), ("Q4", "Noviembre"), ("Q4", "Diciembre"),
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
            sizing_mode="stretch_width",
            x_range=FactorRange(*self.factors),
            toolbar_location=None,
        )

        vbar_consumption = p.vbar(x=dodge('time', -0.20, range=p.x_range), top='consumption', width=0.3, source=self.source, color="skyblue", legend_label="Consumo")
        vbar_cost = p.vbar(x=dodge('time', 0.20, range=p.x_range), top='cost', width=0.3, source=self.source, color="chocolate", legend_label="Coste")

        # Twin y axis
        p.yaxis.axis_label = "Gasto (€)"
        p.yaxis.axis_label_text_color ="chocolate"

        p.extra_y_ranges = {"consumption": p.y_range}
        p.add_layout(LinearAxis(y_range_name="consumption", axis_label="Consumo (kWh)", axis_label_text_color="skyblue"), 'right')

        # Toolstips
        consumption_tool = HoverTool(renderers=[vbar_consumption], tooltips=[('Consumo', '@consumption{0.00} kWh')])
        cost_tool = HoverTool(renderers=[vbar_cost], tooltips=[('Coste', '@cost{0.00} €')])
        p.add_tools(consumption_tool, cost_tool)

        print(self.source.data)

        return p

    def update_source(self, new_data):

        self.source.data = {
            'consumption': new_data['consumo'],
            'cost': new_data['price'],
            'time': self.factors,
        }