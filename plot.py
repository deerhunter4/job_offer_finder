import matplotlib.pyplot as plt
import pandas as pd

# Plot function automatically sets scale to the max value of the variable.
# So even if the there is little precipitation the rain bars will be streach till top of the plot suggesting havy rain fall.
# To avoid this misleading data presentation for low rain forecast the scale will be fixed LOW_RAIN_SCALE_MAX.
# Additionally, for visual clarity we do not want that any part of the graph (bar ot line) touch the top or down of the plot.
# That is why we are adding 10% to the max value of each variable to obtain scale maximum MAX_SCALE_VALUE_RATIO.
# For temperature additionally we decrease min value on the scale by 10% for the same reason MIN_SCALE_VALUE_RATIO.
LOW_RAIN_SCALE_MAX = 10
MAX_SCALE_VALUE_RATIO = 1.1
MIN_SCALE_VALUE_RATIO = 0.1


def create_plot(full_forecast_dataframe, parameters):
    # create plot axes limits
    max_rain = LOW_RAIN_SCALE_MAX
    rain_max = full_forecast_dataframe["mean_rain"].max()*MAX_SCALE_VALUE_RATIO
    if max_rain < rain_max:
        max_rain = rain_max

    max_temp = full_forecast_dataframe["mean_temp"].max()*MAX_SCALE_VALUE_RATIO
    min_temp = full_forecast_dataframe["mean_temp"].min() - full_forecast_dataframe["mean_temp"].max()*MIN_SCALE_VALUE_RATIO

    # create plot
    fig, ax = plt.subplots(figsize=(20, 12)) # plot size (Width x Height) in centimeters
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
    fig.savefig(plot_name, dpi=300) # dpi is picture resolution (higher number better resolution)

    plt.show()
