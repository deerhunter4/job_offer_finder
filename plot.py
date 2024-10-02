import matplotlib.pyplot as plt
import pandas as pd


def create_plot(full_forecast_dataframe, parameters):
    # create plot axes limits
    max_rain = 10
    rain_max = full_forecast_dataframe["mean_rain"].max()*1.1
    if max_rain < rain_max:
        max_rain = rain_max

    max_temp = full_forecast_dataframe["mean_temp"].max()*1.1
    min_temp = full_forecast_dataframe["mean_temp"].min() - full_forecast_dataframe["mean_temp"].max()*0.1

    # create plot
    fig, ax = plt.subplots(figsize=(20, 12))
    ax.bar(full_forecast_dataframe['hour'], full_forecast_dataframe['mean_rain'], color='blue')
    ax.set_title(f'Weather forecast: {parameters.location}, {parameters.date}', fontsize=18)
    ax.set_xlabel('Time [hour]', fontsize=16)
    ax.set_ylabel('Precipitation [mm]', fontsize=16)
    ax.set_ylim(0, max_rain)
    ax.grid()

    ax2 = ax.twinx()
    ax2.plot(full_forecast_dataframe['hour'], full_forecast_dataframe['mean_temp'], marker='o', color='red', linewidth=2)
    ax2.set_ylabel('Temperature [C]', fontsize=16)
    ax2.set_ylim(min_temp, max_temp)
    plot_name = f"Better_weather_{parameters.location}_{parameters.forecast_period}_{parameters.date}.pdf"
    fig.savefig(plot_name, dpi=300)

    plt.show()
