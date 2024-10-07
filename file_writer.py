import pandas as pd


def write_csv_file(dataframe, parameters):
    file_name = f"Better_weather_{parameters.location}_{parameters.forecast_period}_{parameters.date}.csv"
    dataframe.to_csv(file_name, index=False)
