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