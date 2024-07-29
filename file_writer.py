import pandas as pd


def write_csv(df, parameters):
    file_name = f"Better_weather_{parameters.location}_{parameters.forecast_period}_{parameters.date}.csv"
    df.to_csv(file_name, index=False)
