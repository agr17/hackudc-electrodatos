import pandas as pd

def load_data(csv_path):
    df = pd.read_csv(csv_path)
    df['fecha'] = df['fecha'].apply(lambda x: pd.Timestamp(x))
    df['datetime'] = pd.to_datetime(df['datetime'])

    return df