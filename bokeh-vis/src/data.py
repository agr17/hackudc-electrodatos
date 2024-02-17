# SPDX-FileCopyrightText: 2024 Manuel Corujo
# SPDX-FileCopyrightText: 2024 María López
# SPDX-FileCopyrightText: 2024 Pablo Boo
# SPDX-FileCopyrightText: 2024 Ángel Regueiro
#
# SPDX-License-Identifier: MIT

import pandas as pd

def load_data(csv_path):
    df = pd.read_csv(csv_path)
    df['fecha'] = df['fecha'].apply(lambda x: pd.Timestamp(x))
    df['datetime'] = pd.to_datetime(df['datetime'])

    return df

def unify_data(df_consumption, df_costs):
        df = df_consumption.set_index('datetime').join(df_costs.set_index('datetime'))
        df.reset_index(inplace=True)
        return df

def calculate_expenses(df):
    df['expenses'] = df['consumo'] * df['price']
    return df

def data_to_monthly(df):
    df_copy = df.copy()
    df_copy['month'] = df_copy['datetime'].dt.to_period('M')
    result = df_copy.groupby('month').agg({'consumo': 'sum', 'expenses': 'sum'}).reset_index()
    result.columns = ['month', 'consumo', 'expenses']
    return result

def check_year(df, year):
    return int(year) in df['datetime'].dt.year.unique()
