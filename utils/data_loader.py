import pandas as pd
import yaml

def load_config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(df, time_column, metric_column, value_column):
    df[time_column] = pd.to_datetime(df[time_column])
    df.set_index(time_column, inplace=True)
    return df