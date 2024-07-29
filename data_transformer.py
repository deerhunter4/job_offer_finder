import pandas as pd


def create_dataframe(dict1, dict2, dict3):
    all_data_dict = {**dict1, **dict2, **dict3}
    df = pd.DataFrame(all_data_dict)

    # check if for each forecast point the time period (date and hour) is the same and create variables date and hour
    if df['hours_meteostat'][0][:10] == df['hours_openmeteo'][0][:10] and df['hours_meteostat'][0][:10] == df['hours_weatherapi'][0][:10]:
        df['date'] = df['hours_meteostat'][0][:10]

    df.insert(loc=1, column='hour', value="empty")
    for row_no in range(0, len(df)):
        if df['hours_meteostat'][row_no][11:16] == df['hours_openmeteo'][row_no][11:16] == df['hours_weatherapi'][row_no][11:16]:
            df.loc[row_no, 'hour'] = df['hours_meteostat'][row_no][11:16]

    df = df.drop(columns=['hours_meteostat', 'hours_openmeteo', 'hours_weatherapi'])

    # sort DF by column names
    df = df.reindex(sorted(df.columns), axis=1)

    # count mean temperature and mean precipitation
    df['mean_rain'] = df.loc[:, ['rain_meteostat', 'rain_openmeteo', 'rain_weatherapi']].mean(axis=1).round(1)
    df['mean_temp'] = df.loc[:, ['temp_meteostat', 'temp_openmeteo', 'temp_weatherapi']].mean(axis=1).round(1)

    return df
