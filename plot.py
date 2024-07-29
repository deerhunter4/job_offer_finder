import matplotlib.pyplot as plt
import pandas as pd

# df = pd.read_csv("test_for_plot.txt", sep="\t")
# df['mean_rain'] = [0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 11.0, 20.0, 17.0,
#                    6.0, 0.5, 0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0,
#                    0.0, 0.0, 0.0, 0.2, 0.1, 0.2]


def create_plot(df, parameters):
    # create plot axes limits
    max_rain = 10
    rain_max = df["mean_rain"].max()*1.1
    if max_rain < rain_max:
        max_rain = rain_max

    max_temp = df["mean_temp"].max()*1.1
    min_temp = df["mean_temp"].min() - df["mean_temp"].max()*0.1

    # create plot
    fig, ax = plt.subplots()
    # plt.tick_params(axis='y', which='both', labelleft=False, labelright=True)
    # fig = plt.figure(figsize=(12, 8))
    ax.bar(df['hour'], df['mean_rain'], color='blue')
    ax.set_title(f'Weather forecast: {parameters.location}, {parameters.date}', fontsize=18)
    ax.set_xlabel('Time [hour]', fontsize=16)
    ax.set_ylabel('Precipitation [mm]', fontsize=16)
    ax.set_ylim(0, max_rain)

    ax2 = ax.twinx()
    ax2.plot(df['hour'], df['mean_temp'], marker='o', color='red', linewidth=2)
    ax2.set_ylabel('Temperature [C]', fontsize=16)
    ax2.set_ylim(min_temp, max_temp)
    plot_name = f"Better_weather_{parameters.location}_{parameters.forecast_period}_{parameters.date}.pdf"
    fig.savefig(plot_name, dpi=300)
    plt.show()
