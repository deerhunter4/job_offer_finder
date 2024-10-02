import pandas as pd


def check_date(forecast_dataframe):
    meteostat_date = forecast_dataframe['hours_meteostat'][0][:10]
    openmeteo_date = forecast_dataframe['hours_openmeteo'][0][:10]
    weatherapi_date = forecast_dataframe['hours_weatherapi'][0][:10]
    if meteostat_date == openmeteo_date and meteostat_date == weatherapi_date:
        forecast_dataframe['date'] = meteostat_date


def check_hour(forecast_dataframe):
    for row_no in range(0, len(forecast_dataframe)):
        meteostat_hour = forecast_dataframe['hours_meteostat'][row_no][11:16]
        openmeteo_hour = forecast_dataframe['hours_openmeteo'][row_no][11:16]
        weatherapi_hour = forecast_dataframe['hours_weatherapi'][row_no][11:16]
        if meteostat_hour == openmeteo_hour == weatherapi_hour:
            forecast_dataframe.loc[row_no, 'hour'] = meteostat_hour


def create_dataframe(weatherapi_dict, openmeteo_dict, meteostat_dict):
    all_data_dict = {**weatherapi_dict, **openmeteo_dict, **meteostat_dict}
    full_forecast_dataframe = pd.DataFrame(all_data_dict)
    full_forecast_dataframe.insert(loc=1, column='hour', value="empty")

    # check if for each forecast point the time period (date and hour) is the same and create variables date and hour
    check_date(full_forecast_dataframe)
    check_hour(full_forecast_dataframe)

    # remove redundand time columns
    full_forecast_dataframe = full_forecast_dataframe.drop(columns=['hours_meteostat', 'hours_openmeteo', 'hours_weatherapi'])

    # sort full_forecast_dataframe by column names
    full_forecast_dataframe = full_forecast_dataframe.reindex(sorted(full_forecast_dataframe.columns), axis=1)

    # count mean temperature and mean precipitation per each time point
    full_forecast_dataframe['mean_rain'] = full_forecast_dataframe.loc[:, ['rain_meteostat', 'rain_openmeteo', 'rain_weatherapi']].mean(axis=1).round(1)
    full_forecast_dataframe['mean_temp'] = full_forecast_dataframe.loc[:, ['temp_meteostat', 'temp_openmeteo', 'temp_weatherapi']].mean(axis=1).round(1)

    return full_forecast_dataframe
