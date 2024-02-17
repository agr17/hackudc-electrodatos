from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure
from bokeh.layouts import row

from constants import *

class ConsumptionsVisualizer:

    def __init__(self, df):
        super().__init__()
        self.df = df

        self.months = MONTHS
        self.selected_month = self.months[0]

        self.source = ColumnDataSource(data=self._get_empty_source())

    def _get_empty_source(self):
        return {
            'consumption': [],
            'time': [],
        }

    def _get_plot(self):

        tooltips = [
            ("Día", "@time"),
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

        p.line(x='time', y='consumption', source=self.source, line_width=2, line_color=CONSUMPTION_COLOR)
        p.circle(x='time', y='consumption', source=self.source, size=8, color=CONSUMPTION_COLOR)

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
        result = df_copy.groupby('day').agg({'consumo': 'sum'}).reset_index()
        result.columns = ['day', 'consumo']
        result['day'] = result['day'].dt.strftime('%d')

        return result

    def update_source(self):

        filtered_df = self._filter_by_month(self.df, self.months.index(self.selected_month) + 1)

        filtered_df = self._data_to_dayly(filtered_df)

        self.source.data = {
            'consumption': filtered_df['consumo'],
            'time': filtered_df['day'],
        }

    ### GET PLOT ###
    def get_layout(self):
        select_month = self._make_select_month()
        plot = self._get_plot()
        return row(select_month, plot, sizing_mode="stretch_width")
