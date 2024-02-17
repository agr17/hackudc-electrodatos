from bokeh.models import ColumnDataSource, Select, CheckboxGroup
from bokeh.plotting import figure
from bokeh.models import LinearAxis
from bokeh.layouts import row, column

from constants import *

class ConsumptionsVisualizer:

    def __init__(self, df):
        super().__init__()
        self.df = df

        self.months = MONTHS
        self.selected_month = self.months[0]

        self.options = {
            'Consumo': True,
            'Coste': True,
        }

        self.consumption_line = None
        self.consumption_circle = None
        self.cost_line = None
        self.cost_circle = None

        self.source = ColumnDataSource(data=self._get_empty_source())

    def _get_empty_source(self):
        return {
            'consumption': [],
            'cost': [],
            'time': [],
        }

    def _get_plot(self):

        p = figure(
            title="Gráfica de Consumo",
            x_axis_label='Día',
            sizing_mode="stretch_width",
            x_axis_type="datetime"
        )

        # Consumo
        self.consumption_line = p.line(x='time', y='consumption', source=self.source, line_width=2, line_color=CONSUMPTION_COLOR)
        self.consumption_circle = p.circle(x='time', y='consumption', source=self.source, size=8, color=CONSUMPTION_COLOR)

        # Coste
        self.cost_line = p.line(x='time', y='cost', source=self.source, line_width=2, line_color=COSTS_COLOR)
        self.cost_circle = p.circle(x='time', y='cost', source=self.source, size=8, color=COSTS_COLOR)

        # Twin y axis
        p.yaxis.axis_label = "Gasto (€)"
        p.yaxis.axis_label_text_color = COSTS_COLOR

        p.extra_y_ranges = {"consumption": p.y_range}
        p.add_layout(LinearAxis(y_range_name="consumption", axis_label="Consumo (kWh)", axis_label_text_color=CONSUMPTION_COLOR), 'right')

        return p

    ### SELECT MONTH ###
    def _select_month_callback(self, attr, old, new):
        if new == self.selected_month:
            return
        else:
            self.selected_month = new
            self.update_source()

    def _make_select_month(self):
        select_month = Select(title="Mes:", value=self.selected_month, options=self.months)
        select_month.on_change('value', self._select_month_callback)
        return select_month

    def _filter_by_month(self, df, month):
        return df[df['datetime'].dt.month == month]

    def _data_to_dayly(self, df):
        df_copy = df.copy()

        df_copy['day'] = df_copy['datetime'].dt.to_period('D')
        result = df_copy.groupby('day').agg({'consumo': 'sum', 'price': 'sum'}).reset_index()
        result.columns = ['day', 'consumo', 'price']
        result['day'] = result['day'].dt.strftime('%d')

        return result

    def update_source(self):

        filtered_df = self._filter_by_month(self.df, self.months.index(self.selected_month) + 1)

        filtered_df = self._data_to_dayly(filtered_df)

        self.source.data = {
            'consumption': filtered_df['consumo'],
            'cost': filtered_df['price'],
            'time': filtered_df['day'],
        }

    ### CHECKBOX ###
    def _checkbox_callback(self, attr, old, new):
        self.options = {CHECKBOX_LABELS[i]: i in new for i in range(len(CHECKBOX_LABELS))}

        self.consumption_line.visible = self.options['Consumo']
        self.consumption_circle.visible = self.options['Consumo']
        self.cost_line.visible = self.options['Coste']
        self.cost_circle.visible = self.options['Coste']

    def _make_checkbox(self):
        checkbox = CheckboxGroup(labels=CHECKBOX_LABELS, active=[0, 1])
        checkbox.on_change('active', self._checkbox_callback)
        return checkbox

    ### GET PLOT ###
    def get_layout(self):
        select_month = self._make_select_month()
        checkbox = self._make_checkbox()

        visualizar_options = column(select_month, checkbox)

        plot = self._get_plot()
        return row(visualizar_options, plot, sizing_mode="stretch_width")
